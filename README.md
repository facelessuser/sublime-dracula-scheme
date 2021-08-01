# Color Scheme - Dracula

This is a Sublime Text (and Merge) color scheme using the [Dracula color palette](https://github.com/dracula/dracula-theme).
Our implementation of Dracula uses the Sublime Text Mariana color scheme as a template with the Dracula color palette.

![Sublime Text](screenshots/Text%20-%20Dracula.png)

![Sublime Merge](screenshots/Merge%20-%20Dracula.png)

## Install

Git clone the project or download the project to your Sublime Text or Sublime Merge Packages folder as
`Color Scheme - Dracula`. If you want to use it in both Sublime Merge and Sublime Text, you only have to install it in
Sublime Text as Sublime Merge will find the color schemes in Sublime Text.

For Sublime Text, edit your `Preferences.sublime-settings` file to use the Dracula theme:

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula.sublime-color-scheme",
```

For Sublime Merge, once installed, it is recommended to install the [Sublime Merge theme](https://github.com/facelessuser/merge-dracula-theme)
and follow related theme instructions.

## Alternative Scheme: Alucard

An alternative color scheme is also provided called `Dracula (Alucard)`. It is just like Dracula, but we take some
liberties and "fix" issues that we find problematic in the original, classic `Dracula`. One such issue is line
highlight. Our personal belief is that the chosen line highlight color does not work well with the comment color, so we
have chosen a color that is more subtle, looks better with the background, and makes text easier to read.

![Alucard](screenshots/Text%20-%20Alucard.png)

To use `Dracula (Alucard)`, simply set color scheme to:

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula (Alucard).sublime-color-scheme",
```

## Dracula Pro?

Dracula Pro changed up the color palette a bit and added new variants such as Buffy, Van Helsing, and others. Dracula
Pro is also not free. Because of this, we only provide the "classic" Dracula palette.

We'd love to provide Pro variants, and we already have variants ready in a private repository, but while we think we
have figured out the color palette for the new Pro variants, we have chosen not to release it at this time as we do not
want our repository taken down. While a reasonable argument could be made that the colors themselves cannot be
copyrighted and we have not seen the official Dracula Pro source and have not copied any actual theme sources, we do not
feel it would be proper to release our variants at this time.

For those who've acquired Pro through purchasing, the current color scheme can be used as a base to easily and quickly
create Pro variants. We've created a section to help guide interested parties who have purchased Dracula Pro or others,
like us, who have deduced what the actual colors are. Check out [How to Create Pro Variants](#how-to-create-pro-variants)
for more info.

If at some future time the Pro color palette becomes available to the public, we will be happy to provide theme
variants here as well. It is not a matter of the paid themes themselves becoming public, but mainly the palette. If
it appears to generally be safe to create custom interpretations using the color palette, then we will be happy to
distribute our own take here.

## How to Create Pro Variants?

Assuming you have access to the official Pro variant colors, or feel you have deduced what these colors are, you can
modify the provided color scheme with the official Dracula Pro color palette. If you wish to create Pro color schemes
that work with the [Sublime Merge theme](https://github.com/facelessuser/merge-dracula-theme), you should use the names
found below when creating your Pro color schemes:

- Pro: `Dracula Pro.sublime-color-scheme`
- Buffy: `Dracula Pro (Buffy).sublime-color-scheme`
- Blade: `Dracula Pro (Blade).sublime-color-scheme`
- Lincoln: `Dracula Pro (Lincoln).sublime-color-scheme`
- Morbius: `Dracula Pro (Morbius).sublime-color-scheme`
- Van Helsing: `Dracula Pro (Van Helsing).sublime-color-scheme`

Using the `Dracula.sublime-color-scheme` as a base (found [here](https://github.com/facelessuser/sublime-dracula-scheme/blob/master/Dracula.sublime-color-scheme)),
simply change the main palette colors below to the appropriate, official colors. These colors will be the same for all
Pro color schemes except for `background` and `comment` which are variant specific colors.

```js
        // Static palette colors. These are constant through all variations.
        "foreground": "",
        "red": "",
        "orange": "",
        "yellow": "",
        "green": "",
        "cyan": "",
        "blue": "", // <- Blue is not actually from the Dracula palette per se. See below for more info.
        "pink": "",
        "purple": "",

        // Variant specific colors (change these for variants)
        "background": "",
        "comment": ""
```

It should be noted that `blue` is not a defined color in the official Dracula color palette or Pro color palette. But
`blue` is used as an additional color for themes when more color variants are needed. Also, Sublime provides `bluish`
and `cyanish` variables, and when plugins or popups specify these variables, expecting unique colors, unless an
appropriate color is provided, Sublime will just reuse an existing color. We specify `blue` to ensure that popups and
plugins that use both `cyanish`, `bluish` and/or `purplish` will yield a unique color. While `blue` is not used in the
actual syntax highlighting of code, it is used as a recommend accent color for a couple of the color schemes and is used
as an additional color in the commit graph and blame view in our Merge theme.

In the classic Dracula color scheme, we simply take the `comment` color which has a bluish hue and normalize the
saturation and lightness to get a more vibrant blue which matches the feel of the Dracula palette: `hsl(225 27% 51%)` ->
`hsl(255 100% 75%)`. For Pro, the Van Helsing background, while extremely dark, actually uses a blue hued color, and we
take that color and normalize its saturation and lightness to create a suitable "Pro" `blue`. Assuming you have the Van
Helsing color converted to its HSL color form, simply take the hue of the Van Helsing background and apply the same saturation and lightness that all the other main colors use.

If you are trying to reverse engineer the color schemes yourselves, `color(var(background) s(25%) l(55%))` for `coment`
is honestly a very close, generic solution (assuming you have a background that matches the official). The official
color schemes seem to be very close to this with a few color schemes deviating slightly, but not in a significant way
that most people would notice unless comparing the colors very, very closely.

Next, we generically set `selection` and `line-highlight` to the following. Again, these might not be exactly what is
used in the official Pro color schemes, but these look really good and are more than sufficient. If you have the
official color schemes and determine those to be superior, feel free to use those instead.

```js
        // Variant specific colors (change these for variants)
        "selection": "color(var(background) s(15%) l(30%))",
        "line-highlight": "color(var(background) s(25%) l(25%))",
```

This gives a generally good line looking line highlight and selection. You could just as easily use the `line-highlight`
setting for `selection` as well if you wanted the same, more subtle highlight for selections.

Lastly, we pick a color from the main palette for the `accent`. While we recommend using a palette color that matches
the overall dominant hue in the color scheme, this can really be set to anything that is preferred. We will post our
recommendations below:

```js
        "accent": "var(purple)" // Pro
        "accent": "var(pink)"   // Buffy
        "accent": "var(cyan)"   // Blade
        "accent": "var(yellow)" // Lincoln
        "accent": "var(red)"    // Morbius
        "accent": "var(blue)"   // Van Helsing
        "accent": "var(blue)"   // Alucard
```

The Pro version of Alucard is exactly like the classic Alucard except it uses the Pro color palette. Like above, one
would update all the main colors with the official Dracula Pro colors except for `background` and `comment`.
`background` and `comment` should use the same colors as the original Dracula color scheme which gives the color scheme
an updated, but classic look. `selection` and `line-highlight` would use the same values as the rest of the Pro color
schemes and use a recommended `accent` of `var(blue)`.

```js
        // Variant specific colors (change these for variants)
        "background": "hsl(231, 15%, 18%)",
        "selection": "color(var(background) s(15%) l(30%))",
        "comment": "hsl(225, 27%, 51%)",
        "line-highlight": "color(var(background) s(25%) l(25%))",
        "accent": "var(blue)",
```

Using the steps above, and a little sleuthing in regards to the main colors, we were able to create Pro variants that
match very close. While we have not purchased the official Dracula color scheme, and do not know the exact colors, we
are fairly certain that the below images are a very close approximation and, if steps were followed with the official
colors, would yield a very similar result.

Dracula Pro:

![Pro](screenshots/Text%20-%20Pro.png)

Dracula Pro (Alucard)

![Alucard](screenshots/Text%20-%20Alucard%20Pro.png)

Dracula Pro (Buffy)

![Buffy](screenshots/Text%20-%20Buffy.png)

Dracula Pro (Blade)

![Blade](screenshots/Text%20-%20Blade.png)

Dracula Pro (Lincoln)

![Lincoln](screenshots/Text%20-%20Lincoln.png)

Dracula Pro (Morbius)

![Morbius](screenshots/Text%20-%20Morbius.png)

Dracula Pro (Van Helsing)

![Van Helsing](screenshots/Text%20-%20Van%20Helsing.png)

## Customize Merge

The [Dracula Merge theme](https://github.com/facelessuser/merge-dracula-theme) theme dynamically sources its colors
from the color scheme. While you are free to provide overrides to the theme, it would normally be recommended to apply
overrides to the color scheme if all you want is to tweak the color palette. Overriding the color scheme is all we will
be covering at this time. You are free to override the Merge theme if you desire, but you will have to explore the inner
workings on you own.
