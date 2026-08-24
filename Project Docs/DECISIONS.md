# Technical Decisions

These decisions were made during a prior planning discussion, before any production code was written. They are recorded here as established direction for `ARCHITECTURE.md` and `PHASES.md`. Where original reasoning was not captured at the time, this is marked explicitly rather than guessed.

## Decision: Production stack — Django + Django templates + Tailwind CSS + React islands

- Status: Accepted
- Date: 2026-08-19
- Context: The project needed a technology stack for the production portfolio site, chosen before any implementation began.
- Decision: Python Django with Django templates for server-rendered pages, styled with Tailwind CSS, with React mounted into specific DOM nodes ("islands") via plain JS/bundled script for interactive pieces — not a full single-page React application.
- Reasoning: To be defined. (Not captured in the planning record; only the chosen stack is known.)
- Consequences: Production implementation has not yet started, so no consequences have been observed. Note that the existing visual prototype (`prototype/index.html`) does not use this stack — it is a separate, framework-free artifact. See "Standalone static prototype" decision below.

## Decision: Three Django apps — `core`, `contents`, `hiring`

- Status: Accepted
- Date: 2026-08-19
- Context: The site's feature set (Projects, Designs, Blog, Resume, Timeline, Hire Me, home/nav, search) needed to be organized into Django apps.
- Decision: Exactly three apps:
  - `core` — home/nav views + urls, and search bar logic
  - `contents` — Projects, Designs, Blog, Resume, and a vertical Timeline (college → now), as separate models within one app
  - `hiring` — the "Hire Me" feature logic
- Reasoning: To be defined beyond the boundary itself. (One nuance is recorded — see "Designs kept removable" below — but the broader rationale for exactly this three-way split was not captured.)
- Consequences: Not yet implemented. `PHASES.md` / `TASKS.md` should be updated once Django scaffolding begins to confirm the boundaries hold in practice.

## Decision: Global `templates/` and `static/` directories, not per-app

- Status: Accepted
- Date: 2026-08-19
- Context: Django supports both a per-app `templates/`/`static/` layout and a single global layout at the project root. Per-app namespacing was initially considered.
- Decision: One global `templates/` folder and one global `static/` folder at the project root.
- Reasoning: The project owner was explicit about preferring this after initially considering per-app namespacing. The detailed rationale beyond stated preference: To be defined.
- Consequences: Do not re-suggest per-app template/static namespacing for this project.

## Decision: Designs feature kept removable via feature flag

- Status: Accepted
- Date: 2026-08-19
- Context: The Designs feature may be dropped from the site in the future, unlike Projects, Blog, Resume, and Timeline.
- Decision: Implement Designs as its own model with a feature flag gating its URLs, nav entry, and search visibility, kept isolated so it can be removed without disturbing Projects, Blog, Resume, or Timeline.
- Reasoning: Anticipated possibility that Designs will be cut; isolating it avoids entangling its removal with unrelated features.
- Consequences: When `contents` app is implemented, Designs-related code should stay isolated from the other content models per this decision.

## Decision: Build a standalone static visual prototype before production implementation

- Status: Accepted (observed via existing code)
- Date: Unknown exact date; file present in the repository as of 2026-08-23.
- Context: `prototype/index.html` exists as a single, self-contained, framework-free HTML/CSS/JS file implementing a client-side hash-routed mockup (Home, Projects list/detail, About, Contact) with placeholder persona ("Renzo Malik") and placeholder project content — built independently of the planned Django + Tailwind + React stack.
- Observed implementation: See `ARCHITECTURE.md` for full technical detail.
- Original reasoning: To be defined. (No record explains why a standalone vanilla-JS prototype was chosen over prototyping directly within the planned Django + Tailwind stack, or what this prototype is meant to become — e.g. a design reference to port into templates, versus a throwaway mockup.)
- Consequences: The prototype's relationship to the production build is currently unconfirmed — see `TASKS.md` and `PHASES.md`. This should be clarified with the project owner before Phase 3 (production scaffolding) begins.
