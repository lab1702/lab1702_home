# lab1702's Toolbox

A personal homepage presenting projects as a dark terminal-phosphor board of
color-accented cards, grouped into three directories.

## Overview

This is a single-page landing site that provides navigation to 16 games, data
projects and web tools. The page opens with a shell-prompt header and a
`lab1702` wordmark, then lays the projects out as a responsive grid of cards
grouped under `games/`, `data/` and `tools/` — each group carrying its own
accent hue so the three read apart at a glance.

## Features

- **Section Board**: Each directory is a responsive `auto-fit` card grid that
  collapses from two columns to one; every card shows the project name, a full
  description, and its tech stack as chips
- **Per-Section Accents**: Amber for `games/`, green for `data/`, cyan for
  `tools/` — set once per section as `--ac` and inherited by the cards
- **Terminal Header**: Shell prompt line (`~/lab1702 on main — tree`), a
  monospace wordmark with a blinking block cursor, and a scanline overlay
- **Hover/Focus States**: The card shifts to a lighter surface, its border takes
  the section accent, and the name changes to that accent
- **Responsive Design**: Fluid wordmark sizing with `clamp()` and a grid that
  reflows at any width — no content is hidden on small screens
- **Accessibility**: Skip-to-content link, `aria-label` on every card,
  `aria-labelledby` on each section, accent-colored `:focus-visible` rings, and
  a `prefers-reduced-motion` fallback
- **Zero Dependencies**: A single HTML file with inline CSS, no JavaScript and
  no build step

## Technical Details

- **Frontend**: Single-file vanilla HTML5 and CSS3 — the page runs no
  JavaScript at all
- **Color System**: CSS custom properties in oklch for the dark terminal
  palette (`--bg-0`/`--bg-1`/`--bg-2`, `--fg-1`/`--fg-2`/`--fg-3`, `--border-1`)
  plus three accent hues (`--amber`, `--green`, `--cyan`) exposed to each
  section as `--ac`
- **Typography**: JetBrains Mono for the wordmark, names, labels and chips;
  IBM Plex Sans for descriptions — both via Google Fonts
- **Effects**: Staggered fade-in on load, a blinking cursor, and a scanline
  gradient across the header
- **Accessibility**: `prefers-reduced-motion` disables the fade-in, the cursor
  blink and the card transitions

## Project Structure

```
lab1702_home/
├── index.html          # Main homepage (HTML and CSS inline, no JS)
├── README.md           # Project documentation
└── LICENSE             # MIT License
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Copyright

© 2025 lab1702. All rights reserved.
