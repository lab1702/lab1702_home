# Warm-Menu Homepage Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the amber CRT-terminal `index.html` with a calm, typographic "menu" of projects in a Warm Charcoal palette.

**Architecture:** Single hand-written static `index.html` served by GitHub Pages — no build step, no dependencies. All styling is in one inline `<style>` block; one tiny inline `<script>` handles the optional on-load fade. The redesign is presentation-only: every project link and meta tag is preserved.

**Tech Stack:** HTML + CSS, Google Fonts (Fraunces + JetBrains Mono). No framework, no tooling.

**Spec:** `docs/plans/2026-06-11-homepage-warm-menu-redesign-design.md`

**Verification note:** No unit-test framework exists in this repo. Verification is (a) `grep` checks for required structure and (b) live visual check in the visual-companion browser already running at the URL from the brainstorm session (`.superpowers/brainstorm/*/state/server-info`). If that server is gone, open the file directly: `python3 -m http.server` from the repo root and visit `/index.html`.

---

## File Structure

- **Modify (full rewrite):** `index.html` — the only file changed. Sections in order: `<head>` (meta + fonts), inline `<style>` (palette tokens → base → hero → sections → rows → motion/responsive), `<body>` markup (skip link → hero → two project sections), inline `<script>` (gated fade-in).

No other files are created or modified.

---

## Task 1: Rewrite `index.html` as the Warm-Menu page

**Files:**
- Modify: `index.html` (replace entire file contents)

- [ ] **Step 1: Back up the current file for reference**

```bash
cp index.html /tmp/index.html.crt-backup
```

This lets you diff against the old version while working. Expected: no output.

- [ ] **Step 2: Replace the entire contents of `index.html` with the following**

Write this exact content to `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Lab1702's collection of coding projects — games, data analysis tools, and utilities">
    <meta property="og:title" content="lab1702">
    <meta property="og:description" content="Collection of coding projects — games, data analysis tools, and utilities">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://lab1702.github.io">
    <meta name="twitter:card" content="summary">
    <meta name="theme-color" content="#1a1714">
    <title>lab1702</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=JetBrains+Mono:wght@400;500&display=swap">
    <style>
        :root {
            --bg: #1a1714;
            --text: #e9dcc6;
            --bright: #f4ead6;
            --muted: #9b8d77;
            --faint: #7d7264;
            --leader: #3a332c;
            --leader-hot: #5a4636;
            --accent: #c98a5e;
            --accent-hot: #ef9a5c;
        }

        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html { -webkit-font-smoothing: antialiased; }

        body {
            font-family: 'Fraunces', Georgia, 'Times New Roman', serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            overflow-x: hidden;
            background-image: radial-gradient(55% 38% at 50% -6%, rgba(201, 123, 84, 0.10), transparent 70%);
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
            color: var(--accent);
            white-space: normal;
            z-index: 10000;
        }

        main {
            max-width: 560px;
            margin: 0 auto;
        }

        /* Hero */
        .hero { margin-bottom: 3.5rem; }

        .hero-name {
            font-size: clamp(2.4rem, 7vw, 3.1rem);
            font-weight: 700;
            color: var(--bright);
            letter-spacing: -0.02em;
            line-height: 1;
        }

        .hero-github {
            display: inline-block;
            margin-top: 1.1rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.04em;
            color: var(--faint);
            text-decoration: none;
            transition: color 200ms ease;
        }

        .hero-github:hover { color: var(--accent); }

        .hero-github:focus-visible {
            color: var(--accent);
            outline: 2px solid var(--accent);
            outline-offset: 4px;
            border-radius: 2px;
        }

        /* Sections */
        .project-section { margin-bottom: 2.75rem; }

        .section-label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.68rem;
            font-weight: 400;
            text-transform: uppercase;
            letter-spacing: 0.24em;
            color: var(--muted);
            margin-bottom: 0.4rem;
        }

        /* Menu rows */
        .row {
            display: flex;
            align-items: baseline;
            gap: 0.7rem;
            padding: 0.6rem 0;
            text-decoration: none;
            color: inherit;
        }

        .row-name {
            font-size: 1.32rem;
            font-weight: 600;
            color: var(--bright);
            white-space: nowrap;
            transition: color 180ms ease;
        }

        .row-arrow {
            color: var(--accent-hot);
            opacity: 0;
            margin-left: -0.35rem;
            transform: translateX(-4px);
            transition: opacity 180ms ease, transform 180ms ease;
        }

        .row-leader {
            flex: 1;
            align-self: stretch;
            border-bottom: 2px dotted var(--leader);
            transform: translateY(-0.35rem);
            transition: border-color 180ms ease;
        }

        .row-tech {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            color: var(--accent);
            white-space: nowrap;
            transition: color 180ms ease;
        }

        .row:hover .row-name,
        .row:focus-visible .row-name { color: var(--accent-hot); }

        .row:hover .row-arrow,
        .row:focus-visible .row-arrow { opacity: 1; transform: translateX(0); }

        .row:hover .row-leader,
        .row:focus-visible .row-leader { border-color: var(--leader-hot); }

        .row:hover .row-tech,
        .row:focus-visible .row-tech { color: var(--accent-hot); }

        .row:focus-visible {
            outline: 2px solid var(--accent);
            outline-offset: 4px;
            border-radius: 3px;
        }

        /* On-load fade (carried over, gated by reduced-motion) */
        @keyframes fade-in-up {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .fade-target { opacity: 0; }
        .fade-in { animation: fade-in-up 400ms ease forwards; }

        @media (prefers-reduced-motion: reduce) {
            .fade-target { opacity: 1; }
            .fade-in { animation: none; opacity: 1; }
            .row-name, .row-arrow, .row-leader, .row-tech,
            .hero-github { transition: none; }
        }
    </style>
</head>
<body>
<a href="#main" class="sr-only">Skip to main content</a>

<main id="main">
    <header class="hero fade-target">
        <h1 class="hero-name">lab1702</h1>
        <a href="https://github.com/lab1702" target="_blank" rel="noopener noreferrer" class="hero-github" aria-label="lab1702 on GitHub">github.com/lab1702 ↗</a>
    </header>

    <nav aria-label="Projects">
        <section class="project-section">
            <h2 class="section-label fade-target">games</h2>

            <a href="/netrek" class="row fade-target" aria-label="Netrek Web — space combat multiplayer game built with Go and JavaScript">
                <span class="row-name">Netrek Web</span>
                <span class="row-arrow" aria-hidden="true">→</span>
                <span class="row-leader" aria-hidden="true"></span>
                <span class="row-tech">go · js</span>
            </a>
            <a href="/word" class="row fade-target" aria-label="Word Garden — word game">
                <span class="row-name">Word Garden</span>
                <span class="row-arrow" aria-hidden="true">→</span>
                <span class="row-leader" aria-hidden="true"></span>
                <span class="row-tech">js</span>
            </a>
            <a href="/gorgon-maps" class="row fade-target" aria-label="Project Gorgon Nav — MMO map tool">
                <span class="row-name">Project Gorgon Nav</span>
                <span class="row-arrow" aria-hidden="true">→</span>
                <span class="row-leader" aria-hidden="true"></span>
                <span class="row-tech">js</span>
            </a>
        </section>

        <section class="project-section">
            <h2 class="section-label fade-target">tools</h2>

            <a href="/detcrime" class="row fade-target" aria-label="Detroit Crime — crime data visualization built with Python and Streamlit">
                <span class="row-name">Detroit Crime</span>
                <span class="row-arrow" aria-hidden="true">→</span>
                <span class="row-leader" aria-hidden="true"></span>
                <span class="row-tech">python · streamlit</span>
            </a>
            <a href="/tiresize" class="row fade-target" aria-label="Tire Size Calc — tire comparison tool">
                <span class="row-name">Tire Size Calc</span>
                <span class="row-arrow" aria-hidden="true">→</span>
                <span class="row-leader" aria-hidden="true"></span>
                <span class="row-tech">js</span>
            </a>
            <a href="/chat" class="row fade-target" aria-label="Chat — chat application">
                <span class="row-name">Chat</span>
                <span class="row-arrow" aria-hidden="true">→</span>
                <span class="row-leader" aria-hidden="true"></span>
                <span class="row-tech">js</span>
            </a>
            <a href="/ccalendar.html" class="row fade-target" aria-label="Cruise Calendar — South East Michigan car cruises and events">
                <span class="row-name">Cruise Calendar</span>
                <span class="row-arrow" aria-hidden="true">→</span>
                <span class="row-leader" aria-hidden="true"></span>
                <span class="row-tech">html</span>
            </a>
            <a href="/detroit-crime-weather" class="row fade-target" aria-label="Crime & Weather — analysis of weather impact on Detroit crime">
                <span class="row-name">Crime &amp; Weather</span>
                <span class="row-arrow" aria-hidden="true">→</span>
                <span class="row-leader" aria-hidden="true"></span>
                <span class="row-tech">python · pandas</span>
            </a>
            <a href="/trading" class="row fade-target" aria-label="Ichimoku Trading — trading strategy app using the R ichimoku package">
                <span class="row-name">Ichimoku Trading</span>
                <span class="row-arrow" aria-hidden="true">→</span>
                <span class="row-leader" aria-hidden="true"></span>
                <span class="row-tech">r · shiny</span>
            </a>
        </section>
    </nav>
</main>
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
</body>
</html>
```

- [ ] **Step 3: Structural verification with grep**

Run each and confirm the expected result:

```bash
grep -c 'class="row ' index.html      # Expected: 9  (all 9 project links)
grep -c 'row-leader' index.html       # Expected: 18 (one CSS rule region + 9 spans... see note)
grep -o 'href="/[^"]*"' index.html    # Expected: /netrek /word /gorgon-maps /detcrime /tiresize /chat /ccalendar.html /detroit-crime-weather /trading
grep -c 'Fraunces' index.html         # Expected: >=2 (font link + font-family)
grep -c '#1a1714' index.html          # Expected: >=2 (theme-color + --bg)
grep -c 'Fira Code' index.html        # Expected: 0  (old font fully removed)
```

For the `href` check, confirm all **9** project paths appear and match the spec exactly. (Ignore the exact count for `row-leader`; just confirm it appears in both the CSS and the markup.)

- [ ] **Step 4: Live visual verification in the browser**

Copy the new file into the visual-companion content dir so it renders at the existing URL, OR serve it directly. Easiest: serve the repo and open it.

```bash
# from repo root
python3 -m http.server 8000 >/dev/null 2>&1 &
echo "open http://localhost:8000/index.html"
```

Confirm by eye:
- Centered ~560px column, content left-aligned, generous side margins on a wide window.
- Hero: "lab1702" in Fraunces serif + mono "github.com/lab1702 ↗" beneath it. No tagline.
- Two labelled sections (`games`, `tools`) with 3 and 6 rows respectively.
- Hovering a row: name warms to terracotta, arrow slides in, dotted leader + tech brighten.
- Tab key moves focus row-to-row with a visible outline; GitHub link is focusable.
- Resize narrow: single column, `1.5rem` side padding, no horizontal scroll.

Stop the server when done:

```bash
kill %1 2>/dev/null
```

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: redesign homepage as warm typographic menu

Replace amber CRT-terminal aesthetic with a Warm Charcoal palette and a
contents-page menu layout (Fraunces serif + JetBrains Mono, dotted leaders,
terracotta hover). Presentation-only: all 9 project links and meta tags preserved.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 2: Update README if it describes the old look

**Files:**
- Modify: `README.md` (only if it references the terminal/amber aesthetic)

- [ ] **Step 1: Check whether the README describes the visual design**

```bash
grep -niE 'amber|terminal|crt|fira|glassmorph|monospace' README.md
```

Expected: either no matches (then **skip this task entirely** — nothing to do) or lines describing the old aesthetic.

- [ ] **Step 2: If there were matches, update only those descriptions**

Edit the matched lines so they describe the new design: a "warm, typographic menu of projects" in a "Warm Charcoal palette with Fraunces + JetBrains Mono." Do not invent new sections; only correct stale wording. Leave project listings and links untouched.

- [ ] **Step 3: Commit (only if README changed)**

```bash
git add README.md
git commit -m "docs: update README to match warm-menu homepage redesign

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Self-Review (completed during planning)

- **Spec coverage:** Palette tokens ✓, Fraunces+JetBrains Mono ✓, 560px centered left-aligned column ✓, hero name + github link, no tagline ✓, two sections ✓, dotted-leader rows with name/arrow/tech ✓, hover/focus states ✓, reduced-motion ✓, skip link + aria-labels + OG/meta preserved ✓, theme-color changed to `#1a1714` ✓, all 9 projects with exact hrefs ✓.
- **Placeholder scan:** No TBD/TODO; the full file is provided verbatim, not summarized.
- **Consistency:** Class names (`row`, `row-name`, `row-arrow`, `row-leader`, `row-tech`, `section-label`, `hero-github`, `fade-target`) are identical between the CSS and markup. Tech tags lowercased per spec. README task is conditional to avoid a no-op commit.
