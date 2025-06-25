# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal homepage/landing page for lab1702's collection of web applications and tools. The repository contains a single-page application that serves as a navigation hub for various coding projects.

## Architecture

The project is a simple static website consisting of:
- **index.html** - Main landing page with navigation to different applications
- **README.md** - Project documentation
- **LICENSE** - MIT license file

The homepage showcases two categories of applications:
1. **Traditional Coding** - R/Shiny applications (Trading Assistant, Tire Size Calculator, Detroit Crime Incidents)
2. **Vibe Coding (Claude Code)** - Modern web applications (Stock Analysis Hub, HTML/CSS/JS Tire Calculator, Detroit Crime analysis)

## Technical Details

- **Frontend**: Vanilla HTML, CSS, and JavaScript
- **Styling**: CSS custom properties with automatic dark mode support via `prefers-color-scheme`
- **Responsive**: Mobile-first design with clamp() functions for fluid typography
- **Accessibility**: ARIA labels, semantic HTML, and focus management

## Development

This is a static website with no build process, testing framework, or package management. Changes can be made directly to the HTML file and tested by opening in a browser.

## Key Features

- Automatic dark/light mode switching based on system preferences
- Responsive grid layout that adapts to different screen sizes
- Hover effects and focus states for improved user interaction
- Clean, modern design with CSS custom properties for consistent theming