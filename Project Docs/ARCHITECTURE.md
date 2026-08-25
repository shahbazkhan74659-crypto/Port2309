# Architecture

This describes the **actual current implementation** — the static prototype plus a Django project with Home, About, Contact, Blog, Resume, Hire Me, a real database-backed Projects app with a detail modal, a live-data GitHub page, and the `core`/`projects` apps carrying the owner's real content (Phases 1–5, 7–8) — followed by the **planned** production architecture beyond that. See `DECISIONS.md` for the reasoning behind the planned stack.

## System Overview

**Implemented:** The repository contains `prototype/index.html` (the standalone static mockup, unchanged — kept only as a styling/layout reference per `DECISIONS.md`) plus a from-scratch Django project: `manage.py` and a `config/` settings package (created via `django-admin startproject config .`) running inside a project-local `.venv` with Django 5.2.14 pinned in `requirements.txt` (Phase 1, 2026-08-24). Phases 2–3 (2026-08-24) added Home, About, Contact, and a static Projects list page, plus a GitHub page added just after Phase 3 — all styled by a Tailwind CSS build (npm + Tailwind CLI v4) reproducing the prototype's design tokens. As of Phase 4 (2026-08-24), routing/views moved out of `config/` into a real `core` app (`core/views.py`, `core/urls.py` — the latter is now `ROOT_URLCONF` directly), and a `projects` app is scaffolded and registered but intentionally empty (no models/views/urls yet). `config/` now holds only `settings.py`/`wsgi.py`/`asgi.py`. As of Phase 5 (2026-08-24), Home/About/Contact/base.html carry the owner's real content instead of generic placeholders, and `/github/` fetches real, live profile data from GitHub's public API server-side — the one deliberate exception was Home's featured-project card and the entire Projects page, left on Phase 3's mockup/placeholder content until the `projects` app gained real models. Phase 7 (2026-08-25) added placeholder Blog and a real-Skills-section Resume page. As of Phase 8 (2026-08-25), the `projects` app is no longer empty: a real `Project` model backs both the Projects list page and Home's featured-project card (seeded with 3 placeholder rows via a data migration — real content is still deferred, now to Phase 12), a vanilla-JS modal opens project details without a full page navigation, and a real `/projects/<slug>/` detail page exists as the no-JS/shareable-link fallback. `core` also gained its first model (`HireRequest`) backing a real, backend-processed `/hire/` form. The project's first-ever `manage.py migrate` ran as part of Phase 8 (SQLite, Django's default engine — the production engine choice is still Phase 10's job). No React tooling exists yet. Phase 9 (2026-08-25) polished the frontend and backend across 8 owner-confirmed items — see the "Implemented (Phase 9, 2026-08-25)" notes throughout this file and `DECISIONS.md`.

**Planned:** A Django server rendering HTML templates, styled with Tailwind CSS, with React mounted into specific DOM nodes ("islands") for interactive pieces. React tooling is not implemented yet — Phase 8's modal deliberately used vanilla JS instead (see `DECISIONS.md`).

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
- `python-dotenv` 1.1.0 (added Phase 9, 2026-08-25) — loads a gitignored `.env` file (tracked `.env.example` documents the expected keys) so `config/settings.py` can read `DJANGO_SECRET_KEY`/`DJANGO_DEBUG`/`DJANGO_ALLOWED_HOSTS` from the environment, with dev-safe defaults when `.env` is absent

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

**Implemented (Phase 7, 2026-08-25):** `core/views.py` gained `blog` and `resume` view functions (plain `render`, no context — same pattern as `about`/`contact`/`projects`), registered in `core/urls.py` as `path('blog/', ..., name='blog')` / `path('resume/', ..., name='resume')`. Both render new templates: `templates/pages/blog.html` (three hardcoded placeholder post entries) and `templates/pages/resume.html` (real Skills section + placeholder Experience/Education entries, "Download PDF" link pointing at `static/files/resume.pdf`, which does not exist on disk yet). No models. See `DECISIONS.md`.

**Implemented (Phase 8, 2026-08-25):** `projects` gained a real `Project` model, `projects/views.py` (`project_list`, `project_detail`), and `projects/urls.py` (`path('', project_list, name='projects')`, `path('<slug:slug>/', project_detail, name='project_detail')`) — `core/urls.py`'s `path('projects/', ...)` now `include()`s it, exactly as `DECISIONS.md`'s "`core.urls` as `ROOT_URLCONF`" entry anticipated. The old `core.views.projects` function was removed. `core/models.py` (new file — `core` had no models before this) holds `HireRequest`; `core/forms.py` (new file) holds `HireRequestForm`; `core/views.py` gained a `hire_me` view, routed at `path('hire/', ..., name='hire_me')` in `core/urls.py`. Both apps' models are registered in their respective `admin.py` (new files).

**Planned:** None remaining for `projects`' core CRUD surface — future work is data-only (Phase 12).

## Component Structure

**Implemented:** The prototype has no component framework. It uses plain JavaScript functions that build and return HTML strings, assembled into `#app`'s `innerHTML`:
- `renderNav`, `renderFooter` — shared chrome
- `renderHome`, `renderProjectsPage`, `renderProjectDetail`, `renderAbout`, `renderContact`, `renderNotFound` — page-level renderers
- `mockupFor` / `mockupBar` — decorative "browser chrome" project mockups (no real screenshots)
- `renderContactForm` / `renderSuccessPanel` / `wireContactForm` — client-side-only contact form and validation

**Implemented (Django, Phase 2):** `templates/base.html` defines the shared shell (nav header, `<main id="main">` content block, footer) via `{% block content %}`; `templates/pages/home.html` extends it. No template partials/includes yet — nav and footer are inlined directly in `base.html`, since it is itself the single shared shell.

**Implemented (Django, Phase 3):** `templates/pages/about.html`, `templates/pages/contact.html`, and `templates/pages/projects.html` also extend `base.html`, following the same pattern as Home. `base.html`'s nav/footer now render active-page state via `{% if request.resolver_match.url_name == '...' %}aria-current="page"{% endif %}` per link (the `.nav-link[aria-current="page"]` CSS existed since the Phase 2 port but was unused until now).

**Implemented (post-Phase 5 addition, 2026-08-24):** The nav/footer brand mark in `base.html` (`.nav-mark`/`.foot-mark`) now renders the owner's real "SK" badge image (`static/images/sk-badge.png`) instead of an auto-derived "S." text mark. See `DECISIONS.md` for the background-removal technique used to clean the source asset.

**Implemented (Phase 7, 2026-08-25):** `templates/pages/blog.html` and `templates/pages/resume.html` extend `base.html`, following the same `.page-head` pattern as About/Contact/Projects. `base.html`'s footer (`.foot-links`) gained a "Blog" link. `templates/pages/home.html`'s hero section gained a `.hero-resume-btn` linking to `/resume/`, positioned via CSS beside the hero portrait's left edge. Originally `.btn-ghost` styled (matching the rest of the site); restyled 2026-08-25 to a bespoke `.btn-neon` treatment (double-ring glowing green pill, matching an owner-supplied reference image) — see Data Flow/Routing below and `DECISIONS.md`.

**Implemented (Phase 8, 2026-08-25):** `templates/pages/projects.html` now loops `{% for project in projects %}` over the `.proj-entry` markup (one shared `.mockup` chip/line body per entry, instead of Phase 3's three bespoke hand-crafted mockup layouts, since content is now per-row) and renders a `<template id="modal-{{ project.slug }}">` per project plus a single shared `#project-modal-backdrop`/`#project-modal-panel` pair. `templates/pages/project_detail.html` (new) is a standalone single-project page reusing the same `.proj-*` classes. `templates/pages/hire.html` (new) follows the `.page-head` + `.contact-grid`/`.field`/`.submit-btn` pattern established by `contact.html`, rendering a Django `ModelForm` (`{{ form.name }}` etc.) instead of hand-written `<input>` markup. `base.html`'s nav/footer gained a "Hire Me" link (same `aria-current="page"` pattern as the other links). `home.html`'s featured-project block gained an `{% if featured %}...{% else %}...{% endif %}` split — the `{% else %}` branch keeps Phase 3's original hardcoded markup verbatim as a safe fallback if no `Project` is ever marked `featured`.

**Implemented (Phase 9, 2026-08-25):** Three new global error templates — `templates/404.html`, `500.html`, `403.html` — each `{% extends "base.html" %}` and reuse the existing `.page-head`/`.page-title`/`.page-sub`/`.eyebrow` classes, no new CSS. Django serves these automatically by filename whenever `DEBUG=False`; no `handler404`/`handler500`/`handler403` or `core/urls.py` changes were needed. `contact.html`/`hire.html` gained per-field error markup (`{% if form.<field>.errors %}<p id="{{ ... }}-error" class="field-error" role="alert">{{ ... }}</p>{% endif %}`, plus a `.form-errors` block for non-field errors) — previously an invalid submission silently re-rendered the form with no visible error. Both templates' contact-row `<a>` tags also had their repeated inline `style="display:flex;..."` replaced with a shared `.contact-row-link` CSS class.

**Planned:** Beyond the base shell, not yet defined — will depend on further Django template structure and which pieces become React islands.

## Data Flow

**Implemented:** All content is hardcoded in JavaScript objects/arrays at the top of the script — `PROFILE`, `SOCIALS`, `PROJECTS`, `NAV_ITEMS`. On load and on every `hashchange`, `render()` reads `window.location.hash`, picks a page renderer, and replaces `#app`'s `innerHTML` with `renderNav() + <main> + renderFooter()`. There is no data fetching, no API, and no persistence.

**Implemented (Django, Phase 2):** The Home page's content (name, tagline, roles, featured project, about snapshot, CTA copy) is hardcoded directly in `templates/pages/home.html` as generic placeholder text — not passed via view context, not model-backed. See `DECISIONS.md` for why (prototype content is fictional and must not be reused as real data; real content doesn't exist yet).

**Implemented (Django, Phase 3):** Same pattern for About, Contact, and Projects — all content is hardcoded directly in each template, not passed via view context. The Projects page's three entries are hardcoded markup, **not** a loop over a data structure or model — there is no `Project` model yet; each entry is a literal repeated block in `templates/pages/projects.html`. **Still true as of Phase 5** — this page and Home's featured-project card were deliberately excluded from the Phase 5 content swap (see `DECISIONS.md`) and remain exactly this way.

**Implemented (Django, Phase 5, 2026-08-24):** `base.html`, `home.html` (except the featured-project card), `about.html`, and `contact.html` now hold the owner's real hardcoded content (still not passed via view context — same "hardcoded in the template" pattern as before, just real text instead of generic placeholders). The GitHub page is the one exception to "hardcoded" — `core/views.py`'s `github` view now fetches live data server-side from `https://api.github.com/users/<username>` and passes it into the template context (`avatar_url`, `name`, `bio`, `public_repos`, `followers`, `following`, `html_url`), falling back to static real values on any request failure. See `DECISIONS.md` for both decisions.

**Implemented (post-Phase 5 addition, 2026-08-24):** The same `github` view also fetches the owner's repo list (`GET /users/<username>/repos?sort=updated`) and passes a `repos` list into the context; `templates/pages/github.html` renders it as a scrollable panel (`.repo-list`) beside the profile card, each entry linking out to its real GitHub URL. Falls back to an empty list (rendered as a small "not available right now" note) on request failure. See `DECISIONS.md`.

**Implemented (Phase 7, 2026-08-25):** `blog.html`'s three post entries and `resume.html`'s Experience/Education entries are hardcoded placeholder markup in their templates — not passed via view context, no model. `resume.html`'s Skills section is real content, copied verbatim from `about.html`'s existing skill data.

**Implemented (Phase 8, 2026-08-25):** `home.html`'s featured-project card and the entire Projects page are now model-backed — `projects/views.py`'s `project_list` passes `Project.objects.all()` (ordered by `Meta.ordering = ['order', '-year']`); `core/views.py`'s `home` passes `Project.objects.filter(featured=True).first()` as `featured`. Three placeholder `Project` rows (mirroring Phase 3's old hardcoded "Project One/Two/Three" text) were seeded via a `RunPython` data migration (`projects/migrations/0002_seed_placeholder_projects.py`), one flagged `featured=True` — real content swap is Phase 12's job, not this phase's; the seeded text is still explicitly placeholder-quality. `HireRequest` rows are the one piece of genuinely real, user-generated data in the project so far — created via `/hire/`'s POST handler, not seeded.

**Implemented (Phase 9, 2026-08-25):** `core/views.py`'s `github` view now checks Django's cache (`django.core.cache.cache`, the default `LocMemCache` — no `CACHES` setting was added, none was needed) before making either live GitHub API call, under two keys (`github_profile_<username>`, `github_repos_<username>`) with a 15-minute TTL. Only successful responses are cached; failure behavior (fall back to context defaults) is unchanged. `contact`/`hire_me` were also refactored to share one `_handle_lead_form(request, form_class, template_name)` helper in `core/views.py` (exact same POST/redirect/GET/`?sent=1` behavior as before, now written once) — see Application Structure/Important Invariants below for the precedent this sets for future lead-capture forms.

**Planned:** Real blog posts (likely a `Post` model), the view/URL logic to serve them, and real content are scheduled to Phase - X, "Blog Upgrade: Content, Logic, and Tables." Real resume experience/education content and the actual resume PDF file remain deferred — no phase scheduled yet. Real (non-placeholder) `Project` content is Phase 12, once the Phase 10 production database is in place.

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

**Implemented (Phase 7, 2026-08-25):** `path('blog/', ..., name='blog')` and `path('resume/', ..., name='resume')` added to `core/urls.py` alongside the existing routes. Footer's `{% url 'blog' %}` link and Home's `{% url 'resume' %}` hero button both resolve through these.

**Implemented (Phase 8, 2026-08-25):** `path('', project_list, name='projects')` and `path('<slug:slug>/', project_detail, name='project_detail')` in the new `projects/urls.py`, `include()`d from `core/urls.py` at `path('projects/', include('projects.urls'))` — the first real use of the `include()` layering `DECISIONS.md` anticipated, with `core.urls` still `ROOT_URLCONF` itself. `path('hire/', ..., name='hire_me')` added directly to `core/urls.py` (same flat pattern as `about`/`contact`). The Projects-list-page modal does not add any new server-side route — it operates entirely client-side on top of the existing `/projects/<slug>/` links (progressive enhancement, not a routing change).

**Planned:** None remaining for the app-boundary routing question this section originally tracked.

## API Architecture

Not applicable. No API exists in the prototype, and none has been implemented for the planned production system.

## Data / Persistence

**Implemented:** Not applicable. The prototype has no database or persistence layer; all data is hardcoded in the script. The contact form does not send data anywhere — submitting it simulates success client-side only (the prototype explicitly tells the user "this is a prototype, so nothing was actually sent").

**Implemented (Phase 8, 2026-08-25):** The project's first real database usage — `db.sqlite3` (Django's default engine, gitignored) via `manage.py migrate`, run for the first time this phase. Two models: `projects.Project` (list/detail/featured data, 3 placeholder rows seeded via data migration) and `core.HireRequest` (real user submissions from `/hire/`, created only via the form POST handler — never seeded). The Hire Me form is genuinely backend-processed: it validates via a Django `ModelForm` and persists to the database.

**Implemented (post-Phase 8 additions, 2026-08-25):** `core` gained two more models — `ContactRequest` (real Contact-page submissions) and `Resume` (an admin-uploaded PDF file via `FileField`, the project's first use of `MEDIA_ROOT`-backed file storage rather than a database row of plain fields). Neither is seeded; both are populated only by real user/owner action (a form submission, or an admin file upload).

**Implemented (post-Phase 8 addition, 2026-08-25):** `core.HeroContent` added — the Home hero section's portrait, greeting, hero lines, roles, three meta lines, and year/location are now admin-editable database fields instead of hardcoded template text. Unlike `ContactRequest`/`HireRequest`, this one **is** seeded (`core/migrations/0005_seed_hero_content.py`, text; `0006_backfill_hero_portrait.py`, the portrait image copied in from `static/images/hero-portrait.png`) with the exact real content Phase 5 had hardcoded, so it starts populated rather than empty. `core/views.py`'s `home` view passes `HeroContent.objects.first()` as `hero`; `home.html` reads every field as a bare `{{ hero.<field> }}` with **no template-level fallback text or fallback image** — the database is the single source of truth for this section (see `DECISIONS.md` for why this differs from `Resume`'s degrade-gracefully fallback pattern). `HeroContent` also gained a `statement` field (`core/migrations/0007_herocontent_statement.py`) holding Home's "Statement" section text — kept in this same table rather than a new one per the owner's direction. It then gained a `role` field (`primary`/`quote`, `core/migrations/0008_herocontent_role.py`) so a second row could hold the quote separately from the identity row (`core/migrations/0009_split_quote_row.py` created that second row) — `core/views.py`'s `home` view now queries the two roles independently (`hero` = `role="primary"`, `quote` = `role="quote"`), and `home.html`'s statement section reads `{{ quote.statement }}`. `HeroContentAdmin`'s list view shows a `role` column/filter so the two rows are distinguishable in `/admin/`.

**Implemented (post-Phase 8 addition, 2026-08-25):** The `role`/`statement` split on `HeroContent` described above was superseded the same day — `role` and `statement` were removed from `HeroContent` entirely, and a new, minimal `core.Quote` model (`statement`, `updated_at`) was added to hold the quote line on its own, registered separately in admin (`QuoteAdmin`). `core/views.py`'s `home` view now queries `HeroContent.objects.first()` and `Quote.objects.first()` independently rather than filtering one table by `role`. See `DECISIONS.md`'s "Quote split out of `HeroContent` into its own `Quote` model" entry for the full reasoning and migration details (`core/migrations/0010_quote.py`, `0011_migrate_quote_data.py`, `0012_remove_herocontent_role_statement.py`).

**Implemented (post-Phase 8 addition, 2026-08-25):** Home's "A LITTLE ABOUT ME" snapshot section is now model-backed too — `core.AboutSnapshot` (eyebrow, three headline words, headline sub-line, paragraph, and four "Currently: Building/Learning/Writing/Exploring" fields), registered in admin, seeded with the section's existing real content via `core/migrations/0013_aboutsnapshot.py`/`0014_seed_about_snapshot.py`. `core/views.py`'s `home` view passes `AboutSnapshot.objects.first()` as `about_snapshot`; `home.html`'s snapshot section reads every field as `{{ about_snapshot.<field> }}`, no fallback. See `DECISIONS.md`.

**Implemented (post-Phase 8 addition, 2026-08-25):** The contact email is now model-backed too — `core.ContactEmail` (`email`, `updated_at`), admin-registered, seeded via `core/migrations/0016_contactemail.py`/`0017_seed_contact_email.py`. Unlike the other content models, it's wired in via a new Django context processor (`core/context_processors.py::contact_email`, registered in `config/settings.py`) rather than per-view queries — this is the project's first context processor, and it injects `contact_email` into every template's context automatically. `templates/pages/home.html`, `contact.html`, and `hire.html` all read `{{ contact_email.email }}` instead of a hardcoded address. See `DECISIONS.md`.

**Implemented (post-Phase 8 addition, 2026-08-25):** The whole About page is now model-backed — `core.About` (one row covering all five page sections: page head, Background/What-I-care-about, Philosophy, Skills & Tools, Where this is going), admin-registered, seeded via `core/migrations/0018_about.py`/`0019_seed_about.py`. The three skill-tag groups reuse `projects.Project`'s `tags`-CharField-plus-`tag_list()`-method pattern (`languages`/`frameworks`/`learning` fields, `languages_list()`/`frameworks_list()`/`learning_list()` methods). `core/views.py`'s `about` view now passes `About.objects.first()` as `about`; `about.html` reads every field via `{{ about.<field> }}`, no fallback. See `DECISIONS.md`.

**Implemented (post-Phase 8 addition, 2026-08-25):** `core.ContactEmail` gained `github_display`/`linkedin_display` fields (the visible domain-style strings shown on Contact/Hire Me's GitHub/LinkedIn rows) — added via `core/migrations/0020_contactemail_links.py`/`0021_seed_contact_links.py`. `templates/pages/contact.html`'s rows now render these fields as their text while keeping their `href`s unchanged; `templates/pages/hire.html` gained matching GitHub/LinkedIn rows (previously had none). See `DECISIONS.md`.

**Implemented (post-Phase 8 addition, 2026-08-25):** `core.ContactEmail` gained `available_for_label`/`available_for` and `stack_label`/`stack` fields (Hire Me's "Available for"/"Stack" rows, both label and value) — added via `core/migrations/0022_contactemail_hire_fields.py`/`0023_seed_contact_hire_fields.py`. `templates/pages/hire.html`'s rows now render these fields, no hardcoded text remains. See `DECISIONS.md`.

**Implemented (post-Phase 8 addition, 2026-08-25):** `core.ContactRequest` (name, email, message, submitted_at) added, mirroring `HireRequest`. `core/views.py`'s `contact` view now follows the same POST/redirect/GET pattern as `hire_me` — the Contact page's form is now genuinely backend-processed too (previously plain, non-submitting HTML), reversing the earlier "Contact gets no further scheduled work" call. See `DECISIONS.md`.

**Implemented (post-Phase 8 addition, 2026-08-25):** `core.Resume` (`file` — `FileField(upload_to="resume/")` — plus `uploaded_at`) added, admin-uploadable. `config/settings.py` gained `MEDIA_URL`/`MEDIA_ROOT`; `core/urls.py` serves `MEDIA_ROOT` via Django's `static()` helper when `DEBUG=True`. `core/views.py`'s `resume` view passes the latest `Resume`'s file URL as `resume_url`; `templates/pages/resume.html`'s "Download PDF" button uses it when present, falling back to the original `static/files/resume.pdf` link (Phase 7's placeholder path) when no `Resume` row exists yet. This is the project's first `FileField`/media-upload usage. See `DECISIONS.md`.

**Planned:** A relational database via Django's ORM for production. Engine: To be defined — PostgreSQL or MySQL, deliberately deferred until closer to a hosting decision (see `DECISIONS.md`, `PHASES.md`'s Phase 10). SQLite is a development-only stand-in, not a production choice.

## Authentication & Authorization

Not applicable. No auth exists in the prototype or in any implemented production code.

## External Integrations

**Implemented:** Google Fonts, loaded via `<link rel="preconnect">` and a stylesheet `<link>` in the document head. This is the only external dependency in the repository.

**Implemented (Phase 5, 2026-08-24):** GitHub's public REST API (`api.github.com/users/<username>`), called server-side from `core/views.py`'s `github` view via the `requests` library — real avatar/name/bio/repo/follower/following data rendered on `/github/`. Unauthenticated, so capped at 60 requests/hour per IP. **As of Phase 9 (2026-08-25), responses are cached for 15 minutes** (Django's default `LocMemCache`) — see Data Flow above and `DECISIONS.md`.

**Planned:** No integration planned for LinkedIn or Email (no viable public API — see `DECISIONS.md`).

## Build & Runtime

**Implemented (prototype):** None. The file can be opened directly in a browser or served as a static file; there is no build step, package manager, or dev server.

**Implemented (Django, Phase 1):** `.venv/` (project-local virtual environment) + `requirements.txt` (currently: Django, asgiref, sqlparse, tzdata, pillow, requests + requests' transitive deps — see Technology Stack). Run via `manage.py runserver`.

**Implemented (Phase 9, 2026-08-25):** `config/settings.py` now calls `load_dotenv(BASE_DIR / '.env')` (via `python-dotenv`) before reading `SECRET_KEY`/`DEBUG`/`ALLOWED_HOSTS` from `os.environ`, each with a dev-safe default matching the pre-Phase-9 hardcoded values — so `runserver` behaves identically with no `.env` present. A tracked `.env.example` documents the three keys (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`); the real `.env` stays gitignored (already excluded before this phase).

**Implemented (Tailwind, Phase 2):** `npm install` (Node/npm toolchain, `package.json` + `node_modules/`, gitignored) then `npm run build:css` (one-shot, minified) or `npm run watch:css` (rebuild on change) to generate `static/css/main.css` from `static_src/css/input.css`. This build step must run (or `main.css` must already exist) before `runserver` will show a styled page — Django does not invoke it automatically.

**Planned:** React/JS build tooling — not yet set up.

## Architectural Boundaries

**Implemented (Phase 4, 2026-08-24):** The `core`/`projects` app split (see `DECISIONS.md`) is now real in code, not just decided in principle — `core` owns all current views/URLs/routing, `projects` exists as an empty, registered app awaiting its own models/views. Template/static layout stays global per the Phase 0 decision (unaffected by app boundaries). The prototype has no architectural boundaries beyond being a single file.

**Implemented (Phase 8, 2026-08-25):** The `core`/`projects` boundary is now exercised for real: `projects` owns the `Project` model and its own `views.py`/`urls.py`/`admin.py`, `include()`d from `core.urls` rather than defined inside `core`. `HireRequest` (Hire Me) lives in `core`, per the `DECISIONS.md` feature-placement decision — `core` continues to own identity/site-wide features while `projects` stays scoped strictly to projects/works/code, exactly as that decision specified.

## Important Invariants

- `core.urls` is `ROOT_URLCONF` — there is no `config/urls.py`. Any new app's routes must be `include()`d from `core/urls.py`, following the `projects.urls` precedent (Phase 8), not added as a project-level `urls.py`.
- `Project.featured` should have at most one `True` row at a time — `core.views.home` uses `.first()`, so a second `featured=True` row would silently be ignored rather than erroring; there is no database-level constraint enforcing this.
- `core.context_processors.contact_email` (registered in `config/settings.py`) runs on every template render project-wide — any new page that needs the contact email just references `{{ contact_email.email }}`, no view change needed. Keep site-wide, cross-view data like this in a context processor rather than duplicating a query across views, following this precedent.
- Django's default `LocMemCache` (used by `core.views.github`'s Phase 9 caching, no explicit `CACHES` setting) is per-process, in-memory, and not shared across multiple worker processes — fine at this app's current traffic/single-process scale, but would need a shared backend (e.g. Redis/Memcached) if the site ever runs multiple production workers.
- `config/settings.py` reads `SECRET_KEY`/`DEBUG`/`ALLOWED_HOSTS` from `os.environ` (via `python-dotenv`'s `.env` loading, Phase 9) with dev-safe defaults matching the pre-Phase-9 hardcoded values — a fresh checkout with no `.env` behaves identically to before Phase 9. Any new setting that needs to differ between dev and production should follow this same pattern rather than being hardcoded.
- `core._handle_lead_form(request, form_class, template_name)` (Phase 9) is the shared POST/redirect/GET helper behind `contact`/`hire_me` — any future lead-capture form (same "render form, save on valid POST, redirect to `?sent=1`" shape) should reuse or extend this helper rather than duplicating the pattern again.
