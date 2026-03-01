# CRT Terminal Redesign — Design Document

## Goal

Redesign lab1702's landing page as a full amber CRT terminal experience. Same content structure (Games and Tools sections), completely new visual identity — the page should look and feel like powering on a vintage phosphor monitor in a lab.

## Color & Typography

- **Background**: `#0a0a0a` (near-black)
- **Primary text**: `#ffb000` (warm amber phosphor)
- **Dimmed text**: `#805800` (half-brightness amber for descriptions)
- **Highlight/hover**: `#ffc840` (brighter amber)
- **Glow color**: `rgba(255, 176, 0, 0.4)` (text-shadow bloom)
- **No light mode** — dark only
- **Font**: `'JetBrains Mono', 'Fira Code', 'Courier New', monospace`
- **Base size**: 16px, scaled with `clamp()` for responsiveness
- **Line height**: 1.6

## CRT Effects

### Scanlines
- CSS `::after` pseudo-element on body
- Repeating linear gradient, thin dark lines every 2-3px
- Opacity ~0.05-0.08 — subtle texture
- `pointer-events: none`

### Screen glow/bloom
- Double-layer amber `text-shadow`: one tight (1px), one diffuse (5-8px)
- Box-shadow vignette on body edges (darker corners, brighter center)
- Faint radial gradient on background (lighter center, simulating convex screen)

### Screen flicker
- CSS keyframe: opacity varies between ~0.97 and 1.0 on a ~4s cycle
- Barely perceptible

### Accessibility
- All CRT effects disabled inside `@media (prefers-reduced-motion: reduce)`
- Base amber-on-black contrast remains WCAG AA compliant without glow

## Boot Sequence (Intro Animation)

Replaces the current character-by-character "lab1702" reveal.

### Sequence
1. Screen "powers on" — background fades from pure black to `#0a0a0a` over ~500ms
2. Blinking cursor appears (`_`, blinking at ~530ms)
3. Text types out line by line (~40ms per character):
   ```
   > login lab1702
   authenticating...
   welcome, lab1702
   last login: <today's date>
   ```
4. Brief pause (~600ms), then main content fades in over ~400ms
5. Cursor remains blinking at bottom of content (decorative)

### Timing
- ~300ms pause between lines
- `authenticating...` types slower with longer pause before `welcome`
- Total duration: ~3-4 seconds

### Skip
- Click or any keypress immediately reveals all content
- `prefers-reduced-motion` skips boot entirely — content shows immediately

## Layout & Content

Single column always. No multi-column — terminals don't do that.

### Structure
```
[boot sequence]

lab1702@home:~$ ls ~/games
─────────────────────
> NETREK-WEB          space combat
> Project Gorgon Nav  mmo map tool
> Word Garden         word game

lab1702@home:~$ ls ~/tools
─────────────────────
> Detroit Crime (R)   shiny app
> Detroit Crime (Py)  streamlit app
> Tire Size Calc      tire comparison

─────────────────────
lab1702@home:~$ _
```

- **Header**: Eliminated — the boot sequence serves as the header
- **Sections**: Introduced by prompt lines (`lab1702@home:~$ ls ~/games`)
- **Links**: `>` prefixed lines, project name + short description, full line clickable
- **Separator**: Dash lines (`─────`) between sections
- **Footer**: Final prompt with blinking cursor
- **Emojis**: Removed — terminals don't have emojis
- **Responsive**: Single column, font scales via `clamp()`, text wraps naturally on mobile

## Link Interactions

### Default
- Dim amber (`#ffb000`), no underline, `>` prefix

### Hover
- Text brightens to `#ffc840`
- Text-shadow glow intensifies (phosphor flare)
- `>` shifts to `>>` (~150ms transition)
- Cursor: pointer

### Focus (keyboard)
- Same brightness as hover
- Dotted amber underline for tracking
- No box-shadow ring

### Active (click)
- Flash to near-white (`#ffe0a0`) for ~100ms (phosphor overload)
- Then navigates

### External links
- All open in new tabs (`target="_blank"`)
- `rel="noopener noreferrer"` maintained
