# CLAUDE.md

Rules and instructions for how Claude should work in this repository.

## Project Documentation System

This project uses a strict 6-file Markdown documentation system, each file with **one** distinct responsibility:

```text
CLAUDE.md       → Rules and instructions (this file)
PROJECT.md      → Project definition — what we're building, and why
PHASES.md       → Development roadmap — in what order we're building it
TASKS.md        → Current execution — what we're doing right now
ARCHITECTURE.md → System design — how the system works internally
DECISIONS.md    → Technical decision history — why we chose to build it this way
```

Claude must preserve this separation. Do not duplicate large sections across files — if a fact belongs in another file, put it there and reference it instead.

## Mandatory Maintenance Rules

### 1. Responsibility Separation
Keep each file focused on its own responsibility. Do not duplicate large sections across files.

### 2. TASKS.md
Must remain actionable. Tasks should normally belong to a phase defined in `PHASES.md`. Tasks represent concrete work, not vague project goals.

### 3. PHASES.md
Must remain high-level: development stages, milestones, sequencing — **not** individual coding tasks. The project owner determines the number and order of phases. Claude must not arbitrarily restructure the project's phase order or phase count.

### 4. ARCHITECTURE.md
Describes the project's actual technical structure — stable system design, relationships, boundaries, data flow, dependencies, architectural patterns. Not a dumping ground for temporary implementation notes.

### 5. DECISIONS.md
Records significant technical decisions and the reasoning behind them. Do not create decision records for trivial coding choices.

### 6. Documentation Accuracy
Update documentation when major project changes make existing documentation inaccurate.

### 7. No Silent Destruction
Never silently modify, delete, or replace important documentation. If a change makes existing documentation obsolete: (1) identify what became obsolete, (2) explain why, (3) determine which file(s) should change, (4) make the update deliberately. Do not casually overwrite historical information.

### 8. Six-File Limit
Do not create additional Markdown documentation files unless information genuinely cannot fit into these six. Assume these six are sufficient by default.

### 9. Actual Project State
Documentation must always reflect the actual project state. Never document a feature, architecture, system, component, or integration as completed when it is not actually implemented.

### 10. Whole-Project Understanding
Together, the six files should let Claude answer "Analyze the whole project" without reading the entire codebase first — but they remain a high-level representation, not a replacement for source code.

## Documentation Conflict Priority

```text
CLAUDE.md
    ↓
PROJECT.md
    ↓
PHASES.md
    ↓
TASKS.md
    ↓
ARCHITECTURE.md
    ↓
DECISIONS.md
```

When information conflicts between documentation files, the higher-priority document governs. **However**, when code and documentation disagree, do not blindly trust the documentation — inspect the code, determine the actual current state, and correct the stale documentation.

## Mandatory Pre-Change Documentation Check

Before making any significant project change, identify which documentation file(s) will become affected or inaccurate as a consequence:

- New project requirement → `PROJECT.md`
- Change in development stage → `PHASES.md`
- New/current implementation work → `TASKS.md`
- Architectural change → `ARCHITECTURE.md`
- Significant technical choice → `DECISIONS.md`
- Change to Claude's working rules → `CLAUDE.md`

A single change may require updates to multiple files.

## Project-Specific Notes

- **As of 2026-08-24 (Phase 2)**, the repository contains `prototype/index.html` (static reference-only prototype, unchanged) plus a Django project with a real Home page: `manage.py`, `config/` (settings/urls/views), `templates/` (`base.html` + `pages/home.html`), `static/`+`static_src/` (Tailwind-built CSS), `.venv/` (gitignored), `requirements.txt`, and `package.json`/`node_modules/` (gitignored) for the Tailwind toolchain. No Django apps, database models, or React tooling exist yet. Do not assume more exists than this — verify against the filesystem before making claims. The repo is git-initialized and pushed to `origin` (`https://github.com/shahbazkhan74659-crypto/Port2309.git`, branch `main`).
- A production tech stack (Django + Django templates + Tailwind CSS + React/JS + a relational database, engine TBD) and Django app boundaries were decided during prior planning discussions. See `DECISIONS.md`. Phases 1–2 are done; **do not create the `core`/`projects` apps or start further production implementation (Phase 3+) until the project owner explicitly asks for it.**
- Styled pages require a Tailwind build: `npm install && npm run build:css` generates `static/css/main.css` (gitignored, not committed) from `static_src/css/input.css`. `manage.py runserver` does not run this automatically.
- The documentation files themselves live in `Project Docs/` (not the repository root) — the project owner relocated them there.
- The prototype uses a placeholder persona ("Renzo Malik") and fictional example projects. This is not the owner's real name, resume, or project list — real content has not yet been provided. Do not treat prototype content as real biographical or project data.
- The prototype is a **styling/design reference only** — production implementation will be built from scratch on the confirmed stack, not by porting or reusing the prototype's code (see `DECISIONS.md`, decided 2026-08-24).
