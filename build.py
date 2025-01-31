"""
Parse color schemes from YAML source and extend and override them.

Licensed under MIT
Copyright (c) 2025 Isaac Muse <isaacmuse@gmail.com>
"""
import yaml
import glob
import json
from collections import OrderedDict
import copy
import os


def yaml_load(stream, loader=yaml.Loader):
    """
    Make all YAML dictionaries load as ordered Dicts.

    http://stackoverflow.com/a/21912744/3609487
    """

    def construct_mapping(loader, node):
        """Keep dict ordered."""

        loader.flatten_mapping(node)
        return OrderedDict(loader.construct_pairs(node))

    class Loader(loader):
        """Custom loader."""

    Loader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping
    )

    return yaml.load(stream, Loader)


def yaml_dump(data, stream=None, dumper=yaml.Dumper, **kwargs):
    """Special dumper wrapper to modify the yaml dumper."""

    class Dumper(dumper):
        """Custom dumper."""

    # Handle Ordered Dict
    Dumper.add_representer(
        OrderedDict,
        lambda self, data: self.represent_mapping('tag:yaml.org,2002:map', data.items())
    )

    return yaml.dump(data, stream, Dumper, **kwargs)



def yaml_convert_to(obj, strip_tabs=False):
    """Convert specific serialized objects before converting to YAML."""

    if isinstance(obj, dict):
        for k, v in obj.items():
            obj[k] = yaml_convert_to(v, strip_tabs)
    elif isinstance(obj, list):
        count = 0
        for v in obj:
            obj[count] = yaml_convert_to(v, strip_tabs)
            count += 1
    elif isinstance(obj, str):
        if strip_tabs:
            obj = obj.replace("\t", "    ").rstrip(" ")

    return obj



def yaml_dumps(obj, default_flow_style=False, indent=4, strip_tabs=False):
    """Wrapper for yaml dump."""

    return yaml_dump(
        yaml_convert_to(obj, strip_tabs),
        width=None,
        indent=indent,
        allow_unicode=True,
        default_flow_style=default_flow_style,
        sort_keys=False
    )


def override_keys(obj, obj2):
    """
    Override keys in the color scheme.

    `rules` will just have new rules appended.
    """
    for key in obj2:
        if key in obj:
            if isinstance(obj2[key], dict) and isinstance(obj[key], dict):
                override_keys(obj[key], obj2[key])
            elif key == 'rules' and isinstance(obj[key], list) and isinstance(obj2[key], list):
                obj[key].extend([copy.deepcopy(i) for i in obj2[key]])
            else:
                obj[key] = copy.deepcopy(obj2[key])
        else:
            obj[key] = copy.deepcopy(obj2[key])


def parse(file, obj2=None, relative='.'):
    """Extend a color scheme."""
    yml = os.path.join(relative, file) if file.startswith(('./', '../')) else file
    base = os.path.dirname(yml)
    with open(yml, 'r') as f:
        obj = yaml_load(f.read())

    extend = ''
    overrides = []
    if 'extends' in obj:
        extend = obj.pop('extends')
    if 'overrides' in obj:
        overrides = obj.pop('overrides')

    if obj2:
        override_keys(obj, obj2)

    if extend:
        obj = parse(extend, obj, base)

    for o in overrides:
        yml = os.path.join(relative, o) if o.startswith(('./', '../')) else o
        base = os.path.dirname(yml)
        i = parse(yml, None, base)
        override_keys(obj, i)

    return obj


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(prog='build.py', description='Build tool for color schemes.')
    parser.add_argument('--build', '-b', help='Build a specific color schemes.')
    parser.add_argument('--convert', '-c', help="Convert a scheme into a YAML file.")
    parser.add_argument('--output', '-o', default='.', help="Output path.")
    args = parser.parse_args()

    if not args.convert:
        if args.build:
            files = [args.build]
        else:
            files = glob.iglob('**/*.sublime-color-scheme.YAML', recursive=True)

        # Parse the YAML source to generate JSON color schemes.
        for file in files:
            folder = os.path.dirname(file)
            name = f'./{os.path.basename(file)}'
            output = os.path.join(args.output, f"{name}".rstrip('.YAML'))
            if name.lower().startswith('./hidden'):
                continue
            obj = parse(name, None, folder)
            print(f'Building: {file}\n    -> {output}')
            with open(output, 'w') as f:
                f.write(json.dumps(obj, sort_keys=False, indent=4, separators=(',', ': ')) + '\n')
    elif args.convert:
        with open(args.convert, 'r') as f:
            j = json.loads(f.read())
            yml = yaml_dumps(j)
        output = os.path.basename(args.convert) + '.YAML'
        output = os.path.join(args.output, output)
        with open(output, 'w') as f:
            f.write(yml)
