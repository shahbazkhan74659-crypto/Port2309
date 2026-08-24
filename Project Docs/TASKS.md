# Current Tasks

## Active

To be defined. No task is currently confirmed as actively in progress.

## Next

To be defined. The full roadmap (Phase 0–12, see `PHASES.md`) is now named, starting with [Phase 1] "Project Setup and Django Rocket Page", but detailed task breakdowns for each phase have not yet been given by the project owner. Do not begin Django scaffolding without explicit confirmation from the owner (see `CLAUDE.md`). Build from scratch on the confirmed stack — use `prototype/index.html` only as a styling/layout reference, not as code to port (see `DECISIONS.md`).

Open question: Blog, Resume, Timeline, and Hire Me are now scheduled ([Phase 7], [Phase 8]), but which of the two apps (`core`/`projects`) each lives in — or whether they need app(s) of their own — is still unstated. **Designs is the one originally-planned feature with no phase yet at all.** Ask when these are actually implemented, or when Designs next comes up (see `DECISIONS.md`).

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
