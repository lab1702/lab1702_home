# Homepage Redesign — "Color-Block Grid" (Bold & Graphic, Vivid-on-Dark)

**Date:** 2026-06-21
**Status:** Approved (design)

## Goal

Redesign the personal homepage to be more flashy. The current "warm menu" is a
calm, typographic contents-page list. This redesign keeps the same content but
reshapes it into a **bold, graphic, poster-like grid** of vivid color-block
project tiles on a dark canvas.

## Direction (decided)

- **Vibe:** Bold & graphic — flashy through visual boldness (big type, strong
  shapes, vivid color blocks), not through heavy motion or effects.
- **Palette:** Vivid on dark. Deep dark base evolved from the heritage warm
  charcoal, with a small set of saturated accent hues applied per tile.
- **Layout:** Responsive color-block grid. Each project is a tile with its own
  fixed, hand-picked accent color.
- **Typography:** Switch to a bold geometric sans (**Space Grotesk**) for the
  hero wordmark and all tile names. Keep **JetBrains Mono** for tech tags and
  section labels. **Fraunces is dropped entirely.**

## Constraints (unchanged from current site)

- Single `index.html` — inline CSS and JS, **no build step**, zero dependencies
  beyond Google Fonts.
- Keep all accessibility: skip-to-content link, `aria-label`s on links,
  `:focus-visible` outlines, and a `prefers-reduced-motion` fallback.
- Same 10 projects, same hrefs, same two sections ("games", "tools"),
  alphabetical order preserved within each section.

## Palette

Base (evolved warm charcoal, dark):

| Token        | Value      | Use                                  |
|--------------|------------|--------------------------------------|
| `--bg`       | `#16130f`  | Page background (slightly deeper)    |
| `--surface`  | `#211c16`  | Tile background (resting)            |
| `--text`     | `#e9dcc6`  | Body / tag text                      |
| `--bright`   | `#f7efe0`  | Names, high-contrast text            |
| `--muted`    | `#9b8d77`  | Section labels, github link          |

Per-tile accent palette (5 hues, hand-picked, vivid on dark):

| Name       | Value      |
|------------|------------|
| terracotta | `#ef9a5c`  |
| blue       | `#5ab0ef`  |
| green      | `#9fd356`  |
| violet     | `#c77dff`  |
| gold       | `#f4c430`  |

Each tile exposes its accent via a CSS custom property (`--ac`) set inline or via
a modifier class, so the tile styles (border, glow, hover name color, tag color)
reference one variable.

### Fixed accent assignment

**games**
- Netrek Web → blue
- Project Gorgon Nav → violet
- Word Garden → green

**tools**
- Chat → blue
- Crime & Weather → gold
- Cruise Calendar → terracotta
- Detroit Crime → violet
- Ichimoku Trading → gold
- Tire Size Calc → green
- US Presidents Pivot Viewer → terracotta

(Assignments are a starting point and may be nudged during implementation for
visual balance across the grid; the count of distinct hues stays at 5.)

## Layout & Components

### Hero
- `lab1702` wordmark in Space Grotesk heavy weight, large scale (bigger than
  the current hero).
- `github.com/lab1702 ↗` link beneath in JetBrains Mono, muted, hover → accent.

### Sections
- Two sections: "games" and "tools".
- Section heading: JetBrains Mono, uppercase, wide letter-spacing, muted —
  carried over in spirit from the current `.section-label`.
- Each section heads its own grid.

### Grid
- CSS Grid with `repeat(auto-fit, minmax(<min>, 1fr))`.
- Target: ~3 columns desktop, 2 columns tablet, 1 column mobile (driven by the
  `minmax` min and the centered container max-width — container widens from the
  current 560px to accommodate the grid, e.g. ~860–960px).
- Gap between tiles consistent with the bold spacing.

### Tile (the link)
- Whole tile is an `<a>` (keeps single-click target + `aria-label`).
- Contents:
  - Project name — Space Grotesk, bold, large.
  - Tech tags — JetBrains Mono, small, in the tile's accent color.
  - An arrow `→` that appears on hover/focus.
- Resting state: `--surface` background, a subtle accent-tinted border, soft
  rounded corners.
- Hover/focus state: accent intensifies — border glows (accent box-shadow),
  name brightens toward `--bright`/accent, tile lifts slightly
  (`translateY(-3px)`), arrow slides in. Transition quick (~180ms).

## Behavior

- **On-load animation:** staggered fade/scale-in of tiles (cascade), reusing the
  existing JS pattern that adds a class with a per-element delay.
- **Reduced motion:** `prefers-reduced-motion: reduce` disables the load
  animation and hover transforms/transitions (tiles render fully visible and
  static), matching the current implementation's guarantees.

## Accessibility

- Skip-to-content link (retained).
- Each tile `<a>` keeps a descriptive `aria-label`; decorative arrow is
  `aria-hidden`.
- `:focus-visible` outline on tiles and the github link.
- Color is never the sole carrier of meaning — names and tags are always legible
  against the surface regardless of accent.
- Contrast: accent hues chosen to meet legible contrast for tag text on the dark
  surface; names use `--bright`/`--text`, not accent, in the resting state.

## Out of Scope

- No motion-heavy backgrounds, particles, or WebGL.
- No changes to project content, links, or the set of projects.
- No build tooling, frameworks, or external JS libraries.

## Files Touched

- `index.html` — full rewrite of the `<style>` block, hero, and project grid
  markup; updated font `<link>` (Space Grotesk + JetBrains Mono, drop Fraunces).
- `README.md` — update the aesthetic description to match the new design.
