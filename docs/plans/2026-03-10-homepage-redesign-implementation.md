# Homepage Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the CRT terminal homepage with a dark, polished developer portfolio using glassmorphism cards, hero section, and project grid.

**Architecture:** Single-file rewrite of `index.html`. Remove all CRT effects (scanlines, vignette, flicker, boot sequence). Replace with modern dark portfolio: hero section up top, two-section project card grid below. Glassmorphism card styling with amber accent color carried from the old design.

**Tech Stack:** Vanilla HTML5, CSS3 (custom properties, grid, backdrop-filter), ES6 JavaScript (minimal — staggered fade-in only). JetBrains Mono via Google Fonts. No build tools.

---

### Task 1: Scaffold new HTML structure

**Files:**
- Modify: `index.html` (full rewrite)

**Step 1: Replace the HTML body content**

Strip everything between `<body>` tags (boot sequence, terminal div, script). Replace with new semantic structure:

```html
<a href="#main" class="sr-only">Skip to main content</a>

<main id="main">
    <header class="hero">
        <h1 class="hero-name">lab1702</h1>
        <p class="hero-tagline">games & tools</p>
        <a href="https://github.com/lab1702" target="_blank" rel="noopener noreferrer" class="hero-github" aria-label="lab1702 on GitHub">github.com/lab1702</a>
    </header>

    <nav aria-label="Projects">
        <section class="project-section">
            <h2 class="section-title">games</h2>
            <div class="card-grid">
                <a href="/netrek" class="card" aria-label="NETREK-WEB — space combat game built with Go and JavaScript">
                    <h3 class="card-title">NETREK-WEB</h3>
                    <p class="card-desc">Space combat multiplayer game</p>
                    <div class="card-tags">
                        <span class="tag">Go</span>
                        <span class="tag">JavaScript</span>
                    </div>
                </a>
                <a href="/gorgon-maps" class="card" aria-label="Project Gorgon Navigator — MMO map tool">
                    <h3 class="card-title">Project Gorgon Nav</h3>
                    <p class="card-desc">MMO map tool</p>
                    <div class="card-tags">
                        <span class="tag">JavaScript</span>
                    </div>
                </a>
                <a href="/word" class="card" aria-label="Word Garden — Scrabble-like word game">
                    <h3 class="card-title">Word Garden</h3>
                    <p class="card-desc">Word game</p>
                    <div class="card-tags">
                        <span class="tag">JavaScript</span>
                    </div>
                </a>
            </div>
        </section>

        <section class="project-section">
            <h2 class="section-title">tools</h2>
            <div class="card-grid">
                <a href="/detcrime" class="card" aria-label="Detroit Crime — Python and Streamlit data visualization">
                    <h3 class="card-title">Detroit Crime</h3>
                    <p class="card-desc">Crime data visualization</p>
                    <div class="card-tags">
                        <span class="tag">Python</span>
                        <span class="tag">Streamlit</span>
                    </div>
                </a>
                <a href="/tiresize" class="card" aria-label="Tire Size Calculator — tire comparison tool">
                    <h3 class="card-title">Tire Size Calc</h3>
                    <p class="card-desc">Tire comparison tool</p>
                    <div class="card-tags">
                        <span class="tag">JavaScript</span>
                    </div>
                </a>
                <a href="/chat" class="card" aria-label="Chat — chat application">
                    <h3 class="card-title">Chat</h3>
                    <p class="card-desc">Chat app</p>
                    <div class="card-tags">
                        <span class="tag">JavaScript</span>
                    </div>
                </a>
            </div>
        </section>
    </nav>
</main>
```

**Step 2: Verify HTML is valid**

Open `index.html` in browser. Should render unstyled content with correct heading hierarchy and all 6 project links working.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: scaffold new portfolio HTML structure"
```

---

### Task 2: CSS reset and custom properties

**Files:**
- Modify: `index.html` (the `<style>` block)

**Step 1: Replace the entire `<style>` block**

Remove all CRT styles. Start fresh with reset and custom properties:

```css
:root {
    --bg: #0a0a0a;
    --surface: rgba(255, 176, 0, 0.03);
    --border: rgba(255, 176, 0, 0.12);
    --border-hover: rgba(255, 176, 0, 0.3);
    --text-primary: #e8e8e8;
    --text-secondary: #888888;
    --accent: #ffb000;
    --accent-hover: #ffc840;
    --glow: rgba(255, 176, 0, 0.15);
    --radius: 8px;
}

*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
    font-size: clamp(0.875rem, 1.75vw, 1rem);
    line-height: 1.6;
    background: var(--bg);
    color: var(--text-primary);
    min-height: 100vh;
    overflow-x: hidden;
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
```

**Step 2: Verify in browser**

Page should show unstyled content on dark background with off-white JetBrains Mono text.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add CSS reset and design tokens"
```

---

### Task 3: Background gradient and page layout

**Files:**
- Modify: `index.html` (append to `<style>` block)

**Step 1: Add background gradient and main layout**

```css
/* Subtle radial gradient for depth */
body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(
        ellipse at 50% 0%,
        rgba(255, 176, 0, 0.04) 0%,
        transparent 70%
    );
    pointer-events: none;
    z-index: -1;
}

main {
    max-width: 800px;
    width: 100%;
    margin: 0 auto;
    padding: 0 clamp(1rem, 4vw, 2rem);
}
```

**Step 2: Verify in browser**

Very faint warm glow at top center of page. Content centered with max-width 800px.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add background gradient and page layout"
```

---

### Task 4: Hero section styling

**Files:**
- Modify: `index.html` (append to `<style>` block)

**Step 1: Add hero styles**

```css
.hero {
    text-align: center;
    padding: 20vh 0 4rem;
}

.hero-name {
    font-size: clamp(2rem, 5vw, 2.5rem);
    font-weight: 700;
    color: var(--accent);
    letter-spacing: 0.02em;
}

.hero-tagline {
    color: var(--text-secondary);
    font-size: clamp(0.875rem, 2vw, 1rem);
    margin-top: 0.5rem;
}

.hero-github {
    display: inline-block;
    margin-top: 1rem;
    color: var(--text-secondary);
    text-decoration: none;
    font-size: clamp(0.75rem, 1.5vw, 0.875rem);
    transition: color 200ms ease;
}

.hero-github:hover {
    color: var(--accent-hover);
}

.hero-github:focus-visible {
    color: var(--accent-hover);
    outline: 2px solid var(--accent);
    outline-offset: 4px;
    border-radius: 2px;
}
```

**Step 2: Verify in browser**

Hero centered at top with amber name, gray tagline below, subtle GitHub link. Hover turns GitHub link amber. Tab to it — visible amber outline.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: style hero section"
```

---

### Task 5: Section titles and card grid layout

**Files:**
- Modify: `index.html` (append to `<style>` block)

**Step 1: Add section and grid styles**

```css
.project-section {
    margin-bottom: 3rem;
}

.section-title {
    font-size: clamp(0.75rem, 1.5vw, 0.875rem);
    font-weight: 400;
    color: var(--text-secondary);
    text-transform: lowercase;
    letter-spacing: 0.1em;
    margin-bottom: 1rem;
}

.card-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}

@media (max-width: 768px) {
    .card-grid {
        grid-template-columns: 1fr;
    }
}
```

**Step 2: Verify in browser**

Two sections visible with lowercase gray headers. Cards in 2-col grid on desktop, 1-col on mobile. Resize browser to confirm responsive breakpoint at 768px.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add section titles and card grid layout"
```

---

### Task 6: Glassmorphism card styling

**Files:**
- Modify: `index.html` (append to `<style>` block)

**Step 1: Add card base styles**

```css
.card {
    display: block;
    text-decoration: none;
    padding: 1.25rem;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: transform 200ms ease, border-color 200ms ease, box-shadow 200ms ease;
    min-height: 44px;
}

.card-title {
    font-size: 1rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.25rem;
}

.card-desc {
    font-size: 0.875rem;
    color: var(--text-secondary);
    margin-bottom: 0.75rem;
}

.card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.tag {
    font-size: 0.75rem;
    color: var(--accent);
    background: rgba(255, 176, 0, 0.08);
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
}
```

**Step 2: Add card hover and focus states**

```css
.card:hover {
    transform: translateY(-2px);
    border-color: var(--border-hover);
    box-shadow: 0 4px 20px var(--glow);
}

.card:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
    transform: translateY(-2px);
    border-color: var(--border-hover);
    box-shadow: 0 4px 20px var(--glow);
}
```

**Step 3: Verify in browser**

Cards should show frosted glass appearance with faint amber tint. Hover lifts card and adds amber glow. Tab through cards — each gets visible amber outline. Tech tags show as amber pills.

**Step 4: Verify contrast ratios**

Check these manually or with browser dev tools:
- `#e8e8e8` on `#0a0a0a` → ~17:1 (AAA pass)
- `#888888` on `#0a0a0a` → ~5.5:1 (AA pass)
- `#ffb000` on `#0a0a0a` → ~9.6:1 (AAA pass)
- `#ffb000` on `rgba(255,176,0,0.08)` over `#0a0a0a` → verify ≥4.5:1

**Step 5: Commit**

```bash
git add index.html
git commit -m "feat: add glassmorphism card styling with hover and focus states"
```

---

### Task 7: Staggered fade-in animation

**Files:**
- Modify: `index.html` (append to `<style>` block, add `<script>` before `</body>`)

**Step 1: Add fade-in keyframe and utility class**

```css
@keyframes fade-in-up {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-target {
    opacity: 0;
}

.fade-in {
    animation: fade-in-up 400ms ease forwards;
}

@media (prefers-reduced-motion: reduce) {
    .fade-target {
        opacity: 1;
    }
    .fade-in {
        animation: none;
        opacity: 1;
    }
}
```

**Step 2: Add `fade-target` class to animated elements in HTML**

Add `class="fade-target"` to: `.hero`, each `.card`, and `.section-title` elements.

**Step 3: Add stagger script**

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

**Step 4: Verify in browser**

Reload page. Hero fades in first, then section titles and cards cascade in with 50ms delays. Enable reduced motion in OS settings — content appears immediately with no animation.

**Step 5: Commit**

```bash
git add index.html
git commit -m "feat: add staggered fade-in animation with reduced motion support"
```

---

### Task 8: Mobile responsiveness and polish

**Files:**
- Modify: `index.html` (update `<style>` block)

**Step 1: Add mobile refinements**

```css
@media (max-width: 480px) {
    .hero {
        padding: 12vh 0 3rem;
    }

    .card {
        padding: 1rem;
    }
}
```

**Step 2: Verify on mobile viewport sizes**

Use browser dev tools responsive mode:
- 375px (iPhone SE): single column, readable text, tappable cards
- 768px: grid collapses to single column
- 1024px+: 2-column grid, hero centered

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add mobile responsive refinements"
```

---

### Task 9: Final WCAG audit and cleanup

**Files:**
- Modify: `index.html`

**Step 1: Verify semantic structure**

Confirm in the HTML:
- One `<h1>` (hero name)
- Two `<h2>`s (section titles)
- `<h3>`s inside cards
- `<nav>` wrapping project sections
- `<main>` wrapping everything
- Skip-to-content link as first element in body

**Step 2: Verify all links have aria-labels**

Every `<a>` should have an `aria-label` describing the destination.

**Step 3: Verify keyboard navigation**

Tab through the entire page:
1. Skip link → 2. GitHub link → 3-5. Game cards → 6-8. Tool cards
Every focusable element must have a visible focus indicator.

**Step 4: Update `<head>` meta description if needed**

Keep existing meta tags, ensure `theme-color` is still `#0a0a0a`.

**Step 5: Remove any leftover CRT-related CSS or HTML**

Search for any remaining references to: boot, terminal, scanlines, vignette, flicker, blink, cursor, prompt, separator, marker, term-*.

**Step 6: Commit**

```bash
git add index.html
git commit -m "fix: final WCAG audit and cleanup of old CRT references"
```
