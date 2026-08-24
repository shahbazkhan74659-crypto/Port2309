# Development Phases

The project owner has defined the full build roadmap, Phase 0 through Phase 12 (confirmed 2026-08-24 as the complete set — no further phases expected). The earlier planning and prototyping work is recorded below as **Phase 0 — Pre-Development**, an unnumbered stage that precedes the numbered build roadmap (owner's explicit choice, 2026-08-24, to restart numbering from Phase 1 rather than continue the old Phase 1/2 sequence). Do not invent additional phases beyond what is listed here — see `CLAUDE.md` rule 3.

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
To be defined.

**Status: Not started.**

## Phase 2 — Static Global Base Structure and a Home Page

### Objective
Establish the site's global, reusable structure — the base Django template(s), global `templates/`/`static/` layout (per the Phase 0 decision), and Tailwind CSS setup that every page will build on — and implement the Home page against it.

### Scope
To be defined in further detail by the project owner. Implied by the phase name: a global base template (nav/footer/shared chrome) and a static (non-dynamic/no-models-yet) Home page built from scratch using `prototype/index.html` only as a styling/layout reference (see `DECISIONS.md`).

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 3 — Other Static Pages

### Objective
Build out the remaining static (non-dynamic/no-models-yet) pages on top of the Phase 2 global base structure.

### Scope
To be defined in further detail by the project owner. Implied by the phase name and the prototype reference (see `PROJECT.md`, `DECISIONS.md`): pages such as About and Contact beyond the Phase 2 Home page, built from scratch using `prototype/index.html` only as a styling/layout reference — not yet the dynamic, model-backed pages that depend on the `projects` app (and any other app(s) still to be resolved, see `DECISIONS.md`).

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 4 — Apps: `core`, `projects`

### Objective
Scaffold the two Django apps that carry the site's dynamic functionality: `core` (views, URLs, and the site's main routing; identity, etc.) and `projects` (handling the owner's projects, works, and code).

### Scope
To be defined in further detail by the project owner. This phase also formally supersedes the earlier three-app plan (`core`/`contents`/`hiring`) — see `DECISIONS.md`. Where Designs, Blog, Resume, Timeline, and Hire Me fit is unresolved and not part of this phase's stated scope.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 5 — Turning the Static Pages into Dynamic Pages

### Objective
Take the static pages/base structure built in Phases 2–3 and make them dynamic — wiring up navigation, placeholder content/states, and animation.

### Scope
To be defined in further detail by the project owner. Implied by the phase name: real (non-hash, server-routed) navigation between pages, placeholder content/loading states, and animation/interactivity — likely where the planned React/JS islands (see `DECISIONS.md`) come in, though that hasn't been confirmed for this phase specifically.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 6 — Connecting Pages to the Apps, and Modals

### Objective
Wire the static/dynamic pages built so far up to real data from the `core`/`projects` Django apps (see `DECISIONS.md`), and add modal UI.

### Scope
To be defined in further detail by the project owner. Implied by the phase name: pages driven by app views/models instead of static placeholder content, plus modal components (e.g. project detail modals) — likely where React/JS islands (see `DECISIONS.md`) get used, though not confirmed for this phase specifically.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 7 — Blog and Resume

### Objective
Build the Blog and Resume features.

### Scope
To be defined in further detail by the project owner. This phase begins resolving part of the open question in `DECISIONS.md` (where Designs/Blog/Resume/Timeline/Hire Me fit under the two-app `core`/`projects` plan) — which app(s) Blog and Resume live in has not yet been stated.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 8 — Vertical Growth Timeline, Contact, and Hire Me

### Objective
Build the vertical Timeline feature (college → now, per `PROJECT.md`), a working Contact feature (replacing the prototype's simulated-only contact form), and the "Hire Me" feature.

### Scope
To be defined in further detail by the project owner. This phase resolves most of the remaining open question in `DECISIONS.md` (where Designs/Blog/Resume/Timeline/Hire Me fit under the two-app `core`/`projects` plan) — Timeline and Hire Me are now scheduled, though which app(s) they live in has not yet been stated. Designs remains the one originally-planned feature with no phase yet.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 9 — Finishing and Polishing the Frontend and Backend

### Objective
Finish and polish the site across both frontend and backend, following the feature-building phases (0–8).

### Scope
To be defined in further detail by the project owner.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 10 — Database: MySQL/PostgreSQL

### Objective
Choose and set up the production relational database engine — PostgreSQL or MySQL — resolving the deferral recorded in `DECISIONS.md` (deliberately left open until closer to a hosting decision).

### Scope
To be defined in further detail by the project owner. Implied by the phase name and its placement after the feature-building/polish phases: moving from whatever local database was used during development onto the chosen production engine.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 11 — Full End-to-End Testing (Component/Unit + E2E)

### Objective
Full test coverage across frontend, backend, and database: component/unit tests plus end-to-end tests.

### Scope
To be defined in further detail by the project owner. Implied by the phase name: unit/component-level tests (e.g. Django test framework for backend, a JS testing tool for React islands) and end-to-end tests exercising the whole stack, including the Phase 10 production database. No testing framework/tooling has been chosen yet.

### Completion Criteria
To be defined.

**Status: Not started.**

## Phase 12 — Deployment and Hosting

### Objective
Deploy and host the finished site.

### Scope
To be defined in further detail by the project owner. Implied by the phase name and its placement after Phase 10 (database engine, chosen "closer to a hosting decision" per `DECISIONS.md`) and Phase 11 (testing): choosing a hosting provider and deploying the completed, tested site. No hosting provider has been chosen yet.

### Completion Criteria
To be defined.

**Status: Not started.**

Phase 12 is the last phase in the roadmap — the project owner does not expect further phases (confirmed 2026-08-24). If new phases are identified later, add them here rather than assuming the roadmap is fixed forever.
