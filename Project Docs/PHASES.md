# Development Phases

The project owner has defined the full build roadmap, Phase 0 through Phase 14 (originally confirmed 2026-08-24 as the complete set through Phase 12 — no further phases expected at the time; the owner then added a new Phase 11, "Seeding real Projects," on 2026-08-25, pushing the former Phase 11 "Full End-to-End Testing" to Phase 12 and the former Phase 12 "Deployment and Hosting" to Phase 13; the owner then added a second new Phase 11, "Custom Admin Hub," also on 2026-08-25, pushing "Seeding Real Projects" to Phase 12, "Full End-to-End Testing" to Phase 13, and "Deployment and Hosting" to Phase 14 — see `DECISIONS.md`; the owner then inserted a further phase, **Phase - X — Blog Upgrade: Content, Logic, and Tables**, after Phase 10 and before Phase 11 on 2026-08-25 — deliberately given a non-numeric "X" label instead of a renumbering, per the owner's explicit instruction not to renumber Phases 11–14, so it sits in roadmap order without a sequence number; the owner then inserted **Phase Y — Project Page Upgrade: Logic and Content-Ready Interface** right after Phase - X, also 2026-08-25, using the same non-numeric-label convention so Phases 11–14 stayed unchanged again — see `DECISIONS.md`). The earlier planning and prototyping work is recorded below as **Phase 0 — Pre-Development**, an unnumbered stage that precedes the numbered build roadmap (owner's explicit choice, 2026-08-24, to restart numbering from Phase 1 rather than continue the old Phase 1/2 sequence). Do not invent additional phases beyond what is listed here — see `CLAUDE.md` rule 3.

## Phase 0 — Pre-Development (Planning & Prototyping)

### Objective
Define the feature set, technology stack, and application boundaries, and explore visual design, before writing any production code.

### Scope

**0a. Planning & Definition**
Requirements gathering, stack selection, Django app boundary decisions, template/static directory layout decisions.

- Feature set defined (see `PROJECT.md`)
- Stack chosen: Django + Django templates + Tailwind CSS + React/JS + relational database (see `DECISIONS.md`)
- App boundaries defined at the time: `core`, `contents`, `hiring` — later superseded 2026-08-24 by a simpler two-app plan (`core`, `projects`); see `DECISIONS.md`
- Global `templates/` and `static/` directory structure decided (see `DECISIONS.md`)

**Status: Complete**, as evidenced by the decisions recorded in `DECISIONS.md`.

**0b. Visual / UX Prototyping**
A standalone, framework-free HTML/CSS/JS mockup (`prototype/index.html`) covering Home, Projects (list + detail), About, and Contact, using placeholder persona and content. Confirmed (2026-08-24, see `DECISIONS.md`) to serve as a styling/design-and-layout reference only — it will not be ported into or reused as production code.

**Status: Complete.** The existing `prototype/index.html` is sufficient — owner confirmed (2026-08-24) no further prototyping is needed before moving on.

### Completion Criteria
- 0a: Complete (see above).
- 0b: Complete — `prototype/index.html` exists and serves as the styling/design reference; owner confirmed 2026-08-24 that this satisfies the phase.

**Phase 0 overall status: Complete.**

## Phase 1 — Project Setup and Django Rocket Page

### Objective
Initialize the Django project from scratch (per Phase 0 stack decisions and the "prototype is a reference only" decision — no code ported from `prototype/index.html`) and confirm the setup works by getting Django's default landing page ("rocket" success page) running locally.

### Scope
To be defined in further detail by the project owner. Implied by the phase name: creating the Django project and confirming `runserver` serves Django's default success page.

### Completion Criteria
Running the Django dev server (`runserver`) shows Django's default success page (the "rocket" page) with no errors.

**Status: Complete.** Verified 2026-08-24 — `manage.py check` reported no issues, and `runserver` served the rocket page (HTTP 200) at `http://127.0.0.1:8000/`. See `ARCHITECTURE.md` for the resulting project structure.

## Phase 2 — Static Global Base Structure and a Home Page

### Objective
Establish the site's global, reusable structure — the base Django template(s), global `templates/`/`static/` layout (per the Phase 0 decision), and Tailwind CSS setup that every page will build on — and implement the Home page against it.

### Scope
A global `templates/base.html` (nav/footer chrome) and `templates/pages/home.html`, styled via Tailwind CSS (npm + Tailwind CLI v4, CSS-first `@theme` config), reproducing `prototype/index.html`'s exact design tokens and markup structure for the nav, hero, featured project, statement, about-snapshot, and CTA sections. Routed directly via `config/views.py` + `config/urls.py` (no Django app yet — `core`/`projects` are Phase 4). Content uses generic placeholders (not the prototype's fictional persona), per owner direction — see `DECISIONS.md`.

### Completion Criteria
`manage.py runserver` serves the Home page at `/` with no errors, styled via the Tailwind-built stylesheet, visually matching `prototype/index.html`'s theme and structure (placeholder content aside).

**Status: Complete.** Verified 2026-08-24 — `manage.py check` reported no issues; `/` returns HTTP 200 with the expected structural classes (`nav`, `hero-line`, `feat-title`, `cta-title`, `foot`); `/static/css/main.css` builds via `npm run build:css` and serves HTTP 200. See `ARCHITECTURE.md`.

## Phase 3 — Other Static Pages

### Objective
Build out the remaining static (non-dynamic/no-models-yet) pages on top of the Phase 2 global base structure.

### Scope
About, Contact, and a static Projects list page, built from scratch on top of the Phase 2 global base structure — using `prototype/index.html` only as a styling/layout reference, per `DECISIONS.md`. Routed directly via `config/views.py` + `config/urls.py`, same as Home (still no `core`/`projects` apps — those are Phase 4). All three pages use hardcoded, generic placeholder content (`DECISIONS.md`'s "Generic placeholder content for pre-content-model pages" decision) rather than the prototype's persona/project data. The Projects page is a **static, hardcoded list only** — no per-project detail pages or slugs (those depend on the real `projects` app/model, Phase 4) and its data is not model-backed; it will be superseded by the real listing once Phase 4 lands. The Contact page ships as static markup only — no client-side validation or simulated-submit JS (deferred to Phase 5/8).

Nav and footer links in `base.html`, and the internal Home page links that target these pages, were updated from `href="#"` placeholders to real routes, including `aria-current="page"` active-state marking on the nav (CSS for this existed since the Phase 2 port but was unused until now).

### Completion Criteria
`manage.py runserver` serves `/about/`, `/contact/`, and `/projects/` at HTTP 200 inside the shared `base.html` shell, styled via the Tailwind-built stylesheet, visually matching `prototype/index.html`'s theme (placeholder content aside). Nav/footer links to these pages work and show the active-page state; Home's "more about me", "get in touch", and featured-project links resolve to the real pages instead of `#`.

**Status: Complete.** Verified 2026-08-24 — `manage.py check` reported no issues; `/`, `/about/`, `/contact/`, and `/projects/` all return HTTP 200; `aria-current="page"` confirmed present on the correct nav link per page; new CSS classes (`.proj-entry`, `.contact-grid`, `.skill-tag`, etc.) confirmed present in the built `static/css/main.css`. Visual confirmation in-browser was not performed this session (browser automation was unavailable) — the project owner should give it a visual pass. See `ARCHITECTURE.md`.

## Phase 4 — Apps: `core`, `projects`

### Objective
Scaffold the two Django apps that carry the site's dynamic functionality: `core` (views, URLs, and the site's main routing; identity, etc.) and `projects` (handling the owner's projects, works, and code).

### Scope
Scaffold both apps via `manage.py startapp`, register them in `INSTALLED_APPS`, and move all routing out of `config/` into `core` — `core/views.py` and `core/urls.py` take over everything that had been living in `config/views.py`/`config/urls.py` since Phase 2 (per `DECISIONS.md`'s "Phase 2/3 static pages routed directly via config/" decision, which explicitly anticipated this move). `core/urls.py` becomes the project's `ROOT_URLCONF` directly (see `DECISIONS.md`'s "`core.urls` as `ROOT_URLCONF`" decision) — `config/` is reduced to `settings.py`/`wsgi.py`/`asgi.py` only, no `urls.py`, no `views.py`. `projects` is scaffolded and registered but left fully empty (default `startapp` stub, no views/urls/models) — this phase also formally supersedes the earlier three-app plan (`core`/`contents`/`hiring`) — see `DECISIONS.md`. Designs, Blog, Resume, Timeline, and Hire Me are resolved to live in `core` (see `DECISIONS.md`), though building them out is not part of this phase's stated scope.

### Completion Criteria
`manage.py check` reports no issues; every existing route (`/`, `/about/`, `/contact/`, `/projects/`, `/github/`, `/admin/`) still resolves identically through `core.urls`, with zero template changes required (url names are unnamespaced). `config/` contains only `__init__.py`, `settings.py`, `wsgi.py`, `asgi.py`.

**Status: Complete.** Verified 2026-08-24 — `manage.py check` clean; all six routes return their expected status codes (five pages 200, `/admin/` 302 to login); nav `{% url %}` resolution and `aria-current="page"` active-state marking confirmed still correct after the swap. See `ARCHITECTURE.md`, `DECISIONS.md`.

## Phase 5 — Replace Placeholder Content With Real Content

### Objective
Owner-defined scope (2026-08-24), superseding this phase's original speculative description (real navigation/animation — that direction was never confirmed and did not happen): replace the generic placeholder identity/bio/contact copy from Phases 2–3 with the owner's real content, and give the GitHub page (`/github/`) live data instead of a placeholder card.

### Scope
Real content replaced site-wide: identity (name, brand mark, role, location) in `base.html`/`home.html`; Home's hero/about-snapshot/statement/CTA copy; the full About page (background, "what I care about", philosophy, skills, closing paragraph); Contact page's email/GitHub/LinkedIn rows. `/github/` now calls GitHub's public REST API server-side (`core/views.py`, new `requests` dependency) for real avatar/name/bio/repo/follower/following data, with a static fallback if the call fails. Explicitly **excluded** by owner direction: the hero portrait photo (already real, untouched) and Home's featured-project card plus the entire Projects page (`templates/pages/projects.html`) — both stay on mockup/placeholder content, to be replaced once the real `projects` app/model exists (Phase 4 apps are scaffolded but still empty — see `ARCHITECTURE.md`).

### Completion Criteria
Every in-scope page renders real content with no leftover generic placeholder strings (`[FIRST]`, `you@example.com`, `yourusername`, "Placeholder ..."); `/github/` shows live-fetched profile data; Projects page and Home's featured project remain untouched placeholder content by design.

**Status: Complete.** Verified 2026-08-24 — `manage.py check` clean; all pages visually confirmed in-browser with real content (name, role, location, bio, skills, philosophy, contact links); `/github/` confirmed showing live avatar/bio/stats fetched from `api.github.com`; only remaining "placeholder" string on the site is intentionally on Home's featured-project card. See `ARCHITECTURE.md`, `DECISIONS.md`.

**Note:** The site brand mark deferral is now resolved (2026-08-24, post-Phase 5) — the nav/footer "S." auto-derived default was swapped for the owner's real "SK" badge image (background-removed, cleaned). See `DECISIONS.md`.

## Phase 6 — Connecting Pages to the Apps, and Modals

### Objective
Wire the static/dynamic pages built so far up to real data from the `core`/`projects` Django apps (see `DECISIONS.md`), and add modal UI.

### Scope
To be defined in further detail by the project owner. Implied by the phase name: pages driven by app views/models instead of static placeholder content, plus modal components (e.g. project detail modals) — likely where React/JS islands (see `DECISIONS.md`) get used, though not confirmed for this phase specifically.

### Completion Criteria
To be defined.

**Status: Superseded — merged into Phase 8.** Owner's call, 2026-08-24. This phase was briefly put on hold (no confirmed need for modal UI existed yet), then its scope was folded into a redefined Phase 8 rather than resumed separately — see `DECISIONS.md`'s "Timeline cut from the roadmap; Phase 6 merged into a redefined Phase 8" decision. The objective/scope above is kept as a historical record of what this phase originally covered; the actual work now happens under Phase 8. Work continues with Phase 7 next.

## Phase 7 — Blog and Resume

### Objective
Build the Blog and Resume features.

### Scope
Owner-defined scope (2026-08-25): a static placeholder `/blog/` page (`templates/pages/blog.html`), mirroring Phase 3's placeholder Projects page pattern — three hardcoded placeholder post entries, no `Post` model yet. A styled `/resume/` page (`templates/pages/resume.html`) with a real Skills section (reusing the About page's real skill data) plus placeholder Experience/Education entries, and a "Download PDF" action wired to a static file path (`static/files/resume.pdf`) that the owner will populate later. Both routed via `core/views.py`/`core/urls.py`, same pattern as `about`/`contact`/`projects`. Also in scope: a footer "Blog" link (`templates/base.html`), and a "See My Resume" button on the Home page's hero section, positioned beside the left edge of the hero portrait image, linking to `/resume/`. See `DECISIONS.md`.

### Completion Criteria
`manage.py runserver` serves `/blog/` and `/resume/` at HTTP 200 inside the shared `base.html` shell, styled via the Tailwind-built stylesheet; footer shows a working "Blog" link; Home's hero section shows a "See My Resume" button linking to `/resume/`, positioned beside the hero portrait.

**Status: Complete**, for this settled scope. Verified 2026-08-25 — `manage.py check` clean; `/`, `/blog/`, `/resume/` all return HTTP 200; footer "Blog" link and Home's "See My Resume" button confirmed in-browser. Real blog posts (model-backed), real resume experience/education content, and the actual resume PDF file are deliberately deferred — not an oversight, same pattern as Phase 3's placeholder Projects page. See `DECISIONS.md`.

## Phase 8 — Projects App: Modal & Mechanism, and Hire Me

### Objective
Redefined 2026-08-24 (owner's direction, see `DECISIONS.md`), superseding this phase's original scope (Vertical Growth Timeline, Contact, and Hire Me — Timeline is cut from the roadmap entirely, Contact is considered already covered by the real Contact page/info shipped in Phases 3/5). Build the real `projects` app — a `Project` model replacing the Phase 3/5 mockup content on the Projects page and Home's featured-project card — with a modal-based mechanism for viewing project details, and build the "Hire Me" feature. This absorbs the held/superseded Phase 6's "connect pages to real data + modal UI" scope.

### Scope
Owner-defined scope, settled 2026-08-25 (see `DECISIONS.md`): a real `Project` model (`title`, `slug`, `short_description`, `tags`, `category`, `role`, `year`, `status`, `github_url`, `live_url`, `order`, `featured`) in the `projects` app, with `project_list`/`project_detail` views and `projects/urls.py` `include()`d from `core/urls.py` at `/projects/`. The Projects list page and Home's featured-project card are now driven by real `Project` rows instead of Phase 3/5's hardcoded mockup markup. A vanilla-JS/CSS modal (no React) on the Projects list page opens a project's details without a full page navigation, backed by a real `/projects/<slug>/` detail page as the no-JS/shareable-link fallback. Three placeholder `Project` rows (mirroring the old hardcoded mockup text) were seeded via a data migration so the feature is testable now — real content stays deferred to Phase 11, per the existing "don't fabricate real content" convention. "Hire Me" was built in `core` (per `DECISIONS.md`) as a dedicated `/hire/` page with a real, backend-processed form: a `HireRequest` model + `HireRequestForm`, saved on submit (POST/redirect/GET), reviewable via Django admin — no email integration, since none exists elsewhere in the project. Nav/footer both gained a "Hire Me" link. Designs remains the one originally-planned feature with no phase yet — when scheduled, it also belongs in `core`.

### Completion Criteria
`manage.py check` and `migrate` run clean; `/projects/` lists the seeded `Project` rows and its "EXPLORE PROJECT"/mockup links open a working modal (closable via Escape, backdrop click, or the close button) without navigating away; `/projects/<slug>/` loads each project's standalone detail page directly; `/` renders the `featured` `Project`'s real data in place of the old hardcoded featured-project card; `/hire/` renders a form that, on valid submission, saves a `HireRequest` and shows a success state, with submissions visible in `/admin/`; nav/footer show a working "Hire Me" link with correct active-page state.

**Status: Complete.** Verified 2026-08-25 — `manage.py check` clean; migrations applied (`projects.0001_initial`, `projects.0002_seed_placeholder_projects`, `core.0001_initial`); `/`, `/projects/`, `/projects/project-one/`, `/hire/` all return HTTP 200 and `/admin/` 302 (login redirect, as expected); Home's featured-project card confirmed showing the seeded "Project One" row; a real Hire Me submission was posted via `curl` (CSRF-protected), confirmed saved in the database, then removed (test data, not a real lead). Browser-based interactive verification (clicking the modal open/close) was not performed this session — the Chrome extension was unavailable — confirmed instead via direct HTTP checks of the rendered HTML/JS. See `ARCHITECTURE.md`, `DECISIONS.md`.

## Phase 9 — Finishing and Polishing the Frontend and Backend

### Objective
Finish and polish the site across both frontend and backend, following the feature-building phases (0–8).

### Scope
To be defined in further detail by the project owner.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 10 — Database: MySQL/PostgreSQL/sqlite

### Objective
Choose and set up the production relational database engine — PostgreSQL or MySQL — resolving the deferral recorded in `DECISIONS.md` (deliberately left open until closer to a hosting decision).

### Scope
To be defined in further detail by the project owner. Implied by the phase name and its placement after the feature-building/polish phases: moving from whatever local database was used during development onto the chosen production engine.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase - X — Blog Upgrade: Content, Logic, and Tables

### Objective
Upgrade the Blog page from Phase 7's static placeholder into a fully ready feature — real content, real logic, and real database tables backing it, rather than the three hardcoded placeholder post entries it has shipped with since Phase 7.

### Scope
To be defined in further detail by the project owner. Implied by the phase name: a real `Post`-style model/table (replacing "no model yet"), the view/URL logic to list and display posts from it, and the owner's real blog content replacing the Phase 7 placeholder entries.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase Y — Project Page Upgrade: Logic and Content-Ready Interface

### Objective
Upgrade the Projects page's logic and interface into a fully content-ready state, building further on Phase 8's `Project` model/list/detail/modal mechanism.

### Scope
To be defined in further detail by the project owner. Implied by the phase name and its placement after Phase - X and before Phase 11: further logic and interface work on the existing `projects` app (model/views/modal shipped in Phase 8) so the page is fully ready to present real content — distinct from Phase 12 "Seeding Real Projects," which populates the data itself rather than the page's logic/interface.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 11 — Custom Admin Hub

### Objective
Build a custom, central, user-friendly CRUD hub for the whole site — a single admin-facing surface for managing all of the site's content, rather than relying solely on Django's default `/admin/`.

### Scope
To be defined in further detail by the project owner. Implied by the phase name and its placement in the roadmap: by this point the site's content is spread across nine models (`core.HeroContent`, `Quote`, `AboutSnapshot`, `About`, `ContactEmail`, `Resume`, `ContactRequest`, `HireRequest`, plus `projects.Project`), currently manageable only through Django's default admin interface — this phase would build a more central, friendlier CRUD experience for managing all of it. Exact design (customized Django admin, a bespoke dashboard, or something else) not yet decided.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 12 — Seeding Real Projects

### Objective
Populate the Projects listing with the owner's real project data, replacing the Phase 3/5 placeholder content once the real `Project` model (Phase 8) and production database (Phase 10) both exist.

### Scope
To be defined in further detail by the project owner. Implied by the phase name and its placement after Phase 8 (`projects` app gains a real `Project` model, list/detail views, and a modal mechanism) and Phase 10 (production database engine chosen and set up): creating real `Project` model instances for the owner's actual projects/works — the data itself, not the model or views (those are Phase 8's scope) — replacing the Projects page and Home's featured-project card, which have stayed on Phase 3/5 mockup/placeholder content up to this point (see `DECISIONS.md`).

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 13 — Full End-to-End Testing (Component/Unit + E2E)

### Objective
Full test coverage across frontend, backend, and database: component/unit tests plus end-to-end tests.

### Scope
To be defined in further detail by the project owner. Implied by the phase name: unit/component-level tests (e.g. Django test framework for backend, a JS testing tool for React islands) and end-to-end tests exercising the whole stack, including the Phase 10 production database. No testing framework/tooling has been chosen yet.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 14 — Deployment and Hosting

### Objective
Deploy and host the finished site.

### Scope
To be defined in further detail by the project owner. Implied by the phase name and its placement after Phase 10 (database engine, chosen "closer to a hosting decision" per `DECISIONS.md`) and Phase 13 (testing): choosing a hosting provider and deploying the completed, tested site. No hosting provider has been chosen yet.

### Completion Criteria
To be defined.

**Status: Not started.**

Phase 14 is the last *numbered* phase in the roadmap — the project owner does not expect further phases beyond this (originally confirmed 2026-08-24 for what was then Phase 12; four additional phases were inserted later, all 2026-08-25: Phase 11 "Seeding Real Projects" (later renumbered to Phase 12), Phase 11 "Custom Admin Hub", and the non-numeric **Phase - X** "Blog Upgrade: Content, Logic, and Tables" and **Phase Y** "Project Page Upgrade: Logic and Content-Ready Interface" — see the note at the top of this file). Phase - X and Phase Y sit after Phase 10 and before Phase 11 in build order (in that sequence — X then Y) despite their labels not being part of the numeric sequence. If new phases are identified later, add them here rather than assuming the roadmap is fixed forever.
