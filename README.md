# lab1702's Toolbox

A personal homepage presenting projects as a calm, typographic menu in a warm dark palette.

## Overview

This is a single-page landing site that provides navigation to different games and web applications. The page is laid out as a contents-page "menu" — each project is a row with a serif name, a dotted leader, and its tech tags — set in a "Warm Charcoal" palette with a single terracotta accent.

## Applications

### Games
- **NETREK-WEB** (`/netrek`) - Space combat multiplayer game
- **Project Gorgon Navigator** (`/gorgon-maps`) - MMO map tool
- **Word Garden** (`/word`) - Scrabble-like word game

### Tools
- **Detroit Crime Incidents** (`/detcrime`) - Crime data visualization for Detroit (Python/Streamlit)
- **Tire Size Calculator** (`/tiresize`) - Automotive tire size comparison utility

## Features

- **Warm Menu Aesthetic**: "Warm Charcoal" dark palette with a terracotta accent and a faint radial glow; no cards or chrome
- **Typographic Layout**: Projects as menu rows — serif names, dotted leaders, monospace tech tags — in a narrow centered column
- **Hover/Focus States**: Row name warms to terracotta, an arrow slides in, and the leader and tech tags brighten
- **Responsive Design**: Fluid typography and a single-column layout adapting to all screen sizes
- **Accessibility**: `prefers-reduced-motion` support, ARIA labels, skip-to-content link, keyboard navigation with `focus-visible` styles
- **Zero Dependencies**: Vanilla HTML, CSS, and JavaScript with no build step

## Technical Details

- **Frontend**: Single-file vanilla HTML5, CSS3, and JavaScript
- **Color System**: CSS custom properties for the Warm Charcoal palette (`--bg`, `--text`, `--bright`, `--muted`, `--accent`)
- **Typography**: Fraunces (serif names) and JetBrains Mono (labels/tech) via Google Fonts, fluid sizing with `clamp()`
- **Effects**: Subtle radial glow and a gentle staggered fade-in on load
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
