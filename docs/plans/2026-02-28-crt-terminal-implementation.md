# CRT Terminal Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rewrite index.html as a full amber CRT terminal with boot sequence animation, scanline effects, and typed-command content presentation.

**Architecture:** Single-file rewrite of index.html. All CSS, HTML, and JS live in one file (no build tools). The page is a static site hosted on GitHub Pages. Google Fonts loads JetBrains Mono. CRT effects use CSS pseudo-elements and keyframes. Boot sequence uses vanilla JS with typed-text animation.

**Tech Stack:** HTML5, CSS3 (custom properties, keyframes, pseudo-elements), vanilla ES6 JavaScript, Google Fonts (JetBrains Mono)

**Design doc:** `docs/plans/2026-02-28-crt-terminal-redesign-design.md`

---

### Task 1: Replace CSS — Base Styles, Colors & Typography

**Files:**
- Modify: `index.html:14-325` (entire `<style>` block)

**Step 1: Replace the full `<style>` block with new base CSS**

Replace everything inside `<style>...</style>` with:

```css
/* CRT Terminal — Amber Phosphor */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

:root {
    --bg: #0a0a0a;
    --text: #ffb000;
    --text-dim: #805800;
    --text-bright: #ffc840;
    --text-flash: #ffe0a0;
    --glow: rgba(255, 176, 0, 0.4);
    --glow-strong: rgba(255, 176, 0, 0.6);
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
    color: var(--text);
    min-height: 100vh;
    padding: clamp(1rem, 4vw, 3rem);
    overflow-x: hidden;
    text-shadow: 0 0 1px var(--glow), 0 0 5px var(--glow);
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

**Step 2: Verify the file is valid HTML**

Open `index.html` in a browser. Expect: black background, amber monospace text, no layout yet (structure changes come later).

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: replace CSS with CRT amber base styles and typography"
```

---

### Task 2: Add CRT Effects — Scanlines, Vignette, Flicker

**Files:**
- Modify: `index.html` (append to `<style>` block)

**Step 1: Add CRT effect styles after the base styles**

Append to the `<style>` block:

```css
/* Scanlines overlay */
body::after {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(
        to bottom,
        transparent,
        transparent 2px,
        rgba(0, 0, 0, 0.08) 2px,
        rgba(0, 0, 0, 0.08) 4px
    );
    pointer-events: none;
    z-index: 9999;
}

/* Screen vignette and curvature simulation */
body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(
        ellipse at center,
        transparent 60%,
        rgba(0, 0, 0, 0.4) 100%
    );
    pointer-events: none;
    z-index: 9998;
}

/* Subtle screen flicker */
@keyframes flicker {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.97; }
}

body {
    animation: flicker 4s ease-in-out infinite;
}

/* Accessibility: disable all CRT effects for reduced motion */
@media (prefers-reduced-motion: reduce) {
    body::after,
    body::before {
        display: none;
    }
    body {
        animation: none;
        text-shadow: none;
    }
}
```

**Step 2: Verify in browser**

Expect: subtle scanlines visible on close inspection, darker edges/corners, barely-perceptible flicker.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add CRT scanlines, vignette, and flicker effects"
```

---

### Task 3: Rewrite HTML Structure — Terminal Layout

**Files:**
- Modify: `index.html:327-367` (everything inside `<body>` except `<script>`)

**Step 1: Replace the HTML body content**

Replace everything inside `<body>` (from the `<div id="intro">` through `</footer>`) with:

```html
<!-- Boot sequence overlay -->
<div id="boot" aria-live="polite">
    <span id="boot-text"></span><span id="cursor" class="blink">_</span>
</div>

<a href="#main" class="sr-only">Skip to main content</a>

<div id="terminal" class="content-hidden">
    <main id="main">
        <nav role="navigation" aria-label="Main navigation">
            <section class="term-section">
                <div class="prompt">lab1702@home:~$ ls ~/games</div>
                <div class="separator">────────────────────────────────</div>
                <ul class="term-list" role="list">
                    <li><a href="/netrek" target="_blank" rel="noopener noreferrer" aria-label="NETREK-WEB - space combat game built with Go and JavaScript"><span class="marker">&gt;</span> NETREK-WEB <span class="desc">space combat</span></a></li>
                    <li><a href="/gorgon-maps" target="_blank" rel="noopener noreferrer" aria-label="Project Gorgon Navigator - MMO map tool"><span class="marker">&gt;</span> Project Gorgon Nav <span class="desc">mmo map tool</span></a></li>
                    <li><a href="/word" target="_blank" rel="noopener noreferrer" aria-label="Word Garden - Scrabble-like word game"><span class="marker">&gt;</span> Word Garden <span class="desc">word game</span></a></li>
                </ul>
            </section>

            <section class="term-section">
                <div class="prompt">lab1702@home:~$ ls ~/tools</div>
                <div class="separator">────────────────────────────────</div>
                <ul class="term-list" role="list">
                    <li><a href="detroitcrime" target="_blank" rel="noopener noreferrer" aria-label="Detroit Crime Incidents analysis - R and Shiny"><span class="marker">&gt;</span> Detroit Crime (R) <span class="desc">shiny app</span></a></li>
                    <li><a href="detcrime" target="_blank" rel="noopener noreferrer" aria-label="Detroit Crime Incidents analysis - Python and Streamlit"><span class="marker">&gt;</span> Detroit Crime (Py) <span class="desc">streamlit app</span></a></li>
                    <li><a href="tiresize.html" target="_blank" rel="noopener noreferrer" aria-label="Tire Size Calculator"><span class="marker">&gt;</span> Tire Size Calc <span class="desc">tire comparison</span></a></li>
                </ul>
            </section>
        </nav>
    </main>

    <div class="separator">────────────────────────────────</div>
    <div class="prompt">lab1702@home:~$ <span id="cursor-bottom" class="blink">_</span></div>

    <footer class="term-footer">
        <a href="https://github.com/lab1702" aria-label="lab1702 on GitHub">
            <span class="marker">&gt;</span> github.com/lab1702
        </a>
    </footer>
</div>
```

**Step 2: Commit**

```bash
git add index.html
git commit -m "feat: rewrite HTML as terminal layout with prompt sections"
```

---

### Task 4: Add Terminal Layout & Link Interaction CSS

**Files:**
- Modify: `index.html` (append to `<style>` block, before the `@media (prefers-reduced-motion)` rule)

**Step 1: Add terminal layout and interaction styles**

Insert before the `@media (prefers-reduced-motion: reduce)` block:

```css
/* Boot sequence */
#boot {
    min-height: 100vh;
    display: flex;
    align-items: flex-start;
    padding: clamp(1rem, 4vw, 3rem);
    white-space: pre-wrap;
    word-break: break-word;
}

#boot-text {
    white-space: pre-wrap;
}

/* Blinking cursor */
.blink {
    animation: cursor-blink 530ms steps(1) infinite;
}

@keyframes cursor-blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

/* Terminal content */
#terminal {
    max-width: 720px;
    width: 100%;
}

.content-hidden {
    display: none;
}

.content-visible {
    display: block;
    animation: fade-in 400ms ease forwards;
}

@keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* Sections */
.term-section {
    margin-bottom: 1.5rem;
}

.prompt {
    color: var(--text);
    margin-bottom: 0.25rem;
}

.separator {
    color: var(--text-dim);
    margin-bottom: 0.5rem;
    user-select: none;
}

/* Links */
.term-list {
    list-style: none;
    padding: 0;
    margin: 0 0 0.5rem 0;
}

.term-list li a {
    display: block;
    color: var(--text);
    text-decoration: none;
    padding: 0.25rem 0.5rem;
    transition: color 0.15s ease, text-shadow 0.15s ease;
    min-height: 44px;
    display: flex;
    align-items: center;
}

.term-list li a .marker {
    display: inline-block;
    min-width: 1.5ch;
    transition: min-width 0.15s ease;
}

.term-list li a .desc {
    color: var(--text-dim);
    margin-left: 1ch;
    transition: color 0.15s ease;
}

/* Hover */
.term-list li a:hover {
    color: var(--text-bright);
    text-shadow: 0 0 2px var(--glow-strong), 0 0 8px var(--glow);
    cursor: pointer;
}

.term-list li a:hover .marker {
    min-width: 2.5ch;
}

.term-list li a:hover .marker::after {
    content: '>';
}

.term-list li a:hover .desc {
    color: var(--text-bright);
}

/* Focus (keyboard) */
.term-list li a:focus {
    outline: none;
    color: var(--text-bright);
    text-shadow: 0 0 2px var(--glow-strong), 0 0 8px var(--glow);
    text-decoration: underline;
    text-decoration-style: dotted;
    text-underline-offset: 4px;
}

.term-list li a:focus .desc {
    color: var(--text-bright);
}

/* Active (click flash) */
.term-list li a:active {
    color: var(--text-flash);
    text-shadow: 0 0 4px var(--glow-strong), 0 0 12px var(--glow);
}

/* Footer */
.term-footer {
    margin-top: 1.5rem;
    font-size: clamp(0.75rem, 1.5vw, 0.875rem);
}

.term-footer a {
    color: var(--text-dim);
    text-decoration: none;
    transition: color 0.15s ease;
}

.term-footer a:hover,
.term-footer a:focus {
    color: var(--text-bright);
}

.term-footer a:focus {
    outline: none;
    text-decoration: underline;
    text-decoration-style: dotted;
    text-underline-offset: 4px;
}
```

**Step 2: Verify in browser**

Links should show `>` prefix, brighten on hover with `>>`, dotted underline on focus, flash on click.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add terminal layout styles and link hover/focus/active states"
```

---

### Task 5: Rewrite JavaScript — Boot Sequence & Typed Animation

**Files:**
- Modify: `index.html` (replace `<script>` block)

**Step 1: Replace the entire `<script>` block with the boot sequence**

```javascript
(function () {
    const boot = document.getElementById('boot');
    const bootText = document.getElementById('boot-text');
    const cursor = document.getElementById('cursor');
    const terminal = document.getElementById('terminal');

    const today = new Date().toLocaleDateString('en-US', {
        weekday: 'short', year: 'numeric', month: 'short', day: 'numeric'
    });

    const lines = [
        { text: '> login lab1702', charDelay: 40, pauseAfter: 300 },
        { text: 'authenticating...', charDelay: 60, pauseAfter: 800 },
        { text: 'welcome, lab1702', charDelay: 40, pauseAfter: 300 },
        { text: 'last login: ' + today, charDelay: 40, pauseAfter: 600 }
    ];

    let skipped = false;

    function skip() {
        if (skipped) return;
        skipped = true;
        boot.style.display = 'none';
        terminal.classList.remove('content-hidden');
        terminal.classList.add('content-visible');
        document.removeEventListener('click', skip);
        document.removeEventListener('keydown', skip);
    }

    // Skip on click or keypress
    document.addEventListener('click', skip);
    document.addEventListener('keydown', skip);

    // Skip entirely for reduced motion
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        skip();
        return;
    }

    // Power-on: fade from black
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 500ms ease';
    requestAnimationFrame(function () {
        document.body.style.opacity = '1';
    });

    function typeLine(lineIndex) {
        if (skipped || lineIndex >= lines.length) {
            if (!skipped) {
                // Boot done — show terminal
                setTimeout(function () {
                    boot.style.display = 'none';
                    terminal.classList.remove('content-hidden');
                    terminal.classList.add('content-visible');
                }, lines[lines.length - 1].pauseAfter);
            }
            return;
        }

        var line = lines[lineIndex];
        var chars = line.text.split('');
        var charIndex = 0;

        // Add newline before each line except the first
        if (lineIndex > 0) {
            bootText.textContent += '\n';
        }

        function typeChar() {
            if (skipped) return;
            if (charIndex < chars.length) {
                bootText.textContent += chars[charIndex];
                charIndex++;
                setTimeout(typeChar, line.charDelay);
            } else {
                // Line done — pause then next line
                setTimeout(function () {
                    typeLine(lineIndex + 1);
                }, line.pauseAfter);
            }
        }

        typeChar();
    }

    // Start typing after power-on fade
    setTimeout(function () {
        typeLine(0);
    }, 600);
})();
```

**Step 2: Verify in browser**

Expect: screen fades in from black, cursor blinks, login text types out line by line, then terminal content appears. Click or keypress skips immediately.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: implement boot sequence with typed animation and skip support"
```

---

### Task 6: Remove Stale Markup & Clean Up

**Files:**
- Modify: `index.html`

**Step 1: Clean up the `<head>` section**

- Remove the Google Fonts `<link rel="preconnect">` tag (the `@import` in CSS handles font loading now)
- Update `<meta name="description">` if desired
- Update copyright year in footer area (already handled in HTML rewrite, verify it says 2025 or current)

**Step 2: Remove any leftover old CSS or HTML that wasn't caught in earlier tasks**

Scan through the file and verify:
- No Catppuccin variables remain
- No `.section-container`, `.menu`, `#intro`, `#intro-text` classes remain
- No `@media (prefers-color-scheme: dark)` block remains
- No old JavaScript remains

**Step 3: Full visual review in browser**

- Desktop: single column, amber text, CRT effects, boot sequence plays
- Mobile (narrow viewport): text wraps, font scales down, still readable
- Keyboard navigation: Tab through links, dotted underline visible
- Click a link: flash effect visible
- `prefers-reduced-motion`: no animation, content shown immediately

**Step 4: Commit**

```bash
git add index.html
git commit -m "chore: remove stale Catppuccin styles and clean up markup"
```

---

### Task 7: Final Polish & Responsive Check

**Files:**
- Modify: `index.html` (minor tweaks only)

**Step 1: Add responsive adjustments if needed**

```css
@media (max-width: 480px) {
    body {
        padding: 0.75rem;
    }

    .term-list li a {
        padding: 0.35rem 0.25rem;
    }
}
```

**Step 2: Verify the complete page end-to-end**

- Boot sequence timing feels right (~3-4 seconds)
- Skip works on first click/keypress
- All links navigate correctly
- CRT effects are subtle, not distracting
- Footer prompt has blinking cursor

**Step 3: Final commit**

```bash
git add index.html
git commit -m "feat: add responsive tweaks and finalize CRT terminal design"
```
