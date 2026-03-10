# Homepage Redesign Design

**Date:** 2026-03-10
**Goal:** Replace the CRT terminal aesthetic with a dark, polished developer portfolio while keeping the same content (3 games, 3 tools).

## Color & Typography

**Palette:**
- Background: `#0a0a0a`
- Card surface: `rgba(255, 176, 0, 0.03)` (faint amber tint)
- Card border: `rgba(255, 176, 0, 0.12)`
- Text primary: `#e8e8e8`
- Text secondary: `#888888`
- Accent: `#ffb000` (amber, carried from old design)
- Accent hover: `#ffc840`

**Typography:**
- Font: JetBrains Mono (keep from current site)
- Hero name: ~2rem bold
- Hero tagline: smaller, secondary color
- Card titles: medium bold
- Card descriptions: regular, secondary color
- Tech tags: small, monospace

## Layout & Structure

**Hero Section:**
- Centered, generous vertical padding (~20vh top)
- `lab1702` in large bold amber
- One-line tagline in secondary text
- GitHub link below tagline, subtle styling

**Project Grid:**
- Two sections ("games", "tools") with simple text headers
- 2-column responsive grid
- Collapses to 1 column on mobile (<=768px)

**Footer:**
- Minimal or none — GitHub link lives in the hero

## Card Design

**Glassmorphism cards:**
- `backdrop-filter: blur(12px)` with semi-transparent amber-tinted background
- Thin amber border at low opacity
- Rounded corners (8px), padding 1.25rem
- Entire card is a clickable link

**Card content:**
- Project name (bold, primary text)
- Description (one line, secondary text)
- Tech tags (small pills, faint amber background, amber text)

**Tech tags per project:**
- NETREK-WEB: Go, JavaScript
- Project Gorgon Nav: JavaScript
- Word Garden: JavaScript
- Detroit Crime: Python, Streamlit
- Tire Size Calc: JavaScript
- Chat: TBD

**Hover state:**
- `translateY(-2px)` lift
- Border brightens to `rgba(255,176,0, 0.3)`
- Subtle amber box-shadow glow
- 200ms transition

**Focus state:**
- Same as hover plus visible amber outline

## Animation & Effects

- Page load: content fades in (~400ms), cards stagger in (50ms delay per card)
- Background: subtle radial gradient for depth
- No scanlines, flicker, or CRT effects
- `prefers-reduced-motion`: disables all animations, shows content immediately

## WCAG 2.1 AA Compliance

- **Contrast:** All text meets 4.5:1 minimum. Amber on black ~9.6:1. Off-white on black ~17:1. Secondary text ~5.5:1. Tech tag contrast verified against tag background.
- **Touch targets:** All cards meet 44x44px minimum
- **Keyboard:** Full tab order, visible focus indicators, skip-to-content link
- **Semantic HTML:** Proper heading hierarchy (h1 name, h2 sections), nav, main, section
- **ARIA:** Labels on all links, aria-label on sections
- **Reduced motion:** prefers-reduced-motion disables all transitions/animations
- **Color independence:** No information conveyed by color alone

## Technical Constraints

- Single-file vanilla HTML/CSS/JS (same as current)
- No external dependencies beyond Google Fonts
- Static deployment to GitHub Pages
