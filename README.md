# lab1702's Toolbox

A personal homepage presenting projects as a bold, vivid-on-dark grid of color-block tiles.

## Overview

This is a single-page landing site that provides navigation to different games and web applications. The page is laid out as a graphic grid — each project is a color-block tile with a bold name, its tech tags, and its own vivid accent color — set on a deep dark canvas.

## Features

- **Color-Block Grid**: Responsive grid of project tiles, each with its own hand-picked accent color (terracotta, blue, green, violet, gold)
- **Bold Typography**: Oversized Space Grotesk display type for the wordmark and tile names, with JetBrains Mono for tech tags and section labels
- **Hover/Focus States**: Tile lifts, its accent border and glow intensify, the name shifts to the accent color, and an arrow slides in
- **Responsive Design**: Fluid typography and an `auto-fit` grid collapsing from three columns to one across screen sizes
- **Accessibility**: `prefers-reduced-motion` support, ARIA labels, skip-to-content link, keyboard navigation with `focus-visible` styles
- **Zero Dependencies**: Vanilla HTML, CSS, and JavaScript with no build step

## Technical Details

- **Frontend**: Single-file vanilla HTML5, CSS3, and JavaScript
- **Color System**: CSS custom properties for the dark base (`--bg`, `--surface`, `--surface-2`, `--text`, `--bright`, `--muted`, `--border`) plus a per-tile `--ac` accent variable set by `.ac-*` modifier classes
- **Typography**: Space Grotesk (wordmark and tile names) and JetBrains Mono (labels/tech) via Google Fonts, fluid sizing with `clamp()`
- **Effects**: Staggered fade-in on load and an accent-colored hover glow (using `color-mix()`)
- **Accessibility**: `prefers-reduced-motion` disables the fade-in and hover transitions

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
