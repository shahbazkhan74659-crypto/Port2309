# Current Tasks

## Active

To be defined. No task is currently confirmed as actively in progress.

## Next

To be defined. The next concrete step depends on direction from the project owner — in particular, whether/how the [Phase 2] prototype (`prototype/index.html`) should inform or be ported into the planned Django + Tailwind + React build, and when to begin [Phase 3] production scaffolding. Do not begin Django scaffolding without explicit confirmation from the owner (see `CLAUDE.md`).

Deferred, to revisit once a hosting provider is chosen: pick PostgreSQL vs MySQL as the production database engine (see `DECISIONS.md`).

## Blocked

None.

## Completed

- [x] [Phase 1] Define feature set (Projects, Designs, Blog, Resume, About, Contact, Skills, GitHub links, Timeline, Hire Me)
- [x] [Phase 1] Choose production stack: Django + Django templates + Tailwind CSS + React/JS
- [x] [Phase 1] Define Django app boundaries: `core`, `contents`, `hiring`
- [x] [Phase 1] Decide on global `templates/` and `static/` directories at project root (not per-app)
- [x] [Phase 1] Confirm relational database as the persistence layer (Postgres vs MySQL deferred until a hosting decision) — 2026-08-24
- [x] [Phase 2] Build static visual prototype (`prototype/index.html`) covering Home, Projects list/detail, About, and Contact pages
- [x] Initialize git repo, commit, and push to `origin` (`Port2309`, branch `main`) — 2026-08-24
