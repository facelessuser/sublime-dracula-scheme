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
have figured out the color palette for the new Pro variants, we have chosen not to release it at this time. While a
reasonable argument could be made that the colors themselves cannot be copyrighted and we have not seen the official
Dracula Pro source and have not copied any actual theme sources, we do not feel it would be proper to release our
variants at this time.

For those who've acquired Pro through purchasing, the current color scheme can be customized with overrides to provide
Pro styles.

If at some future time the Pro color palette becomes available to the public, we will be happy to provide theme
variants here as well. It is not a matter of the paid themes themselves becoming public, but mainly the palette. If
it appears to generally be safe to create custom interpretations using the color palette, then we will be happy to
distribute our own take here.

## Customize Color Scheme

Customizing the color scheme can be useful if you'd like to tweak the background to be darker, tweak the accents, or
even update the palette for something like Dracula Pro variants or even your own custom take.

The color scheme provides a number of variables for the purpose of overrides.

This color scheme is designed in such a way as to be customizable. Simply override the variables with the color of your
choice. You can create an override file using the name `Dracula.sublime-color-scheme` in your `User` folder.

## How to Create Pro Variants?

Assuming you have access to the official Pro variant colors, Merge requires the following color schemes to be found:

- Pro: `Dracula Pro.sublime-color-scheme`
- Buffy: `Dracula Pro (Buffy).sublime-color-scheme`
- Blade: `Dracula Pro (Blade).sublime-color-scheme`
- Lincoln: `Dracula Pro (Lincoln).sublime-color-scheme`
- Morbius: `Dracula Pro (Morbius).sublime-color-scheme`
- Van Helsing: `Dracula Pro (Van Helsing).sublime-color-scheme`

Using the `Dracula (Alucard).sublime-color-scheme` as a base (found [here](https://github.com/facelessuser/sublime-dracula-scheme/blob/master/Dracula%20(Alucard)),
simply change the palette colors below to the appropriate, offical colors.

```js
        // Static palette colors. These are constant through all variations.
        "foreground": "hsl(60, 30%, 96%)", // #f8f8f2
        "red": "hsl(0, 100%, 67%)",        // #ff5555
        "orange": "hsl(31, 100%, 71%)",    // #ffb86c
        "yellow": "hsl(65, 92%, 76%)",     // #f1fa8c
        "green": "hsl(135, 94%, 65%)",     // #50fa7b
        "cyan": "hsl(191, 97%, 77%)",      // #8be9fd
        "blue": "hsl(225, 100%, 75%)",     // #809fff
        "pink": "hsl(326, 100%, 74%)",     // #ff79c6
        "purple": "hsl(265, 89%, 78%)",    // #bd93f9
```

It should be noted that the official Dracula color scheme doesn't really specify a `blue` color, and in the classic
color scheme, we specified the comment color as the `blue`, but in the Pro color schemes, it is defined as a color with
the dominant hue as used in the Van Helsing variant (background hue) but lightened and saturated to match the other
primary colors. We specify this color for any plugins or themes that attempt to reference `bluish` colors. While `blue`
will not be used in normal syntax highlighting it is recommend as a good `accent` color for Van Helsing and Alucard and
is used as an additional branch color in Merge etc.

Lastly, edit the "Variant Specific" section as shown below. The `background` and `comment` can be pulled directly from
the official Dracula Pro color schemes. It can be noted that we use the general `color(var(background) s(25%) l(55%))`
value for `comment`, and while it may not be the "exact" comment color of what the official Dracula Pro color scheme may
use, we've found it to be more than close enough. `accent` can really be anything, but we will mention our personal
recommendations below as well. 

```js
        // Variant specific colors (change these for variants)
        "background": "", // <-- Enter official color here
        "selection": "color(var(background) s(15%) l(30%))",
        "comment": "color(var(background) s(25%) l(55%))", // <-- Use this or the official color from Dracula Pro
        "line-highlight": "color(var(background) s(25%) l(25%))",
        "accent": "",  // <-- Pick a color you like or one of our recommendation below
```

Since Alucard uses classic colors for `background` and `comment`, we can post exactly what we use:

```js
        // Variant specific colors (change these for variants)
        "background": "hsl(231, 15%, 18%)",
        "selection": "color(var(background) s(15%) l(30%))",
        "comment": "hsl(225, 27%, 51%)",
        "line-highlight": "color(var(background) s(25%) l(25%))",
        "accent": "var(blue)",
```

Recommend accent values:

- Pro: `var(purple)`
- Buffy: `var(pink)`
- Blade: `var(cyan)`
- Lincoln: `var(yellow)`
- Morbius: `var(red)`
- Van Helsing: `var(blue)`
- Alucard: `var(blue)`

## Customize Merge

The [Dracula Merge theme](https://github.com/facelessuser/merge-dracula-theme) theme dynamically sources its colors
from the color scheme. While you are free to provide overrides to the theme, it would normally be recommended to apply
overrides to the color scheme if all you want is to tweak the color palette. Overriding the color scheme is all we will
be covering at this time. You are free to override the Merge theme if you desire, but you will have to explore the inner
workings on you own.
