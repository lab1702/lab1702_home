# lab1702's Toolbox

A personal homepage styled as a retro CRT terminal with amber phosphor aesthetics.

## Overview

This is a single-page landing site that provides navigation to different games and web applications. The page features a CRT terminal design with scanlines, vignette, flicker effects, and a typed boot sequence animation.

## Applications

### Games
- **NETREK-WEB** (`/netrek`) - Space combat multiplayer game
- **Project Gorgon Navigator** (`/gorgon-maps`) - MMO map tool
- **Word Garden** (`/word`) - Scrabble-like word game

### Tools
- **Detroit Crime Incidents** (`/detcrime`) - Crime data visualization for Detroit (Python/Streamlit)
- **Tire Size Calculator** (`/tiresize`) - Automotive tire size comparison utility

## Features

- **CRT Terminal Aesthetic**: Amber phosphor color palette, scanline overlay, screen vignette, and subtle flicker animation
- **Boot Sequence**: Typed login animation with skip support (click or keypress)
- **Responsive Design**: Fluid typography and layouts adapting to all screen sizes
- **Accessibility**: `prefers-reduced-motion` support, ARIA labels, skip-to-content link, keyboard navigation with `focus-visible` styles
- **Zero Dependencies**: Vanilla HTML, CSS, and JavaScript with no build step

## Technical Details

- **Frontend**: Single-file vanilla HTML5, CSS3, and JavaScript
- **Color System**: CSS custom properties for amber phosphor palette (`--text`, `--text-dim`, `--text-bright`)
- **Typography**: JetBrains Mono via Google Fonts, fluid sizing with `clamp()`
- **Effects**: Pure CSS scanlines, vignette, and flicker; JavaScript typed boot sequence
- **Accessibility**: `prefers-reduced-motion` disables all effects and skips boot animation

## Project Structure

```
lab1702_home/
├── index.html          # Main homepage (HTML, CSS, and JS inline)
├── docs/
│   └── plans/          # Design and implementation documents
├── README.md           # Project documentation
└── LICENSE             # MIT License
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Copyright

© 2025 lab1702. All rights reserved.
