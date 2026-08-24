# Development Phases

The project owner has not established a full, explicit phase structure. Only the stages below are evidenced by prior planning discussion and the current state of the repository. Do not invent additional phases beyond what is listed here — see `CLAUDE.md` rule 3.

## Phase 1 — Planning & Definition

### Objective
Define the feature set, technology stack, and application boundaries before writing production code.

### Scope
Requirements gathering, stack selection, Django app boundary decisions, template/static directory layout decisions.

### Completion Criteria
- Feature set defined (see `PROJECT.md`)
- Stack chosen: Django + Django templates + Tailwind CSS + React/JS + relational database (see `DECISIONS.md`)
- App boundaries defined: `core`, `contents`, `hiring` (see `DECISIONS.md`)
- Global `templates/` and `static/` directory structure decided (see `DECISIONS.md`)

**Status: Complete**, as evidenced by the decisions recorded in `DECISIONS.md`.

## Phase 2 — Visual / UX Prototyping

### Objective
Explore visual design, layout, and page structure before production implementation.

### Scope
A standalone, framework-free HTML/CSS/JS mockup (`prototype/index.html`) covering Home, Projects (list + detail), About, and Contact, using placeholder persona and content. Confirmed (2026-08-24, see `DECISIONS.md`) to serve as a styling/design-and-layout reference only — it will not be ported into or reused as production code.

### Completion Criteria
To be defined. (No explicit sign-off criteria has been established by the project owner for when this phase is considered done — e.g. whether further pages/states will be mocked up before moving on.)

**Status: In progress.** The prototype's relationship to the production build is now resolved (design/styling reference only, not code to reuse — see `DECISIONS.md`); it is up to the owner whether more of the prototype is built out before Phase 3 begins.

## Phase 3 and beyond

To be defined.

No production implementation (Django project scaffolding, models, React islands, deployment) has been started, and no explicit roadmap for it has been given by the project owner. Per `CLAUDE.md`, production scaffolding should not begin until the owner explicitly requests it.
