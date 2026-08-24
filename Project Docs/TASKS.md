# Current Tasks

## Active

To be defined. No task is currently confirmed as actively in progress. [Phase 1]–[Phase 5] are now complete (see Completed below); a [Phase 6] task breakdown has not yet been given by the project owner.

## Next

To be defined. The full roadmap (Phase 0–12, see `PHASES.md`) is now named. [Phase 1]–[Phase 5] are complete; detailed task breakdowns for [Phase 6] onward have not yet been given by the project owner. Build from scratch on the confirmed stack — use `prototype/index.html` only as a styling/layout reference, not as code to port (see `DECISIONS.md`).

Deferred, explicitly (owner's choice): swap the site brand mark (nav/footer "S.") for the owner's custom badge image ("SK Badge.png") — the owner asked to be consulted again before this is added, so ask before doing it. See `DECISIONS.md`'s Phase 5 content-swap decision.

Deferred, explicitly (owner's choice, Phase 5): Home's featured-project card and the entire Projects page stay on Phase 3's mockup/placeholder content until the `projects` app gains real models — not an oversight.

Resolved 2026-08-24: Designs, Blog, Resume, Timeline, and Hire Me all live in the `core` app; `projects` is scoped strictly to the owner's projects/works/code. **Designs still has no phase assigned yet** — when it's scheduled, it belongs in `core` per this decision. See `DECISIONS.md`.

Deferred to [Phase 10] "Database: MySQL/PostgreSQL", once a hosting provider is chosen: pick PostgreSQL vs MySQL as the production database engine (see `DECISIONS.md`).

## Blocked

None.

## Completed

- [x] [Phase 0a] Define feature set (Projects, Designs, Blog, Resume, About, Contact, Skills, GitHub links, Timeline, Hire Me)
- [x] [Phase 0a] Choose production stack: Django + Django templates + Tailwind CSS + React/JS
- [x] [Phase 0a] Define Django app boundaries: `core`, `contents`, `hiring` (superseded 2026-08-24 — see next entry)
- [x] [Phase 0a] Decide on global `templates/` and `static/` directories at project root (not per-app)
- [x] [Phase 0a] Confirm relational database as the persistence layer (Postgres vs MySQL deferred until a hosting decision) — 2026-08-24
- [x] [Phase 0b] Build static visual prototype (`prototype/index.html`) covering Home, Projects list/detail, About, and Contact pages
- [x] Initialize git repo, commit, and push to `origin` (`Port2309`, branch `main`) — 2026-08-24
- [x] Confirm prototype is a styling/design reference only; production build starts from scratch — 2026-08-24
- [x] Establish full build roadmap, Phase 0 (pre-development, done) through Phase 12 "Deployment and Hosting" — confirmed complete, no further phases expected — 2026-08-24 (see `PHASES.md`)
- [x] Simplify Django app boundaries to two apps (`core`, `projects`), superseding the earlier `core`/`contents`/`hiring` plan — 2026-08-24
- [x] [Phase 1] Initialize Django project from scratch (`manage.py` + `config/` package at repo root, `.venv`, `requirements.txt`) and verify `runserver` shows the default rocket page with no errors — 2026-08-24 (see `ARCHITECTURE.md`)
- [x] [Phase 2] Build global base template (`templates/base.html`) and Home page (`templates/pages/home.html`), wire up Tailwind CSS via npm + Tailwind CLI, matching `prototype/index.html`'s theme/structure with generic placeholder content — 2026-08-24 (see `ARCHITECTURE.md`, `DECISIONS.md`)
- [x] Add real hero portrait image to Home page (`static/images/hero-portrait.png`); added Pillow as a dependency for image processing (background removal) — 2026-08-24 (see `ARCHITECTURE.md`)
- [x] [Phase 3] Build About, Contact, and a static Projects list page (`templates/pages/{about,contact,projects}.html`), routed via `config/views.py`/`config/urls.py`; ported the matching CSS from `prototype/index.html` into `static_src/css/input.css`; wired nav/footer + Home's internal links to the real routes with active-page (`aria-current="page"`) marking — 2026-08-24 (see `ARCHITECTURE.md`, `PHASES.md`)
- [x] Add a placeholder GitHub profile page (`/github/`, `templates/pages/github.html`, new `.profile-card` CSS) — no live API fetch yet; trimmed LinkedIn/Email from the site footer (LinkedIn/Email stay plain outbound links elsewhere, no custom UI) — 2026-08-24, ad-hoc addition, not a numbered phase (see `DECISIONS.md`)
- [x] Clean up an AI-generated GitHub logo (background removed to transparent, watermark stripped, edges cleaned) and place it on the GitHub page's header (`static/images/github-logo.png`) — 2026-08-24, verified in-browser
- [x] [Phase 4] Scaffold `core`/`projects` apps via `manage.py startapp`; moved all views/routing out of `config/` into `core` (`core/views.py`, `core/urls.py` — now `ROOT_URLCONF`); `config/` reduced to `settings.py`/`wsgi.py`/`asgi.py` only; `projects` registered but left empty — 2026-08-24 (see `ARCHITECTURE.md`, `DECISIONS.md`, `PHASES.md`)
- [x] [Phase 5] Replaced placeholder content with the owner's real content site-wide (identity, Home hero/about-snapshot/statement/CTA, About page, Contact links) — 2026-08-24; explicitly excluded Home's featured-project card and the Projects page (owner's choice, stay on Phase 3 mockup content) and the site brand mark badge swap (deferred, owner wants to be asked first) — see `PHASES.md`, `DECISIONS.md`
- [x] [Phase 5] Wired `/github/` up to GitHub's public REST API for live avatar/name/bio/repo/follower/following data, with a static-real-values fallback on request failure; added `requests` to `requirements.txt` — 2026-08-24, verified in-browser (see `DECISIONS.md`, `ARCHITECTURE.md`) — this closes out the previously-open "wire the GitHub page up" item
- [x] Added a scrollable real-repository list to the GitHub page (`.repo-list`, beside the profile card), fetched live from GitHub's repos API, each entry linking out to the real repo — 2026-08-24, ad-hoc addition, verified in-browser (see `DECISIONS.md`, `ARCHITECTURE.md`)
