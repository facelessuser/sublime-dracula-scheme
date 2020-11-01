# Color Scheme - Dracula

These is a Sublime Text (and Merge) color scheme using the [Dracula color palette](https://github.com/dracula/dracula-theme).
Our implementation of Dracula uses the Sublime Text Mariana color scheme as a template with the Dracula color palette.

![Sublime Text](screenshots/Text%20-%20Dracula.png)

![Sublime Merge](screenshots/Merge%20-%20Dracula.png)

## Install

Git clone project or download project to your Sublime Text or Sublime Merge Packages folder as `Color Scheme - Dracula`.
If you use in both Sublime Merge and Sublime Text, you only have to install it in Sublime Text as Sublime Merge will
find the color schemes in Sublime Text.

For Sublime Text, edit your `Preferences.sublime-settings` file to use the Dracula theme:

```js
    "color_scheme": "Packages/Color Scheme - Dracula/Dracula.sublime-color-scheme",
```

For Sublime Merge, once installed, it is recommended to install the [Sublime Merge theme](https://github.com/facelessuser/merge-dracula-theme)
and follow related theme instructions.

## Dracula Pro?

Dracula Pro changed up the color palette a bit and added new variants such as Buffy, Van Helsing, and others. Dracula
Pro is also not free. Because of this, we only provide the "classic" Dracula palette.

We'd love to provide Pro variants, but while we think we have figured out the color palette for new Pro variants,
without the Pro color scheme being made public, we do not feel it would be proper to release our variants here.

For those who've acquired Pro through purchasing, the current color scheme can be customized with overrides to provide
Pro styles.

If at some future time, the Pro public scheme becomes available to the public, we will be happy to provide theme
variants here as well.

## Customize

The Dracula Pro Merge theme dynamically sources it's colors from the color scheme. While you are free to provide
overrides to the theme, it would normally be recommended to apply overrides to the color scheme if all you want is to
tweak the palette. Overriding the color scheme is all we will be covering at this time.

Customizing the color scheme can be useful if you'd like to things like tweak the background to be darker, or tweak
accents or even to update the palette for something like Dracula Pro variants, or even your own custom palette.

The color scheme provides a number of variables for the purpose of overrides.


This color scheme is designed in such a way as to be customizable. Simply override the background with the color of your
choice, and create comments and selections that adapt based on your background selection (or other color if you choose).
You can create an override file using the name `Dracula.sublime-color-scheme` in your `User` folder.

Want a pinkish theme? Plug in a pink hued background and tweak a couple variables. We will talk about them in sections:

1.  The base palette colors are the base Dracula colors. When creating a Dracula theme, these are the least likely to
    require overriding or it would no longer be a Dracula theme. This defines all the foreground colors. If you, for
    instance, knew the Pro palettes, you would most likely these with the new Pro palette, which would be the same
    across all variants.

    ```js
    // Static palette colors. These are constant through all variations.
    "foreground": "hsl(60, 30%, 96%)", // #f8f8f2
    "red": "hsl(0, 100%, 67%)",        // #ff5555
    "orange": "hsl(31, 100%, 71%)",    // #ffb86c
    "yellow": "hsl(65, 92%, 76%)",     // #f1fa8c
    "green": "hsl(135, 94%, 65%)",     // #50fa7b
    "cyan": "hsl(191, 97%, 77%)",      // #8be9fd
    "blue": "hsl(225, 27%, 51%)",      // #6272a4
    "pink": "hsl(326, 100%, 74%)",     // #ff79c6
    "purple": "hsl(265, 89%, 78%)",    // #bd93f9
    ```

    Dracula doesn't really define a "blue" per se, but here "blue" represents the classic palette's blue-ish comments.

1.  The next section provides a number of colors that it is expected users would alter for color scheme variants. This
    defines colors such as comments, backgrounds, line highlights, selections, etc.

    ```js
    // Variant specific colors (change these for variants)
    "background": "hsl(231, 15%, 18%)", // #282a36
    "selection": "hsl(232, 14%, 31%)",  // #44475a
    "comment": "var(blue)",             // #6272a4
    "line-highlight": "var(selection)",
    "accent": "var(blue)",
    ```

    If attempting a Pro style variant, you may want to change the `background`. You may want to derive `comment` from
    one of the core colors (adjusting saturation and lightness). You may want to derive a new `selection` from your new
    `background` color. You may also want a different accent color.

1. The last group of variables touch items that are less likely to require modification, though you may want to make the
   caret stand out more by setting it to `pink`, or maybe you wish to alter the `highlight` of find results.

   ```js
    // UI elements derived from color schemes
    "caret": "var(foreground)",
    "block-caret": "var(caret)",
    "highlight": "var(yellow)",
    "shadow": "hsl(0, 0%, 0%)",
    "stack": "color(var(comment) s(100%) l(75%))",
    "darken": "hsl(0, 0%, 13%)",
    ```

For an example, let's say we wanted to create our own unofficial Van Helsing variant. Dracula Pro provides a darker
variant called Van Helsing. We will not give the actual Van Helsing palette, but simply show how to make one with the
"classic" palette.

-   We will take the existing `blue` that we use for comments and darken it and adjust the saturation considerably.
-   We will derive a selection from that is similar to the background but lighter.
-   We will derive a comment that also matches the background, but stands out.
-   We will derive a line highlight from the background as well, though you could just use `selection` as a suitable
    line highlight as well.
-   Lastly, we will continue to use the accent, but you are free to change this to anything.

```js
// Variant specific colors (change these for variants)
"background": "color(var(blue) s(15%) l(5%))",
"selection": "color(var(background) s(15%) l(30%))",
"comment": "color(var(blue) s(25%) l(55%))",
"line-highlight": "color(var(background) s(25%) l(25%))",
"accent": "var(blue)",
```

Here we get something similar to Van Helsing, but with a classic palette.

![Dark](screenshots/Text%20-%20Dark.png)

We could just as easily change the colors and produce a Buffy like variant as well:

```js
// Variant specific colors (change these for variants)
"background": "color(var(pink) s(14%) l(15%))",
"selection": "color(var(background) s(15%) l(30%))",
"comment": "color(var(pink) s(25%) l(55%))",
"line-highlight": "color(var(background) s(25%) l(25%))",
"accent": "var(pink)",
```

![Pink](screenshots/Text%20-%20Pink.png)

Or also deduct our own Proish variant using color theory (indluded in this fork):

![Proish](screenshots/proish.png)

```js
// Static palette colors. These are constant through all variations.
"foreground": "hsl(60, 25%, 95%)",
"red": "hsl(12, 100%, 75%)",
"orange": "hsl(35, 100%, 75%)",
"yellow": "hsl(60, 100%, 75%)",
"green": "hsl(115, 100%, 75%)",
"cyan": "hsl(170, 100%, 75%)",
"blue": "hsl(225, 100%, 75%)",
"pink": "hsl(330, 100%, 75%)",
"purple": "hsl(250, 100%, 75%)",

// Variant specific colors (change these for variants)
"background": "hsl(245, 15%, 15%)",
"selection": "hsl(230, 15%, 30%)",
"comment": "color(var(blue) s(25%) l(50%))",
"line-highlight": "var(selection)",
"accent": "var(blue)",
```
