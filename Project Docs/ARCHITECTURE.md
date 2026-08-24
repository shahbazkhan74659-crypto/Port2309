# Architecture

This describes the **actual current implementation** — a single static prototype — followed by the **planned** production architecture, which is not yet implemented. See `DECISIONS.md` for the reasoning behind the planned stack.

## System Overview

**Implemented:** The repository contains exactly one file, `prototype/index.html` — a self-contained, client-side-rendered mockup with no server, no build step, and no dependencies beyond a Google Fonts stylesheet link. There is no git repository, no package manifest, and no production application code.

**Planned:** A Django server rendering HTML templates, styled with Tailwind CSS, with React mounted into specific DOM nodes ("islands") for interactive pieces. Not implemented yet.

## Technology Stack

**Implemented (prototype):**
- Plain HTML, inline CSS (`<style>` block), inline JavaScript (`<script>` block, IIFE, `"use strict"`)
- No framework, no bundler, no package manager, no build tooling
- External dependency: Google Fonts (Archivo, Inter, IBM Plex Mono), loaded via `<link>` tags

**Planned (production, not implemented):**
- Python Django
- Django templates
- Tailwind CSS
- React + JavaScript, mounted as islands into specific DOM nodes (not a full SPA)
- A relational database — PostgreSQL or MySQL, engine choice deferred until closer to a hosting decision (see `DECISIONS.md`)
- Stack is explicitly open to adding further tools as needed; not considered closed

## Application Structure

**Implemented:** `prototype/index.html` is the entire application — head metadata, all CSS, an empty `<div id="app"></div>` mount point, and all JavaScript (data, rendering, and routing logic) in one file.

**Planned:** Not yet scaffolded. As of 2026-08-24 the owner settled on exactly two Django apps (superseding an earlier three-app plan — see `DECISIONS.md`):
- `core` — views, URLs, and the main routing of the site; identity, etc.
- `projects` — the owner's projects, works, and code

Where the rest of the originally-planned feature set (Designs, Blog, Resume, Timeline, Hire Me) lands is unresolved — to be defined per feature as those phases come up. See `DECISIONS.md`.

Plus one global `templates/` folder and one global `static/` folder at the project root (not per-app).

## Component Structure

**Implemented:** The prototype has no component framework. It uses plain JavaScript functions that build and return HTML strings, assembled into `#app`'s `innerHTML`:
- `renderNav`, `renderFooter` — shared chrome
- `renderHome`, `renderProjectsPage`, `renderProjectDetail`, `renderAbout`, `renderContact`, `renderNotFound` — page-level renderers
- `mockupFor` / `mockupBar` — decorative "browser chrome" project mockups (no real screenshots)
- `renderContactForm` / `renderSuccessPanel` / `wireContactForm` — client-side-only contact form and validation

**Planned:** Not yet defined — will depend on Django template structure and which pieces become React islands.

## Data Flow

**Implemented:** All content is hardcoded in JavaScript objects/arrays at the top of the script — `PROFILE`, `SOCIALS`, `PROJECTS`, `NAV_ITEMS`. On load and on every `hashchange`, `render()` reads `window.location.hash`, picks a page renderer, and replaces `#app`'s `innerHTML` with `renderNav() + <main> + renderFooter()`. There is no data fetching, no API, and no persistence.

**Planned:** Not yet defined — will depend on Django models/views (per `contents` app) once implemented.

## State Management

**Implemented:** No state management beyond the DOM itself. Contact-form validation state is tracked via `aria-invalid` attributes and inline error text set directly on DOM elements.

**Planned:** Not yet defined.

## Routing

**Implemented:** Client-side hash-based routing only, handled entirely in `render()`:
- `#/` → Home
- `#/projects` → Projects list
- `#/projects/:slug` → Project detail (falls back to a "Not found" page for unknown slugs)
- `#/about` → About
- `#/contact` → Contact
- any other path → "Not found" page

Routing is driven by the browser's `hashchange` event; there is no server-side routing.

**Planned:** Django URL routing (per app: `core`, `contents`, `hiring`) — not yet implemented.

## API Architecture

Not applicable. No API exists in the prototype, and none has been implemented for the planned production system.

## Data / Persistence

**Implemented:** Not applicable. The prototype has no database or persistence layer; all data is hardcoded in the script. The contact form does not send data anywhere — submitting it simulates success client-side only (the prototype explicitly tells the user "this is a prototype, so nothing was actually sent").

**Planned:** A relational database via Django's ORM. Engine: To be defined — PostgreSQL or MySQL, deliberately deferred until closer to a hosting decision (see `DECISIONS.md`). No schema/models exist yet.

## Authentication & Authorization

Not applicable. No auth exists in the prototype or in any implemented production code.

## External Integrations

**Implemented:** Google Fonts, loaded via `<link rel="preconnect">` and a stylesheet `<link>` in the document head. This is the only external dependency in the repository.

**Planned:** None currently established.

## Build & Runtime

**Implemented:** None. The file can be opened directly in a browser or served as a static file; there is no build step, package manager, or dev server.

**Planned:** Not yet defined — will depend on the Django + Tailwind + React toolchain once set up.

## Architectural Boundaries

Production architectural boundaries (Django app responsibilities, template/static layout) are decided in principle (see `DECISIONS.md`) but not yet implemented in code. The prototype has no architectural boundaries beyond being a single file.

## Important Invariants

None established in code yet.
