# Architecture

This describes the **actual current implementation** — the static prototype plus a Django project with Home, About, Contact, a static Projects page, a live-data GitHub page, and the `core`/`projects` apps, now carrying the owner's real content (Phases 1–5) — followed by the **planned** production architecture beyond that. See `DECISIONS.md` for the reasoning behind the planned stack.

## System Overview

**Implemented:** The repository contains `prototype/index.html` (the standalone static mockup, unchanged — kept only as a styling/layout reference per `DECISIONS.md`) plus a from-scratch Django project: `manage.py` and a `config/` settings package (created via `django-admin startproject config .`) running inside a project-local `.venv` with Django 5.2.14 pinned in `requirements.txt` (Phase 1, 2026-08-24). Phases 2–3 (2026-08-24) added Home, About, Contact, and a static Projects list page, plus a GitHub page added just after Phase 3 — all styled by a Tailwind CSS build (npm + Tailwind CLI v4) reproducing the prototype's design tokens. As of Phase 4 (2026-08-24), routing/views moved out of `config/` into a real `core` app (`core/views.py`, `core/urls.py` — the latter is now `ROOT_URLCONF` directly), and a `projects` app is scaffolded and registered but intentionally empty (no models/views/urls yet). `config/` now holds only `settings.py`/`wsgi.py`/`asgi.py`. As of Phase 5 (2026-08-24), Home/About/Contact/base.html carry the owner's real content instead of generic placeholders, and `/github/` fetches real, live profile data from GitHub's public API server-side — the one deliberate exception is Home's featured-project card and the entire Projects page, which the owner chose to leave on Phase 3's mockup/placeholder content until the `projects` app gains real models. No database models or React tooling exist yet.

**Planned:** A Django server rendering HTML templates, styled with Tailwind CSS, with React mounted into specific DOM nodes ("islands") for interactive pieces. Database models (including a real, model-backed Projects listing/detail, to live in the now-scaffolded `projects` app) and React tooling are not implemented yet.

## Technology Stack

**Implemented (prototype):**
- Plain HTML, inline CSS (`<style>` block), inline JavaScript (`<script>` block, IIFE, `"use strict"`)
- No framework, no bundler, no package manager, no build tooling
- External dependency: Google Fonts (Archivo, Inter, IBM Plex Mono), loaded via `<link>` tags

**Implemented (Django scaffold, Phase 1, 2026-08-24):**
- Python 3.11.9, Django 5.2.14
- Project-local virtual environment (`.venv/`, gitignored), dependencies pinned in `requirements.txt`
- Pillow 12.3.0 (added 2026-08-24) — image asset processing (e.g. background removal for the hero portrait), not used by the running Django app itself
- `requests` 2.34.2 (added Phase 5, 2026-08-24), with its transitive deps `certifi`/`charset-normalizer`/`idna`/`urllib3` — used by `core/views.py`'s `github` view to call GitHub's public REST API server-side

**Implemented (Tailwind, Phase 2, 2026-08-24):**
- Node v24.18.0 / npm 11.16.0, `tailwindcss` + `@tailwindcss/cli` v4.3.3 as devDependencies (`package.json`)
- Source stylesheet `static_src/css/input.css` (CSS-first `@theme` tokens + ported prototype component CSS), built to `static/css/main.css` (gitignored) via `npm run build:css` / `npm run watch:css`
- No React or database engine wired up yet — those remain planned

**Planned (production, not implemented):**
- Python Django
- Django templates
- Tailwind CSS
- React + JavaScript, mounted as islands into specific DOM nodes (not a full SPA)
- A relational database — PostgreSQL or MySQL, engine choice deferred until closer to a hosting decision (see `DECISIONS.md`)
- Stack is explicitly open to adding further tools as needed; not considered closed

## Application Structure

**Implemented:** `prototype/index.html` is a separate, standalone artifact — head metadata, all CSS, an empty `<div id="app"></div>` mount point, and all JavaScript (data, rendering, and routing logic) in one file.

**Implemented (Django, Phase 1):** `manage.py` and a `config/` package (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`, `views.py`) at the repo root.

**Implemented (Phase 2, 2026-08-24):** `config/views.py` holds a `home` view rendering `templates/pages/home.html`, wired directly in `config/urls.py` as `path('', views.home, name='home')` — an interim, app-less arrangement (see `DECISIONS.md`). One global `templates/` folder (`base.html` + `pages/home.html`) and one global `static/` folder (`css/main.css`, Tailwind-built), per the Phase 0 decision, are both now active via `TEMPLATES[0]['DIRS']`/`STATICFILES_DIRS` in `config/settings.py`.

**Implemented (Phase 3, 2026-08-24):** Same app-less pattern extended to three more pages — `config/views.py` gained `about`, `contact`, and `projects` view functions, each rendering their `templates/pages/*.html` counterpart, registered in `config/urls.py` as `path('about/', ...)` / `path('contact/', ...)` / `path('projects/', ...)`.

**Implemented (post-Phase 3 addition, 2026-08-24):** A `github` view/route (`/github/` → `templates/pages/github.html`) added the same way — a placeholder, read-only GitHub profile card (no live API call yet). See `DECISIONS.md` for why GitHub got a custom page while LinkedIn/Email did not.

**Implemented (Phase 4, 2026-08-24):** `core` and `projects` apps scaffolded via `manage.py startapp` and registered in `INSTALLED_APPS`. All five view functions (`home`, `about`, `contact`, `projects`, `github`) and the full `urlpatterns` list (including `admin/`) moved verbatim from `config/` into `core/views.py`/`core/urls.py`; `config/views.py` and `config/urls.py` were deleted. `ROOT_URLCONF` now points at `'core.urls'` directly — there is no `config/urls.py` and no `include()` layer, so `core.urls` *is* the site's root router (see `DECISIONS.md` for why this is `core`'s correct role, not a workaround). `projects` exists only as a registered, empty `startapp` scaffold — no models, views, or urls.py yet. The rest of the originally-planned feature set — Designs, Blog, Resume, Timeline, Hire Me — is resolved (2026-08-24) to live in `core`; `projects` is scoped strictly to the owner's projects/works/code. See `DECISIONS.md`.

**Planned:** `projects` gaining real models/views/urls (a `Project` model, list/detail views) in a future phase, at which point its `urls.py` would be `include()`d from `core/urls.py`.

## Component Structure

**Implemented:** The prototype has no component framework. It uses plain JavaScript functions that build and return HTML strings, assembled into `#app`'s `innerHTML`:
- `renderNav`, `renderFooter` — shared chrome
- `renderHome`, `renderProjectsPage`, `renderProjectDetail`, `renderAbout`, `renderContact`, `renderNotFound` — page-level renderers
- `mockupFor` / `mockupBar` — decorative "browser chrome" project mockups (no real screenshots)
- `renderContactForm` / `renderSuccessPanel` / `wireContactForm` — client-side-only contact form and validation

**Implemented (Django, Phase 2):** `templates/base.html` defines the shared shell (nav header, `<main id="main">` content block, footer) via `{% block content %}`; `templates/pages/home.html` extends it. No template partials/includes yet — nav and footer are inlined directly in `base.html`, since it is itself the single shared shell.

**Implemented (Django, Phase 3):** `templates/pages/about.html`, `templates/pages/contact.html`, and `templates/pages/projects.html` also extend `base.html`, following the same pattern as Home. `base.html`'s nav/footer now render active-page state via `{% if request.resolver_match.url_name == '...' %}aria-current="page"{% endif %}` per link (the `.nav-link[aria-current="page"]` CSS existed since the Phase 2 port but was unused until now).

**Implemented (post-Phase 5 addition, 2026-08-24):** The nav/footer brand mark in `base.html` (`.nav-mark`/`.foot-mark`) now renders the owner's real "SK" badge image (`static/images/sk-badge.png`) instead of an auto-derived "S." text mark. See `DECISIONS.md` for the background-removal technique used to clean the source asset.

**Planned:** Beyond the base shell, not yet defined — will depend on further Django template structure and which pieces become React islands.

## Data Flow

**Implemented:** All content is hardcoded in JavaScript objects/arrays at the top of the script — `PROFILE`, `SOCIALS`, `PROJECTS`, `NAV_ITEMS`. On load and on every `hashchange`, `render()` reads `window.location.hash`, picks a page renderer, and replaces `#app`'s `innerHTML` with `renderNav() + <main> + renderFooter()`. There is no data fetching, no API, and no persistence.

**Implemented (Django, Phase 2):** The Home page's content (name, tagline, roles, featured project, about snapshot, CTA copy) is hardcoded directly in `templates/pages/home.html` as generic placeholder text — not passed via view context, not model-backed. See `DECISIONS.md` for why (prototype content is fictional and must not be reused as real data; real content doesn't exist yet).

**Implemented (Django, Phase 3):** Same pattern for About, Contact, and Projects — all content is hardcoded directly in each template, not passed via view context. The Projects page's three entries are hardcoded markup, **not** a loop over a data structure or model — there is no `Project` model yet; each entry is a literal repeated block in `templates/pages/projects.html`. **Still true as of Phase 5** — this page and Home's featured-project card were deliberately excluded from the Phase 5 content swap (see `DECISIONS.md`) and remain exactly this way.

**Implemented (Django, Phase 5, 2026-08-24):** `base.html`, `home.html` (except the featured-project card), `about.html`, and `contact.html` now hold the owner's real hardcoded content (still not passed via view context — same "hardcoded in the template" pattern as before, just real text instead of generic placeholders). The GitHub page is the one exception to "hardcoded" — `core/views.py`'s `github` view now fetches live data server-side from `https://api.github.com/users/<username>` and passes it into the template context (`avatar_url`, `name`, `bio`, `public_repos`, `followers`, `following`, `html_url`), falling back to static real values on any request failure. See `DECISIONS.md` for both decisions.

**Implemented (post-Phase 5 addition, 2026-08-24):** The same `github` view also fetches the owner's repo list (`GET /users/<username>/repos?sort=updated`) and passes a `repos` list into the context; `templates/pages/github.html` renders it as a scrollable panel (`.repo-list`) beside the profile card, each entry linking out to its real GitHub URL. Falls back to an empty list (rendered as a small "not available right now" note) on request failure. See `DECISIONS.md`.

**Planned:** Real content/model-backed data for Home's featured project and the Projects page — will depend on the `projects` app gaining models/views once that phase happens.

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

**Implemented (Django, Phase 2):** Real server-side routing via `config/urls.py`: `path('', views.home, name='home')` → `/`.

**Implemented (Django, Phase 3):** `path('about/', ..., name='about')`, `path('contact/', ..., name='contact')`, `path('projects/', ..., name='projects')` added alongside `home`. Nav, footer, and Home's internal links (featured-project explore/mockup link → Projects, "more about me" → About, "get in touch" → Contact) all resolve via `{% url %}` now instead of `href="#"`. Remaining `href="#"` placeholders are limited to things with no real destination yet: GitHub/LinkedIn footer and CTA links (no real social URLs), and the Projects page's per-entry "Explore project"/"View on GitHub" actions (no detail routes or repo URLs yet — those depend on a real `Project` model).

**Implemented (Django, Phase 4):** All routing now lives in `core/urls.py`, which is `ROOT_URLCONF` itself (unnamespaced) — so every `{% url %}` name from earlier phases (`home`, `about`, `contact`, `projects`, `github`) kept resolving to the exact same paths with no template changes. `config/` no longer has a `urls.py` at all.

**Planned:** A `projects/urls.py`, once that app has real views to route to, `include()`d from `core/urls.py` (which will remain the actual `ROOT_URLCONF` — see `DECISIONS.md`).

## API Architecture

Not applicable. No API exists in the prototype, and none has been implemented for the planned production system.

## Data / Persistence

**Implemented:** Not applicable. The prototype has no database or persistence layer; all data is hardcoded in the script. The contact form does not send data anywhere — submitting it simulates success client-side only (the prototype explicitly tells the user "this is a prototype, so nothing was actually sent").

**Planned:** A relational database via Django's ORM. Engine: To be defined — PostgreSQL or MySQL, deliberately deferred until closer to a hosting decision (see `DECISIONS.md`). No schema/models exist yet.

## Authentication & Authorization

Not applicable. No auth exists in the prototype or in any implemented production code.

## External Integrations

**Implemented:** Google Fonts, loaded via `<link rel="preconnect">` and a stylesheet `<link>` in the document head. This is the only external dependency in the repository.

**Implemented (Phase 5, 2026-08-24):** GitHub's public REST API (`api.github.com/users/<username>`), called server-side from `core/views.py`'s `github` view via the `requests` library — real avatar/name/bio/repo/follower/following data rendered on `/github/`. Unauthenticated, so capped at 60 requests/hour per IP; no caching implemented (fine for current traffic — see `DECISIONS.md`).

**Planned:** No integration planned for LinkedIn or Email (no viable public API — see `DECISIONS.md`).

## Build & Runtime

**Implemented (prototype):** None. The file can be opened directly in a browser or served as a static file; there is no build step, package manager, or dev server.

**Implemented (Django, Phase 1):** `.venv/` (project-local virtual environment) + `requirements.txt` (currently: Django, asgiref, sqlparse, tzdata, pillow, requests + requests' transitive deps — see Technology Stack). Run via `manage.py runserver`.

**Implemented (Tailwind, Phase 2):** `npm install` (Node/npm toolchain, `package.json` + `node_modules/`, gitignored) then `npm run build:css` (one-shot, minified) or `npm run watch:css` (rebuild on change) to generate `static/css/main.css` from `static_src/css/input.css`. This build step must run (or `main.css` must already exist) before `runserver` will show a styled page — Django does not invoke it automatically.

**Planned:** React/JS build tooling — not yet set up.

## Architectural Boundaries

**Implemented (Phase 4, 2026-08-24):** The `core`/`projects` app split (see `DECISIONS.md`) is now real in code, not just decided in principle — `core` owns all current views/URLs/routing, `projects` exists as an empty, registered app awaiting its own models/views. Template/static layout stays global per the Phase 0 decision (unaffected by app boundaries). The prototype has no architectural boundaries beyond being a single file.

## Important Invariants

None established in code yet.
