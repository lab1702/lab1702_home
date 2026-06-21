# Homepage Color-Block Grid Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild `index.html` as a bold, vivid-on-dark color-block grid of project tiles, replacing the calm typographic "warm menu."

**Architecture:** Single-file static page. All CSS and JS stay inline in `index.html`. The page is a hero wordmark plus two sections ("games", "tools"), each rendering a responsive CSS Grid of accent-colored tiles. Each tile is an `<a>` whose accent color is set by a modifier class exposing a `--ac` custom property consumed by the shared tile styles.

**Tech Stack:** Vanilla HTML5, CSS3 (CSS Grid, custom properties, `color-mix()`), vanilla JS. Google Fonts: Space Grotesk + JetBrains Mono. No build step, no dependencies.

## Global Constraints

- Single `index.html`; all CSS/JS inline; **no build step**; no JS libraries or frameworks.
- Fonts: **Space Grotesk** (hero + tile names) and **JetBrains Mono** (tags, section labels, github link). **Fraunces is removed.**
- Same 10 projects, same hrefs, same two sections, alphabetical order within each section.
- Accessibility preserved: skip-to-content link, descriptive `aria-label` per tile link, decorative arrow `aria-hidden`, `:focus-visible` outlines, `prefers-reduced-motion` fallback that disables load animation + hover transforms.
- Palette tokens (exact): `--bg:#16130f`, `--surface:#211c16`, `--surface-2:#2a241c`, `--text:#e9dcc6`, `--bright:#f7efe0`, `--muted:#9b8d77`, `--border:#3a332c`.
- Accent hues (exact): terracotta `#ef9a5c`, blue `#5ab0ef`, green `#9fd356`, violet `#c77dff`, gold `#f4c430`.
- Fixed accent assignment — games: Netrek=blue, Gorgon=violet, Word Garden=green. tools: Chat=blue, Crime & Weather=gold, Cruise Calendar=terracotta, Detroit Crime=violet, Ichimoku Trading=gold, Tire Size Calc=green, US Presidents Pivot Viewer=terracotta.
- Verification is **visual in a browser** (no unit-test harness exists for this static page). "Run" steps mean: open `index.html` and confirm the described rendering.

---

### Task 1: New scaffold — head, palette, base styles, and hero

Replace the document head (fonts + full `<style>`) and the hero markup. After this task the page shows the new bold hero on the dark background; the body below it will be empty until Task 2.

**Files:**
- Modify: `index.html` (lines 16, 17–199 `<style>`, 205–208 hero markup)

**Interfaces:**
- Produces: CSS custom properties `--bg --surface --surface-2 --text --bright --muted --border`; accent classes `.ac-terracotta .ac-blue .ac-green .ac-violet .ac-gold` each setting `--ac`; classes `.sr-only .hero .hero-name .hero-github`; the `.fade-target` opacity-0 hook (animation added in Task 3).

- [ ] **Step 1: Swap the Google Fonts link**

Replace line 16:

```html
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap">
```

- [ ] **Step 2: Replace the entire `<style>` block**

Replace everything from `<style>` to `</style>` (lines 17–199) with:

```html
    <style>
        :root {
            --bg: #16130f;
            --surface: #211c16;
            --surface-2: #2a241c;
            --text: #e9dcc6;
            --bright: #f7efe0;
            --muted: #9b8d77;
            --border: #3a332c;
        }

        .ac-terracotta { --ac: #ef9a5c; }
        .ac-blue       { --ac: #5ab0ef; }
        .ac-green      { --ac: #9fd356; }
        .ac-violet     { --ac: #c77dff; }
        .ac-gold       { --ac: #f4c430; }

        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html { -webkit-font-smoothing: antialiased; }

        body {
            font-family: 'Space Grotesk', system-ui, -apple-system, sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            overflow-x: hidden;
            padding: clamp(2.5rem, 8vh, 6rem) 1.5rem 4rem;
        }

        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }

        .sr-only:focus {
            position: static;
            width: auto;
            height: auto;
            clip: auto;
            overflow: visible;
            margin: 0;
            padding: 0.5rem 1rem;
            display: block;
            background: var(--bg);
            color: var(--bright);
            white-space: normal;
            z-index: 10000;
        }

        main {
            max-width: 960px;
            margin: 0 auto;
        }

        /* Hero */
        .hero { margin-bottom: clamp(2.5rem, 6vh, 4rem); }

        .hero-name {
            font-size: clamp(3rem, 12vw, 6rem);
            font-weight: 700;
            color: var(--bright);
            letter-spacing: -0.04em;
            line-height: 0.95;
        }

        .hero-github {
            display: inline-block;
            margin-top: 1rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            letter-spacing: 0.04em;
            color: var(--muted);
            text-decoration: none;
            transition: color 200ms ease;
        }

        .hero-github:hover { color: var(--bright); }

        .hero-github:focus-visible {
            color: var(--bright);
            outline: 2px solid var(--muted);
            outline-offset: 4px;
            border-radius: 2px;
        }

        /* Sections */
        .project-section { margin-bottom: clamp(2.5rem, 5vh, 3.5rem); }

        .section-label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            font-weight: 400;
            text-transform: uppercase;
            letter-spacing: 0.28em;
            color: var(--muted);
            margin-bottom: 1rem;
        }

        /* Grid */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1rem;
        }

        /* Tiles */
        .tile {
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 1.5rem;
            min-height: 150px;
            padding: 1.4rem 1.5rem;
            background: var(--surface);
            border: 1px solid color-mix(in srgb, var(--ac) 35%, transparent);
            border-radius: 14px;
            text-decoration: none;
            color: inherit;
            overflow: hidden;
            transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease, background 180ms ease;
        }

        .tile-name {
            font-size: clamp(1.4rem, 2.5vw, 1.75rem);
            font-weight: 700;
            letter-spacing: -0.02em;
            line-height: 1.05;
            color: var(--bright);
            transition: color 180ms ease;
        }

        .tile-meta {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.5rem;
        }

        .tile-tech {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            color: var(--ac);
            transition: color 180ms ease;
        }

        .tile-arrow {
            font-size: 1.1rem;
            line-height: 1;
            color: var(--ac);
            opacity: 0;
            transform: translateX(-6px);
            transition: opacity 180ms ease, transform 180ms ease;
        }

        .tile:hover,
        .tile:focus-visible {
            transform: translateY(-3px);
            background: var(--surface-2);
            border-color: var(--ac);
            box-shadow: 0 0 0 1px color-mix(in srgb, var(--ac) 50%, transparent),
                        0 12px 30px -12px color-mix(in srgb, var(--ac) 60%, transparent);
        }

        .tile:hover .tile-name,
        .tile:focus-visible .tile-name { color: var(--ac); }

        .tile:hover .tile-arrow,
        .tile:focus-visible .tile-arrow { opacity: 1; transform: translateX(0); }

        .tile:focus-visible {
            outline: 2px solid var(--ac);
            outline-offset: 3px;
        }

        /* On-load fade (gated by reduced-motion in Task 3) */
        @keyframes fade-in-up {
            from { opacity: 0; transform: translateY(14px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .fade-target { opacity: 0; }
        .fade-in { animation: fade-in-up 450ms ease forwards; }

        @media (prefers-reduced-motion: reduce) {
            .fade-target { opacity: 1; }
            .fade-in { animation: none; opacity: 1; }
            .tile, .tile-name, .tile-arrow, .tile-tech, .hero-github { transition: none; }
            .tile:hover, .tile:focus-visible { transform: none; }
        }
    </style>
```

- [ ] **Step 3: Confirm the hero markup matches the new classes**

The existing hero (lines 205–208) already uses `.hero`, `.hero-name`, `.hero-github`, `.fade-target` — leave its structure as-is. Verify it reads:

```html
    <header class="hero fade-target">
        <h1 class="hero-name">lab1702</h1>
        <a href="https://github.com/lab1702" target="_blank" rel="noopener noreferrer" class="hero-github" aria-label="lab1702 on GitHub">github.com/lab1702 ↗</a>
    </header>
```

- [ ] **Step 4: Visual check**

Run: open `index.html` in a browser.
Expected: deep dark background; large bold "lab1702" wordmark in Space Grotesk; mono github link beneath in muted color that brightens on hover. Project rows below are unstyled/gone for now (replaced in Task 2) — that's fine.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: new bold palette, fonts, and hero for color-block redesign"
```

---

### Task 2: Project grid and tiles

Replace the `<nav>` body (the old menu rows) with two `.grid` blocks of accent-colored tiles for all 10 projects.

**Files:**
- Modify: `index.html` (the `<nav aria-label="Projects">` block, old lines 210–280)

**Interfaces:**
- Consumes: `.grid`, `.tile`, `.ac-*`, `.tile-name`, `.tile-meta`, `.tile-tech`, `.tile-arrow`, `.section-label`, `.fade-target` from Task 1.

- [ ] **Step 1: Replace the `<nav>` block**

Replace the entire `<nav aria-label="Projects"> … </nav>` element with:

```html
    <nav aria-label="Projects">
        <section class="project-section">
            <h2 class="section-label fade-target">games</h2>
            <div class="grid">
                <a href="/netrek" class="tile ac-blue fade-target" aria-label="Netrek Web — space combat multiplayer game built with Go and JavaScript">
                    <span class="tile-name">Netrek Web</span>
                    <span class="tile-meta">
                        <span class="tile-tech">go · js</span>
                        <span class="tile-arrow" aria-hidden="true">→</span>
                    </span>
                </a>
                <a href="/gorgon-maps" class="tile ac-violet fade-target" aria-label="Project Gorgon Nav — MMO map tool">
                    <span class="tile-name">Project Gorgon Nav</span>
                    <span class="tile-meta">
                        <span class="tile-tech">js</span>
                        <span class="tile-arrow" aria-hidden="true">→</span>
                    </span>
                </a>
                <a href="/word" class="tile ac-green fade-target" aria-label="Word Garden — word game">
                    <span class="tile-name">Word Garden</span>
                    <span class="tile-meta">
                        <span class="tile-tech">js</span>
                        <span class="tile-arrow" aria-hidden="true">→</span>
                    </span>
                </a>
            </div>
        </section>

        <section class="project-section">
            <h2 class="section-label fade-target">tools</h2>
            <div class="grid">
                <a href="/chat" class="tile ac-blue fade-target" aria-label="Chat — chat application">
                    <span class="tile-name">Chat</span>
                    <span class="tile-meta">
                        <span class="tile-tech">js</span>
                        <span class="tile-arrow" aria-hidden="true">→</span>
                    </span>
                </a>
                <a href="/detroit-crime-weather" class="tile ac-gold fade-target" aria-label="Crime &amp; Weather — analysis of weather impact on Detroit crime">
                    <span class="tile-name">Crime &amp; Weather</span>
                    <span class="tile-meta">
                        <span class="tile-tech">python · pandas</span>
                        <span class="tile-arrow" aria-hidden="true">→</span>
                    </span>
                </a>
                <a href="/ccalendar.html" class="tile ac-terracotta fade-target" aria-label="Cruise Calendar — South East Michigan car cruises and events">
                    <span class="tile-name">Cruise Calendar</span>
                    <span class="tile-meta">
                        <span class="tile-tech">html</span>
                        <span class="tile-arrow" aria-hidden="true">→</span>
                    </span>
                </a>
                <a href="/detcrime" class="tile ac-violet fade-target" aria-label="Detroit Crime — crime data visualization built with Python and Streamlit">
                    <span class="tile-name">Detroit Crime</span>
                    <span class="tile-meta">
                        <span class="tile-tech">python · streamlit</span>
                        <span class="tile-arrow" aria-hidden="true">→</span>
                    </span>
                </a>
                <a href="/trading" class="tile ac-gold fade-target" aria-label="Ichimoku Trading — trading strategy app using the R ichimoku package">
                    <span class="tile-name">Ichimoku Trading</span>
                    <span class="tile-meta">
                        <span class="tile-tech">r · shiny</span>
                        <span class="tile-arrow" aria-hidden="true">→</span>
                    </span>
                </a>
                <a href="/tiresize" class="tile ac-green fade-target" aria-label="Tire Size Calc — tire comparison tool">
                    <span class="tile-name">Tire Size Calc</span>
                    <span class="tile-meta">
                        <span class="tile-tech">js</span>
                        <span class="tile-arrow" aria-hidden="true">→</span>
                    </span>
                </a>
                <a href="/presidents.html" class="tile ac-terracotta fade-target" aria-label="US Presidents Pivot Viewer — pivot table viewer for US presidents data">
                    <span class="tile-name">US Presidents Pivot Viewer</span>
                    <span class="tile-meta">
                        <span class="tile-tech">html · python</span>
                        <span class="tile-arrow" aria-hidden="true">→</span>
                    </span>
                </a>
            </div>
        </section>
    </nav>
```

- [ ] **Step 2: Visual check — grid**

Run: open `index.html`.
Expected: "games" label over a row of 3 tiles; "tools" label over a grid of 7 tiles wrapping ~3 per row on a wide window. Each tile shows a bold name and a mono tech tag in its accent color, with an accent-tinted border.

- [ ] **Step 3: Visual check — hover/focus**

Run: hover a tile, then Tab to it with the keyboard.
Expected: tile lifts slightly, border + glow intensify in the accent color, name turns the accent color, and the `→` arrow slides in. Keyboard focus shows the same plus a focus outline.

- [ ] **Step 4: Visual check — responsive + links**

Run: narrow the window to phone width; click a tile.
Expected: tiles collapse to a single column at narrow widths and 2-up at mid widths; clicking a tile navigates to its href (e.g. `/netrek`).

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: render projects as vivid color-block grid"
```

---

### Task 3: Load animation and reduced-motion / accessibility verification

The CSS (Task 1) already defines the fade animation and the reduced-motion fallback. This task ensures the JS still cascades the new tiles and verifies the accessibility guarantees end to end.

**Files:**
- Modify: `index.html` (the `<script>` block, old lines 282–292) — only if changes are needed.

**Interfaces:**
- Consumes: `.fade-target` elements (hero, section labels, tiles) and the `.fade-in` class from Task 1.

- [ ] **Step 1: Confirm the load script targets `.fade-target`**

The existing script already selects `.fade-target` and adds `.fade-in` with a staggered delay; since hero, labels, and all tiles carry `.fade-target`, no change is required. Verify it reads:

```html
<script>
(function () {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var targets = document.querySelectorAll('.fade-target');
    targets.forEach(function (el, i) {
        setTimeout(function () {
            el.classList.add('fade-in');
        }, i * 50);
    });
})();
</script>
```

- [ ] **Step 2: Visual check — load cascade**

Run: reload `index.html`.
Expected: hero, then section labels and tiles fade/rise in with a brief stagger.

- [ ] **Step 3: Visual check — reduced motion**

Run: enable OS "reduce motion" (or DevTools → Rendering → Emulate CSS `prefers-reduced-motion: reduce`) and reload.
Expected: everything is immediately visible with no fade and no hover lift/transition; tiles still change color on hover/focus (acceptable — only motion is suppressed).

- [ ] **Step 4: Visual check — keyboard + skip link**

Run: press Tab from page load.
Expected: first Tab reveals the "Skip to main content" link; subsequent Tabs move through the github link and each tile with a visible focus outline in the tile's accent color.

- [ ] **Step 5: Commit (only if the script changed)**

If Step 1 required no edit, skip this commit. Otherwise:

```bash
git add index.html
git commit -m "feat: cascade load animation across grid tiles"
```

---

### Task 4: Update README

Bring the README's aesthetic description in line with the new design.

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Rewrite the Overview, Features, and Technical Details**

Replace the description of the "warm menu / contents-page" aesthetic with the color-block grid. Specifically:

- **Overview:** describe a single-page landing site presenting projects as a bold, vivid-on-dark grid of color-block tiles, each project a tile with its own accent color.
- **Features:** replace the menu/dotted-leader bullets with: "Color-Block Grid" (responsive grid of accent-colored tiles), "Bold Typography" (Space Grotesk display + JetBrains Mono tags), hover/focus states (accent glow, lift, arrow), responsive design, accessibility (reduced-motion, ARIA, skip link, focus-visible), zero dependencies.
- **Technical Details → Color System:** list the base tokens (`--bg`, `--surface`, `--surface-2`, `--text`, `--bright`, `--muted`, `--border`) plus the per-tile `--ac` accent variable.
- **Technical Details → Typography:** Space Grotesk (hero + tile names) and JetBrains Mono (labels/tags) via Google Fonts; remove Fraunces.
- **Technical Details → Effects:** staggered fade-in on load and accent hover glow; `prefers-reduced-motion` disables motion.

Leave Project Structure, License, and Copyright sections unchanged.

- [ ] **Step 2: Verify no stale references**

Run: `grep -in "fraunces\|warm charcoal\|terracotta accent\|dotted leader\|menu row" README.md`
Expected: no matches (all Fraunces / warm-menu wording removed).

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: update README for color-block grid redesign"
```

---

## Self-Review

**Spec coverage:**
- Vivid-on-dark palette → Task 1 `:root` + accent classes. ✓
- Color-block grid layout → Task 1 `.grid`/`.tile` CSS, Task 2 markup. ✓
- Space Grotesk + Mono, drop Fraunces → Task 1 font link + body font; Task 4 README. ✓
- Per-tile fixed hand-picked accents → Task 2 `ac-*` classes per the Global Constraints assignment. ✓
- Hero in Space Grotesk → Task 1. ✓
- Hover/focus (glow, lift, arrow) → Task 1 `.tile:hover/:focus-visible`. ✓
- Load cascade + reduced motion → Task 1 CSS + Task 3 verification. ✓
- Accessibility (skip link, aria-label, focus-visible, reduced motion) → Tasks 1–3. ✓
- Container widens to ~960px → Task 1 `main { max-width: 960px }`. ✓
- README update → Task 4. ✓

**Placeholder scan:** No TBD/TODO; all code blocks are complete and literal.

**Type/name consistency:** Class names (`.tile`, `.tile-name`, `.tile-meta`, `.tile-tech`, `.tile-arrow`, `.ac-*`, `.grid`, `.section-label`, `.fade-target`, `.fade-in`) are defined in Task 1 and used identically in Task 2/3. Accent assignment in Task 2 markup matches the Global Constraints table.
