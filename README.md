# lab1702's Toolbox

A personal homepage presenting projects as a dark terminal-phosphor board of
color-accented cards, grouped into three directories.

## Overview

This is a single-page landing site that provides navigation to games, data
projects and web tools. The page opens with a shell-prompt header and a
`lab1702` wordmark, then lays the projects out as a responsive grid of cards
grouped under `games/`, `data/` and `tools/` — each group carrying its own
accent hue so the three read apart at a glance.

## Features

- **Section Board**: Each directory is a responsive `auto-fit` card grid that
  collapses from two columns to one; every card shows the project name, a full
  description, and its tech stack as chips, and each section's count badge is
  a CSS counter over its cards, so it never needs editing by hand
- **Per-Section Accents**: Amber for `games/`, green for `data/`, cyan for
  `tools/` — set once per section as `--ac` and inherited by the cards
- **Terminal Header**: A glass panel with a shell prompt line
  (`~/lab1702 on main — tree`), a monospace wordmark with a glowing coral
  gradient and blinking block cursor, a four-color top hairline and a scanline
  overlay — the header has its own coral accent (`--hc`) so it stays distinct
  from the sections
- **Hover/Focus States**: The card lifts, its gradient border and corner glow
  light up in the section accent, an arrow slides in, and the name changes to
  that accent
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
  plus three section accent hues (`--amber`, `--green`, `--cyan`) exposed to
  each section as `--ac`, and a coral header accent (`--hc`, `--hc-hot`,
  `--hc-light`) whose bare oklch channels live in `--hc-lch` so the header can
  derive alpha variants with `oklch(var(--hc-lch) / a)`
- **Typography**: JetBrains Mono for the wordmark, names, labels and chips;
  IBM Plex Sans for descriptions — both via Google Fonts
- **Effects**: Ambient accent-colored background glows over a faint dot grid
  (the amber one rides along with `games/`),
  staggered fade-in on load, a blinking cursor, a pulsing status dot, and a
  scanline gradient across the header
- **Accessibility**: `prefers-reduced-motion` disables the fade-in, the cursor
  blink, the status pulse, and the card transitions and lift

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
