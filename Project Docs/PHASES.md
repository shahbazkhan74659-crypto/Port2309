# Development Phases

The project owner has not established a full, explicit phase structure. Only the stages below are evidenced by prior planning discussion and the current state of the repository. Do not invent additional phases beyond what is listed here — see `CLAUDE.md` rule 3.

## Phase 1 — Planning & Definition

### Objective
Define the feature set, technology stack, and application boundaries before writing production code.

### Scope
Requirements gathering, stack selection, Django app boundary decisions, template/static directory layout decisions.

### Completion Criteria
- Feature set defined (see `PROJECT.md`)
- Stack chosen: Django + Django templates + Tailwind CSS + React islands (see `DECISIONS.md`)
- App boundaries defined: `core`, `contents`, `hiring` (see `DECISIONS.md`)
- Global `templates/` and `static/` directory structure decided (see `DECISIONS.md`)

**Status: Complete**, as evidenced by the decisions recorded in `DECISIONS.md`.

## Phase 2 — Visual / UX Prototyping

### Objective
Explore visual design, layout, and page structure before production implementation.

### Scope
A standalone, framework-free HTML/CSS/JS mockup (`prototype/index.html`) covering Home, Projects (list + detail), About, and Contact, using placeholder persona and content.

### Completion Criteria
To be defined. (No explicit criteria — e.g. design sign-off — has been established by the project owner for when this phase is considered done.)

**Status: In progress** — the prototype exists but its relationship to the production build (e.g. whether it will be ported into Django templates/Tailwind, or replaced) has not been confirmed by the owner. See `TASKS.md`.

## Phase 3 and beyond

To be defined.

No production implementation (Django project scaffolding, models, React islands, deployment) has been started, and no explicit roadmap for it has been given by the project owner. Per `CLAUDE.md`, production scaffolding should not begin until the owner explicitly requests it.
