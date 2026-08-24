# Technical Decisions

These decisions were made during a prior planning discussion, before any production code was written. They are recorded here as established direction for `ARCHITECTURE.md` and `PHASES.md`. Where original reasoning was not captured at the time, this is marked explicitly rather than guessed.

## Decision: Production stack — Django + Django templates + Tailwind CSS + React/JS + relational database

- Status: Accepted
- Date: 2026-08-19 (initial stack decision); reconfirmed and extended 2026-08-24 (database layer added)
- Context: The project needed a technology stack for the production portfolio site, chosen before any implementation began. The 2026-08-19 decision covered the application/rendering layer but did not name a persistence layer; the owner confirmed the full stack including the database on 2026-08-24.
- Decision: Python Django with Django templates for server-rendered pages, styled with Tailwind CSS, with React + JavaScript for interactive pieces (per the 2026-08-19 discussion, mounted as islands into specific DOM nodes rather than a full single-page application), backed by a relational database — either PostgreSQL or MySQL. The owner explicitly deferred choosing between Postgres and MySQL until closer to a hosting decision (see below); the stack is also explicitly open to adding further tools as needed rather than being considered closed.
- Reasoning: To be defined for the app/rendering layer (not captured in the original planning record). For the DB engine specifically: deferred on purpose because Django's ORM makes switching low-cost early on, so the choice is better tied to the eventual hosting provider.
- Consequences: Production implementation has not yet started, so no consequences have been observed. `ARCHITECTURE.md`'s planned data/persistence section marks the DB engine as "To be defined — Postgres or MySQL." Note that the existing visual prototype (`prototype/index.html`) does not use this stack — it is a separate, framework-free artifact. See "Standalone static prototype" decision below.

## Decision: Three Django apps — `core`, `contents`, `hiring`

- Status: **Superseded** (2026-08-24) — see "Two Django apps — `core`, `projects`" below.
- Date: 2026-08-19
- Context: The site's feature set (Projects, Designs, Blog, Resume, Timeline, Hire Me, home/nav, search) needed to be organized into Django apps.
- Decision: Exactly three apps:
  - `core` — home/nav views + urls, and search bar logic
  - `contents` — Projects, Designs, Blog, Resume, and a vertical Timeline (college → now), as separate models within one app
  - `hiring` — the "Hire Me" feature logic
- Reasoning: To be defined beyond the boundary itself. (One nuance is recorded — see "Designs kept removable" below — but the broader rationale for exactly this three-way split was not captured.)
- Consequences: Never implemented, so nothing needs unwinding in code. Superseded by the owner's explicit simplification to two apps.

## Decision: Two Django apps — `core`, `projects`

- Status: Accepted
- Date: 2026-08-24
- Context: While naming Phase 4 of the roadmap, the owner explicitly discarded the earlier three-app plan (`core`/`contents`/`hiring`) in favor of a simpler two-app structure.
- Decision: Exactly two apps:
  - `core` — views, URLs, and the main routing of the site; identity (e.g. About/home identity content), etc.
  - `projects` — the owner's projects, works, and code — replaces the "Projects" portion of the old `contents` app.
- Reasoning: Owner's explicit direction: "forget those three apps we decided back then... only two apps... that's enough."
- Consequences: **Open question** — where Designs, Blog, Resume, Timeline, and the "Hire Me" feature (previously slated for `contents`/`hiring`) now live is unresolved: whether they fold into `core` or `projects`, become their own app(s) later, or are dropped from scope has not been stated. Do not assume; ask the owner when one of those features comes up in a phase. See `TASKS.md`. The "Designs kept removable via feature flag" decision below also needs revisiting once this is resolved, since it was written against the now-superseded `contents` app.

## Decision: Global `templates/` and `static/` directories, not per-app

- Status: Accepted
- Date: 2026-08-19
- Context: Django supports both a per-app `templates/`/`static/` layout and a single global layout at the project root. Per-app namespacing was initially considered.
- Decision: One global `templates/` folder and one global `static/` folder at the project root.
- Reasoning: The project owner was explicit about preferring this after initially considering per-app namespacing. The detailed rationale beyond stated preference: To be defined.
- Consequences: Do not re-suggest per-app template/static namespacing for this project.

## Decision: Designs feature kept removable via feature flag

- Status: Accepted in principle, but **app placement pending** (2026-08-24) — see the `core`/`projects` decision above.
- Date: 2026-08-19
- Context: The Designs feature may be dropped from the site in the future, unlike Projects, Blog, Resume, and Timeline.
- Decision: Implement Designs as its own model with a feature flag gating its URLs, nav entry, and search visibility, kept isolated so it can be removed without disturbing Projects, Blog, Resume, or Timeline.
- Reasoning: Anticipated possibility that Designs will be cut; isolating it avoids entangling its removal with unrelated features.
- Consequences: The isolation principle (own model + feature flag) still stands, but it originally assumed a `contents` app that no longer exists in the plan. Which app Designs now belongs to is unresolved — see the open question in the `core`/`projects` decision above.

## Decision: Build a standalone static visual prototype before production implementation

- Status: Accepted (observed via existing code)
- Date: Unknown exact date; file present in the repository as of 2026-08-23.
- Context: `prototype/index.html` exists as a single, self-contained, framework-free HTML/CSS/JS file implementing a client-side hash-routed mockup (Home, Projects list/detail, About, Contact) with placeholder persona ("Renzo Malik") and placeholder project content — built independently of the planned Django + Tailwind + React stack.
- Observed implementation: See `ARCHITECTURE.md` for full technical detail.
- Original reasoning: To be defined. (No record explains why a standalone vanilla-JS prototype was chosen over prototyping directly within the planned Django + Tailwind stack.)
- Consequences: None outstanding — see the "Prototype is a styling/design reference only" decision below, which resolves how it relates to the production build.

## Decision: Prototype is a styling/design reference only — production build starts from scratch

- Status: Accepted
- Date: 2026-08-24
- Context: The relationship between `prototype/index.html` and the planned Django + Tailwind + React production build was previously unconfirmed (see decision above).
- Decision: The prototype is not to be ported, reused, or built upon as code. Production implementation will be built from scratch on the confirmed stack (Django + Django templates + Tailwind CSS + React/JS + relational database). The prototype's HTML/CSS is retained only as a visual/styling and layout-structure reference to consult while building the real templates and components.
- Reasoning: Owner's explicit direction.
- Consequences: Do not treat `prototype/index.html` as a source to copy code from during production scaffolding (Phase 3) — reimplement the design intent in Django templates/Tailwind/React rather than lifting its vanilla-JS routing/rendering approach. Its placeholder persona ("Renzo Malik") and placeholder project content are not real content and must not carry over either. See `PHASES.md` and `TASKS.md`.
