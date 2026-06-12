# Homepage Redesign — "Warm Menu" Design

**Date:** 2026-06-11
**Status:** Approved (design)
**File touched:** `index.html` (single-file static page, GitHub Pages)

## Goal

Replace the amber CRT-terminal aesthetic with a fresh direction: a calm, typographic
**"menu"** of projects — a contents-page list rather than a grid of cards. The look should
feel distinctly personal without being fussy. Personality comes from typography and a warm
palette, not from chrome, decoration, or layout gimmicks.

This is a presentation-only change. All existing projects, links, and meta tags carry over
unchanged; no projects are added, removed, reordered, or recategorized.

## Non-goals

- No build step, framework, or dependencies — stays a single hand-written `index.html`.
- No search, filtering, tabs, carousels, or other interactive layout machinery.
- No per-project screenshots/thumbnails.
- No content/copy changes beyond removing the tagline (see below).

## Concept

Each project is a single row, like a line in a restaurant menu or a book's table of
contents: **serif project name · dotted leader · monospace tech tags**. No cards, no
borders, no boxes. The page is a narrow centered column that breathes on wide monitors.

## Palette — "Warm Charcoal"

Defined as CSS custom properties on `:root`:

| Token          | Value     | Use                                         |
|----------------|-----------|---------------------------------------------|
| `--bg`         | `#1a1714` | Page background (near-black warm brown)     |
| `--text`       | `#e9dcc6` | Default text (cream)                        |
| `--bright`     | `#f4ead6` | Name + project titles                       |
| `--muted`      | `#9b8d77` | Section labels, secondary text              |
| `--faint`      | `#7d7264` | GitHub link (resting)                       |
| `--leader`     | `#3a332c` | Dotted leader (resting)                      |
| `--leader-hot` | `#5a4636` | Dotted leader (hover)                        |
| `--accent`     | `#c98a5e` | Terracotta — tech tags (resting)            |
| `--accent-hot` | `#ef9a5c` | Terracotta — hover state (name, arrow, tech)|

A faint terracotta radial glow sits at the top of the page:
`radial-gradient(55% 38% at 50% -6%, rgba(201,123,84,.10), transparent 70%)`.

`<meta name="theme-color">` updates from `#0a0a0a` to `#1a1714`.

## Typography

Two web fonts loaded from Google Fonts (replacing Fira Code):

- **Fraunces** (`opsz` 9..144, weights 400/600/700) — the name and project titles. Serif
  with warmth and optical character; carries the personality. Fallback: `Georgia, serif`.
- **JetBrains Mono** (weights 400/500) — section labels, tech tags, and the GitHub link.
  The serif/mono pairing is the design's signature. Fallback: `monospace`.

`-webkit-font-smoothing: antialiased` on `html`.

## Layout

- `main`: `max-width: 560px`, centered (`margin: 0 auto`), content **left-aligned**.
- Body padding: `clamp(2.5rem, 8vh, 6rem) 1.5rem 4rem`.
- **Hero** (`margin-bottom: 3.5rem`):
  - `h1` "lab1702" — Fraunces 700, `clamp(2.4rem, 7vw, 3.1rem)`, `--bright`,
    `letter-spacing: -.02em`, `line-height: 1`.
  - GitHub link "github.com/lab1702 ↗" — JetBrains Mono `.72rem`, `--faint`, hover `--accent`.
    Real `href="https://github.com/lab1702"` with `target="_blank" rel="noopener noreferrer"`.
  - **No tagline** (the "games & tools" / "a workshop of…" line is removed).
- **Two sections** — `games`, then `tools` (`margin-bottom: 2.75rem` each):
  - Section label: JetBrains Mono `.68rem`, uppercase, `letter-spacing: .24em`, `--muted`.
  - **Rows** (`<a class="row">`, `display:flex; align-items:baseline; gap:.7rem; padding:.6rem 0`):
    - `.name` — Fraunces 600, `1.32rem`, `--bright`, `white-space:nowrap`.
    - `.arrow` — "→", `--accent-hot`, hidden by default (`opacity:0`, nudged left).
    - `.leader` — `flex:1`, `border-bottom: 2px dotted var(--leader)`, nudged up to sit on
      the baseline.
    - `.tech` — JetBrains Mono `.72rem`, `--accent`, `white-space:nowrap`. Tags are
      lowercased and joined with " · " (e.g. `go · js`, `python · streamlit`).

## Interaction

- **Hover / focus** on a row: name → `--accent-hot`, arrow fades/slides in, leader →
  `--leader-hot`, tech → `--accent-hot`. Transitions ~`.18s ease`.
- Rows are real `<a>` links (keyboard focusable). `:focus-visible` shows a
  `2px solid var(--accent)` outline with offset.
- Respect `prefers-reduced-motion: reduce` — disable any on-load fade and transitions.
- Optional: keep the existing subtle staggered fade-in on load for hero/sections/rows,
  gated behind `prefers-reduced-motion`. (Carryover from current page; nice-to-have.)

## Content (carried over verbatim, lowercased tech tags)

**games**
- Netrek Web — `/netrek` — `go · js`
- Word Garden — `/word` — `js`
- Project Gorgon Nav — `/gorgon-maps` — `js`

**tools** (order preserved from current `index.html`)
- Detroit Crime — `/detcrime` — `python · streamlit`
- Tire Size Calc — `/tiresize` — `js`
- Chat — `/chat` — `js`
- Cruise Calendar — `/ccalendar.html` — `html`
- Crime & Weather — `/detroit-crime-weather` — `python · pandas`
- Ichimoku Trading — `/trading` — `r · shiny`

All 9 projects currently in `index.html` (3 games + 6 tools) carry over with their existing
hrefs and `aria-label`s. None are added, removed, or reordered.

## Accessibility & meta (preserved)

- Skip-to-content link, `lang="en"`, semantic `<header>` / `<nav>` / sections.
- Each row keeps a descriptive `aria-label` (project name + short description).
- All existing `<meta>` description, Open Graph, and Twitter card tags are preserved;
  only `theme-color` changes.
- Targets ≥44px touch target height on rows.

## Verification

- Open the page at desktop width — column centered ~560px, leaders short, ample side margin.
- Resize narrow (mobile) — column fills with `1.5rem` side padding, no horizontal scroll.
- Tab through rows — visible focus ring, correct order, links resolve to the paths above.
- Toggle reduced-motion — no animation, hover still changes color.
- Confirm fonts load (Fraunces + JetBrains Mono) with graceful serif/mono fallback.
