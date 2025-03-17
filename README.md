# Color Scheme - Dracula

This is a Sublime Text (and Merge) color scheme using the [Dracula color palette](https://github.com/dracula/dracula-theme).
Our implementation of Dracula uses the Sublime Text Mariana color scheme as a starting point and makes some alterations
to better accommodate the Dracula color palette.

We provide both classic and Pro variants of Dracula in our color schemes. The Pro variants use the color palette which
can be easily be obtained from [Dracula Pro's official site](https://draculatheme.com/pro).

In regards to Pro color schemes, it should be noted that we only use the color palettes that we extract from the
official Pro site which are publicly on display. We have not, in any way, referenced official Pro themes provided by the
official Dracula organization. We've been careful to build the Pro color schemes only our work related to classic
Dracula, simply swapping out the color palette.

![Sublime Text](screenshots/Text%20-%20Dracula.png)

![Sublime Merge](screenshots/Merge%20-%20Dracula.png)

## Install

Git clone the project or download the project to your Sublime Text or Sublime Merge Packages folder as
`Color Scheme - Dracula`. If you want to use it in both Sublime Merge and Sublime Text, you only have to install it in
Sublime Text as Sublime Merge will find the color schemes in Sublime Text.

For Sublime Text, edit your `Preferences.sublime-settings` file to use the Dracula theme:

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula Classic.sublime-color-scheme",
```

For Sublime Merge, once installed, it is recommended to install the [Sublime Merge theme](https://github.com/facelessuser/merge-dracula-theme)
and follow related theme instructions.

## Dracula Pro

**We are not affiliated with Dracula Pro, nor do we condone using the official paid for themes without paying for them,
but this theme is an original work that uses the Dracula Pro palette, the theme itself is not derived from the source of
any official Dracula theme.**

The official [Dracula Pro](https://draculatheme.com/pro) color schemes changed up the color palette of the original,
classic Dracula and added new variants such as Buffy, Van Helsing, and others. The author offers a number of supported
themes (and additional goodies) for a price. For anyone interested in the wealth of themes that may be offered by the
official author, we recommend you check out out the official Dracula Pro. If you don't mind a non-official
interpretation on Dracula Pro, or prefer our take on the Pro theme, then give these color schemes a try.

Our themes are simply inspired by the color palette that can easily be acquired by visiting the [Dracula Pro](https://draculatheme.com/pro)
site. The site has all the colors on display, and the few that are not can be inferred from the ones that are present.
That is how we determined the colors in our variants.

The Pro color scheme normalized saturation and lightness of colors in the HSL color space. These colors, while not
placed exactly in a geometrically, symmetrical layout, are more uniform within the HSL color space. With that said, this
does not mean the colors are perceptually uniform as HSL is not perceptually uniform at all.

As previously mentioned, the main foreground colors are directly found within the official Dracula site. Background
colors can be extracted from the images showing previews of the different themes, and a number of the icons in the page
seem to use colors that correspond to the comment colors in certain themes.

After simply gathering the main foreground and background colors, and analyzing other colors on the site, comments were
determined to be based off the background using a normalized saturation and lightness.

```js
"comment": "color(var(background) s(25%) l(55%))",
```

Selections and line highlights were the only colors that were not immediately clear, and out of the few theme previews
that showed line highlights, the actual colors being used seemed to differ sometimes depending on the theme. The
following colors were settled on for selections and line highlights after analyzing screenshots of different themes and
determining what seemed to be the most reasonable and least intrusive colors.

```js
"selection": "color(var(background) s(15%) l(30%))",
"line-highlight": "color(var(background) s(25%) l(25%))",
```

We did define one additional color to the palette in order to define something for Sublime Text's `blueish` variable. We
simply took the hue of the old Dracula comment, which has a much more bluish hue than the official cyan color, and
normalized and saturation and lightness to match the other Dracula foreground colors. It is never used in actual syntax
highlighting except in the case of Alucard Pro which uses the classic hue for the comments. Additionally, it may be used
as a theme accent or additional color in Sublime Merge commit graphs.

It should be noted that the Alucard Pro theme was recently added and deviates some from the dark theme approach.
Currently, it uses colors as close as we were able to get using analysis for comments, line highlights, and base
colors.

### Dracula Pro:

![Pro](screenshots/Text%20-%20Pro.png)

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula Pro.sublime-color-scheme",
```

### Dracula Pro (Buffy)

![Buffy](screenshots/Text%20-%20Buffy.png)

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula Pro (Buffy).sublime-color-scheme",
```

### Dracula Pro (Blade)

![Blade](screenshots/Text%20-%20Blade.png)

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula Pro (Blade).sublime-color-scheme",
```

### Dracula Pro (Lincoln)

![Lincoln](screenshots/Text%20-%20Lincoln.png)

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula Pro (Lincoln).sublime-color-scheme",
```

### Dracula Pro (Morbius)

![Morbius](screenshots/Text%20-%20Morbius.png)

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula Pro (Morbius).sublime-color-scheme",
```

### Dracula Pro (Van Helsing)

![Van Helsing](screenshots/Text%20-%20Van%20Helsing.png)

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula Pro (Van Helsing).sublime-color-scheme",
```

### Dracula Pro (Alucard)

![Alucard](screenshots/Text%20-%20Alucard.png)

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula Pro (Alucard).sublime-color-scheme",
```

### Dracula Pro (Nosferatu)

Nosferatu Pro is our take on a Pro theme with the classic Dracula background and comments. It gives a more bluish
background hue than the purple hue of the normal Pro theme. We feel this combination was a missed opportunity for lovers
of the original Dracula.

![Nosferatu](screenshots/Text%20-%20Nosferatu.png)

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula Pro (Nosferatu).sublime-color-scheme",
```

## Modifying Color Schemes

To modify color schemes, make sure you've installed PyYAML.

```console
$ pip install pyyaml
```

Changes should be made under the `src` folder in the appropriate YAML file. Then `build.py` should be run to generate
the `.sublime-color-scheme` files.

## Customize Merge

The [Dracula Merge theme](https://github.com/facelessuser/merge-dracula-theme) theme dynamically sources its colors
from the color scheme. While you are free to provide overrides to the theme, it would normally be recommended to apply
overrides to the color scheme if all you want is to tweak the color palette. Overriding the color scheme is all we will
be covering at this time. You are free to override the Merge theme if you desire, but you will have to explore the inner
workings on you own.
