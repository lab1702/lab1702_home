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
  reflows from three columns down to one; every card shows the project name, a
  full description, and its tech stack as chips
- **Self-Counting**: Each section's count badge and the footer's
  `N directories, N files` summary are CSS counters over the sections and
  cards, so adding or removing a card never means editing a number by hand
- **Per-Section Accents**: Amber for `games/`, green for `data/`, cyan for
  `tools/` — set once per section as `--ac` and inherited by the cards
- **Terminal Header**: A glass panel with a shell prompt line
  (`~/lab1702 on main — tree`), a monospace wordmark with a glowing white
  gradient and blinking block cursor, a four-color top hairline and a scanline
  overlay — the header has its own neutral white accent (`--hc`) so it stays
  distinct from the sections
- **Hover/Focus States**: The card lifts, its gradient border and corner glow
  light up in the section accent, an arrow slides in, and the name changes to
  that accent; pressing a card drops the lift and pulls its shadow in. On
  touch screens, which have no hover, the arrow is always shown
- **Responsive Design**: Fluid wordmark sizing with `clamp()` and a grid that
  reflows at any width — no content is hidden on small screens. Every font
  size is in `rem`, so the page follows the browser's font-size preference and
  (via `<meta name="text-scale">`, where supported) the OS text-size setting
- **Accessibility**: `<header>`, `<main>` and `<footer>` as page landmarks, a
  skip link that jumps past the header to the projects (pinned to the corner
  when focused, so the page doesn't shift), header links padded out to a
  44px-tall target on touch screens, each section's cards
  as a `<ul>` so screen readers announce the item count, cards and links named
  by their visible text (so voice control matches what's on screen), external
  links announced as opening in a new tab, accent-colored `:focus-visible`
  rings, and motion that is opt-in under `prefers-reduced-motion: no-preference`
- **Instant Navigation**: A speculation-rules block prefetches a project page
  once its card is hovered or pressed (Chromium; ignored elsewhere)
- **Sharing**: An inline SVG favicon and a 1200×630 `og-image.png` link
  preview, rendered by `scripts/make_og.py` from the same oklch tokens
- **Zero Dependencies**: One HTML file with inline CSS and two self-hosted
  font files — no third-party requests, no JavaScript and no build step

## Technical Details

- **Frontend**: Single-file vanilla HTML5 and CSS3 — the page runs no
  JavaScript at all
- **Color System**: CSS custom properties in oklch for the dark terminal
  palette (`--bg-0`/`--bg-1`/`--bg-2`, `--fg-1`/`--fg-2`/`--fg-3`, `--border-1`)
  plus three section accent hues (`--amber`, `--green`, `--cyan`) exposed to
  each section as `--ac`, and a neutral white header accent (`--hc`,
  `--hc-hot`, `--hc-light`) whose bare oklch channels live in `--hc-lch` so the
  header can derive alpha variants with `oklch(var(--hc-lch) / a)`
- **Typography**: JetBrains Mono for the wordmark, names, labels and chips;
  IBM Plex Sans for descriptions — both self-hosted as latin-subset woff2
  files in `fonts/` (SIL Open Font License), with the mono face preloaded.
  Descriptions set `font-size-adjust` to Plex's x-height ratio so the system
  fallback matches its visual size until the font swaps in
- **Effects**: Ambient accent-colored background glows over a faint dot grid
  (the amber one rides along with `games/`),
  staggered fade-in on load, a cursor that blinks four times and then stays
  solid, a status dot that pulses twice, and a scanline gradient across the
  header — nothing keeps moving past five seconds
- **Accessibility**: The fade-in, the cursor blink, the status pulse, the card
  lift and press, and the arrow slide only run under
  `prefers-reduced-motion: no-preference`; colour, glow and opacity
  transitions always run

## Project Structure

```
lab1702_home/
├── index.html          # Main homepage (HTML and CSS inline, no JS)
├── fonts/              # Self-hosted woff2 fonts and their OFL licences
├── og-image.png        # Social link preview (1200×630)
├── scripts/
│   └── make_og.py      # Regenerates og-image.png (Pillow + JetBrains Mono)
├── README.md           # Project documentation
└── LICENSE             # MIT License
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Copyright

© 2025–2026 lab1702. All rights reserved.
