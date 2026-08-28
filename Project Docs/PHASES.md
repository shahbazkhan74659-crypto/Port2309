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
Owner-confirmed scope (2026-08-25), selected from a candidate list surveyed against the actual codebase (see `DECISIONS.md`); SEO/meta items — favicon, Open Graph tags, robots.txt — were surveyed but explicitly excluded from this phase.

**Frontend:**
1. Accessibility fixes — descriptive hero portrait alt text (`templates/pages/home.html`), inline `style=` attributes on Contact/Hire Me row links replaced with a shared CSS class.
2. Responsive/mobile gaps — the GitHub page's `.profile-card`/`.repo-list` fixed-height panels relaxed under the existing 900px breakpoint instead of double-stacking on mobile.
3. Visible form validation errors — Contact and Hire Me forms currently re-render silently on an invalid submission with no error shown; add visible, accessible (`role="alert"`, `aria-invalid`, `aria-describedby`) error output.
4. Smooth scrolling behaviour — `scroll-behavior: smooth` site-wide, respecting the existing `prefers-reduced-motion` override.

**Backend:**
5. Custom error pages — `404.html`/`500.html`/`403.html`, replacing Django's default debug-style pages once `DEBUG=False`.
6. Production-safety settings — `SECRET_KEY`/`DEBUG`/`ALLOWED_HOSTS` moved from hardcoded values to environment variables (via `python-dotenv`), with dev-safe defaults.
7. GitHub API caching — the `/github/` view's two live API calls cached (Django's default `LocMemCache`, 15-minute TTL) to reduce redundant requests and rate-limit risk.
8. View code de-duplication — Contact and Hire Me views' near-identical POST/redirect/GET logic factored into one shared helper.

### Completion Criteria
`manage.py check` runs clean; Contact/Hire Me forms show visible errors on invalid submission and unchanged `?sent=1` success behavior on valid submission; `/github/` page's mobile layout no longer double-stacks fixed-height panels under 900px; `404.html`/`500.html`/`403.html` render without error and are used automatically once `DEBUG=False`; `SECRET_KEY`/`DEBUG`/`ALLOWED_HOSTS` are read from environment variables with working dev-safe defaults; `/github/` serves cached data on repeat loads within the cache TTL; `contact`/`hire_me` views share one helper function.

**Status: Complete.** Verified 2026-08-25 — `manage.py check` clean; Contact/Hire Me forms confirmed showing visible, accessible errors (`role="alert"`, `aria-invalid`) on invalid submission via direct POST, and unchanged `?sent=1` redirect/success behavior on valid submission; the GitHub-page caching change was verified directly against the view function (cache miss on first call populates the cache, a monkeypatched `requests.get` spy confirmed zero live API calls on a second call within the TTL); the custom 404 page was confirmed live in-browser-equivalent (`curl`) under a temporarily real `DEBUG=False`/`ALLOWED_HOSTS` `.env`, returning HTTP 404 with the styled template and working static assets, then `.env` was removed to restore dev defaults; `404.html`/`500.html`/`403.html` all dry-run rendered without error via `get_template(...).render()`. The responsive/mobile CSS fix and the `.contact-row-link`/error-styling CSS were verified by code review and a successful `npm run build:css`, not by a live browser viewport check (no browser automation tool was used this session). See `ARCHITECTURE.md`, `DECISIONS.md`.

## Phase 10 — Database: MySQL/PostgreSQL/sqlite

### Objective
Choose and set up the production relational database engine — PostgreSQL or MySQL — resolving the deferral recorded in `DECISIONS.md` (deliberately left open until closer to a hosting decision).

### Scope
Owner-decided 2026-08-26 (see `DECISIONS.md`): the production database engine is **PostgreSQL**. Narrowed the same day — this phase now covers choosing and connecting that engine only; the actual hosting deployment (Render + UptimeRobot, originally scoped here) was moved to **Phase 14**, which already exists in the roadmap for deployment/hosting. `config/settings.py` reads a `DATABASE_URL` environment variable to configure Postgres (via the `psycopg` driver), falling back to SQLite when unset. Two Postgres targets exist: a **Neon** free-tier project (the eventual Phase 14 production target) and a **local PostgreSQL 18 install** (this machine's day-to-day development database, replacing SQLite for local dev) — both have been migrated and verified working.

### Completion Criteria
`config/settings.py` reads `DATABASE_URL` and connects to PostgreSQL when set (SQLite remains the fallback for a fresh checkout with no `.env`); `manage.py migrate` runs clean against both the local Postgres install and Neon; a superuser exists on both.

**Status: Complete**, for this narrowed scope. Verified 2026-08-26 — `psycopg`/`psycopg-binary` added to `requirements.txt`; `manage.py migrate` ran clean against a new Neon project and separately against a locally-created `portfolio` database/role on the local PostgreSQL 18 service; superusers created on both; the dev server verified serving real/seeded content (`/`, `/projects/`) from each in turn. Render deployment and the UptimeRobot keep-alive ping are **not** part of this phase anymore — see Phase 14 below and `DECISIONS.md`.

## Phase - X — Blog Upgrade: Content, Logic, and Tables

### Objective
Upgrade the Blog page from Phase 7's static placeholder into a fully ready feature — real content, real logic, and real database tables backing it, rather than the three hardcoded placeholder post entries it has shipped with since Phase 7.

### Scope
Owner-directed 2026-08-26 (see `DECISIONS.md`'s "Blog `Post`/`Tag` relocated to `projects`..." entry): a real `Post` model (`title`, `slug`, `short_description`, `content`, `tags`, `published_at`) — placed in the `projects` app rather than `core` (an explicit override of the standing Designs/Blog/Resume/Timeline/Hire-Me → `core` placement decision, Blog only). Tags are a real, shared `Tag` model (`ManyToManyField`, not a comma-separated string), reused across `Post`, `Project`, and `core.About`'s skill fields — the new `Post` table enforces a 1–6 tag count via a custom admin form. `blog_list`/`blog_detail` views and `projects/blog_urls.py` (`include()`d from `core.urls` at `/blog/`, `blog` url name preserved for the footer link, `blog_detail` new); `templates/pages/blog.html` converted from three hardcoded entries to a `{% for post in posts %}` loop; a new `templates/pages/blog_detail.html` standalone page (no modal). One placeholder `Post` was seeded via a data migration (mirroring `Project`'s Phase 8 seeding pattern) — real blog content is **not** part of this scope, same "structure now, real writing later" deferral Phase 7 already established.

### Completion Criteria
`manage.py check`/`migrate` run clean; `/blog/` lists the seeded `Post`(s) with working tag chips and a "READ POST" link; `/blog/post-title-one/` renders the full post body; an unknown slug 404s; the footer's `blog` link still resolves with no template changes; `/admin/projects/post/add/` rejects 0 tags (Django's default required-field validation) and more than 6 tags (custom `clean_tags()`), accepting 1–6.

**Status: Complete.** Model/logic/tables layer verified 2026-08-26 (`manage.py check` clean, `makemigrations --check` clean against the final model state, all routes/status codes verified via `runserver`, admin tag-count validation exercised via a test client for the 0/3/7-tag cases). Real content landed the same day — a data migration (`projects/migrations/0009_seed_real_first_post.py`) removed the placeholder `Post`/its placeholder `Tag` rows (now-orphaned, deleted) and seeded one genuine post, "Building This Portfolio" (slug `building-this-portfolio`), the real story of this site's own build — tagged `Django`/`Python`/`Tailwind CSS`/`Relational DB` (existing real `Tag` rows, reused rather than duplicated). Verified via `manage.py migrate` (clean), a shell check confirming the placeholder post/tags are gone and the real post/tags are present, and `runserver` requests confirming `/blog/`, `/blog/building-this-portfolio/` return 200 and `/blog/post-title-one/` now 404s. Further posts can be added anytime going forward — this phase's objective (real content, logic, and tables all in place) is met with the one post; volume isn't a completion requirement.

## Phase Y — Project Page Upgrade: Logic and Content-Ready Interface

### Objective
Upgrade the Projects page's logic and interface into a fully content-ready state, building further on Phase 8's `Project` model/list/detail/modal mechanism.

### Scope
Owner-confirmed scope (2026-08-27, via direct questions — see `DECISIONS.md`): real project screenshots (`projects.ProjectImage`, a gallery model FK'd to `Project`, used as both the list-card's primary image and the detail page's full gallery — falls back to the existing decorative `.mockup` chip when a project has no images), a new `Project.description` long-form field for the detail page's fuller explanation (distinct from the existing 200-char `short_description` used on cards/Home), and category/tag filtering + free-text search + pagination on `/projects/` (all GET-param driven, AND-combinable, bookmarkable). Cleanup: `Project.tags` now enforces the same 1–6 count validation `Post.tags` already had (`ProjectAdminForm.clean_tags()`); Home's hardcoded featured-project placeholder fallback (`{% else %}` branch — "Project Name", generic "Tag" chips) was removed entirely, following the no-template-fallback convention already established by `HeroContent`/`Quote`/`AboutSnapshot`. The detail page's GitHub/Live-URL display logic was already correct (independent `{% if %}` guards) and needed no change.

### Completion Criteria
`manage.py check`/`makemigrations --check` run clean; `/projects/` supports `?category=`, `?tag=`, `?q=`, and `?page=`, individually and combined, with an out-of-range page clamping instead of erroring and a "No projects match your filters." message on zero results; a project with uploaded `ProjectImage` rows shows its real screenshot on its list card, in the modal, and in a gallery on `/projects/<slug>/`; a project with none falls back to the `.mockup` chip everywhere; `/admin/projects/project/<id>/change/` has a working image-gallery inline and rejects 0 or >6 tags; `/` shows the featured project's real data with no fallback branch when `featured` is unset.

**Status: Complete.** Verified 2026-08-27 — `manage.py check` and `makemigrations --check` both clean after generating and applying `projects/migrations/0010_project_description_projectimage.py`; all routes (`/`, `/projects/`, filter/search/pagination combinations including `?page=999`, `/projects/<slug>/`, an unknown slug) returned expected status codes via `runserver`; a real test image was uploaded to a seeded `Project` via the ORM, confirmed rendering on the list card, in the modal, on the detail-page gallery, and on Home's featured card (then removed as test data, confirming the `.mockup` fallback returns cleanly); `ProjectAdminForm.clean_tags()` confirmed rejecting 0 and 7 tags via a direct form test; the admin inline's formset fields (`images-0-image` etc.) confirmed present on the `Project` change page via an authenticated test-client request. See `ARCHITECTURE.md`, `DECISIONS.md`.

## Phase 11 — Custom Admin Hub

### Objective
Build a custom, central, user-friendly CRUD hub for the whole site — a single admin-facing surface for managing all of the site's content, rather than relying solely on Django's default `/admin/`.

### Scope
Owner-confirmed scope (2026-08-28, via direct questions — see `DECISIONS.md`): a new `adminhub` Django app, mounted at `/adminhub/`, with its own `templates/adminhub/` directory — visually cloning seven public pages (Home, Projects, About, Contact, Hire Me, Blog, Resume) using the exact same section markup/CSS classes as their public counterparts, with small Edit/Delete/Add affordances layered on top of the seeded content. Gated by a custom, site-styled login page (`/adminhub/login/`, Django's existing session auth, staff-only) rather than Django's default `/admin/login/` — `/admin/` itself is untouched. Public lead-capture forms (Contact/Hire Me) are deliberately NOT reproduced in the hub — a `.hub-notice` placeholder card sits in their place, with a "Recent Submissions" list (`ContactRequest`/`HireRequest`, with delete) below it instead. Singleton "settings" models (`HeroContent`, `Quote`, `AboutSnapshot`, `About`, `ContactEmail`) get Edit + Delete only; multi-row content (`Project` + `ProjectImage`, `Post`) gets full Add/Edit/Delete. Resume — previously only its PDF file was model-backed — was upgraded to be fully editable too: three new `core` models (`ResumePage`, `ResumeExperience`, `ResumeEducation`) replace the page's hardcoded Skills/Experience/Education markup, seeded via migration with the exact pre-existing placeholder content. Tags (shared `projects.Tag`) are managed inline within the Project/Post/About/ResumePage edit forms via a checkbox picker plus a same-page "quick add" box that creates a new `Tag` without leaving the form or losing other in-progress field values — no new JS, pure server-rendered PRG. The existing 1–6 tag-count validation (`Post`/`Project`) is duplicated into the hub's own forms and additionally extended to `About`'s and the new `ResumePage`'s tag fields for consistency.

### Completion Criteria
`manage.py check`/`makemigrations --check` run clean; anonymous and non-staff requests to any `/adminhub/...` URL redirect to the custom login page, while the existing staff superuser reaches all 7 hub pages; `/admin/` and every public page/URL are functionally unaffected; creating/editing/deleting a `Project` (with images and tags, including a quick-added tag) and a `Post` through the hub is reflected immediately on the corresponding public page; editing or deleting a singleton (e.g. `HeroContent`, `Quote`) reflects immediately on `/`, with deletion leaving the section blank and no server error; a real Contact/Hire Me submission appears in both the hub's submissions list and Django's default `/admin/` (same table), and deleting it via the hub removes it from both.

**Status: Complete.** Verified 2026-08-28 — `manage.py check` and `makemigrations --check` both clean; the new `core` migrations (`0027_resumeeducation_resumeexperience_resumepage.py`, `0028_seed_resume_page.py`) applied cleanly and the public `/resume/` page renders identically to its pre-migration hardcoded version, now fully database-sourced; anonymous and a temporary non-staff test account were both confirmed redirected to `/adminhub/login/`, while the real superuser reached all 7 hub pages (200); `/admin/` and every public route confirmed unaffected. Full CRUD cycles exercised via Django's test client: a `Project` created with a formset-managed image and a quick-added tag (confirmed rendering on `/projects/<slug>/`), then edited and deleted (cascade-deleting its image); a `Post` created/verified on `/blog/<slug>/`/deleted; `HeroContent` edited with the new text confirmed live on `/`, then restored; `Quote` deleted with `/` confirmed still rendering (blank statement, no 500); a `ResumeExperience` row added, confirmed on `/resume/`, then deleted; a real `/contact/` submission confirmed appearing in the hub's submissions list and removable from there (verified gone from the shared `ContactRequest` table). Tag-count validation confirmed matching the existing `Post`/`Project` admin behavior (0 tags hits Django's own "required" check first, exactly as the pre-existing admin forms already do; 7+ tags triggers the custom "Select at most 6 tags (you selected 7)." message). One implementation pitfall found and fixed during verification: `ProjectImage.order`'s model-level `default=0` was leaking into the inline formset's empty "add another image" row as a non-`None` initial value, causing Django's formset "skip this untouched extra row" check to misfire and reject an image-less save — fixed by declaring `order` explicitly on a dedicated `ProjectImageForm` (bypassing the model-default-as-initial behavior) rather than relying on the auto-generated formset field. Live in-browser visual verification was not performed this session (the Chrome extension was unavailable) — confirmed instead via direct HTTP/test-client checks of the rendered HTML. See `ARCHITECTURE.md`, `DECISIONS.md`.

## Phase 12 — Seeding Real Projects

### Objective
Populate the Projects listing with the owner's real project data, replacing the Phase 3/5 placeholder content once the real `Project` model (Phase 8) and production database (Phase 10) both exist.

### Scope
To be defined in further detail by the project owner. Implied by the phase name and its placement after Phase 8 (`projects` app gains a real `Project` model, list/detail views, and a modal mechanism) and Phase 10 (production database engine chosen and set up): creating real `Project` model instances for the owner's actual projects/works — the data itself, not the model or views (those are Phase 8's scope) — replacing the Projects page and Home's featured-project card, which have stayed on Phase 3/5 mockup/placeholder content up to this point (see `DECISIONS.md`).

**Partially started ad hoc, 2026-08-27** (same pattern as Phase - X's real first blog post, written ahead of that phase's full completion): the first real project, "TS Library," was seeded via `projects/migrations/0011_seed_real_first_project.py`, which deleted all 3 Phase 3/5 placeholder `Project` rows outright (owner's explicit choice) rather than adding alongside them. TS Library has no screenshots yet — it renders via the `.mockup` fallback Phase Y built until real images are uploaded. Remaining Phase 12 work: more real projects, and screenshots for this one.

### Completion Criteria
To be defined.

**Status: Not started** as a formally scoped phase, but its core task (real project data replacing placeholders) has begun — see above.

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
Hosting provider now chosen (moved here from Phase 10, 2026-08-26 — see `DECISIONS.md`): deploy the Django app on **Render**'s free tier, pointed at the existing **Neon** PostgreSQL project (already migrated and verified as of Phase 10), with a free **UptimeRobot** monitor pinging the live URL to prevent Render's free-tier idle spin-down/cold-start. Interim arrangement — once the owner has an international debit/credit card, the plan is to migrate to **Oracle Cloud**'s Always Free tier instead (a real always-on VM, no PaaS cold-start concern). Detailed deployment steps (Render service config, environment variables, static/media file serving in production) still to be worked out when this phase actually starts.

### Completion Criteria
The app is deployed and reachable on Render, connected to the Neon PostgreSQL database; an UptimeRobot monitor is actively pinging the live URL frequently enough to prevent idle spin-down.

**Status: Not started.**

Phase 14 is the last *numbered* phase in the roadmap — the project owner does not expect further phases beyond this (originally confirmed 2026-08-24 for what was then Phase 12; four additional phases were inserted later, all 2026-08-25: Phase 11 "Seeding Real Projects" (later renumbered to Phase 12), Phase 11 "Custom Admin Hub", and the non-numeric **Phase - X** "Blog Upgrade: Content, Logic, and Tables" and **Phase Y** "Project Page Upgrade: Logic and Content-Ready Interface" — see the note at the top of this file). Phase - X and Phase Y sit after Phase 10 and before Phase 11 in build order (in that sequence — X then Y) despite their labels not being part of the numeric sequence. If new phases are identified later, add them here rather than assuming the roadmap is fixed forever.
