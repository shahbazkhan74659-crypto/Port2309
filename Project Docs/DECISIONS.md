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
- Consequences: Where Designs, Blog, Resume, Timeline, and the "Hire Me" feature (previously slated for `contents`/`hiring`) now live was initially an open question — **resolved 2026-08-24, see "Feature placement: Designs/Blog/Resume/Timeline/Hire Me → `core`" below.** The "Designs kept removable via feature flag" decision below also needed revisiting once this was resolved, since it was written against the now-superseded `contents` app — see that decision's updated Consequences.

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
- Consequences: The isolation principle (own model + feature flag) still stands, but it originally assumed a `contents` app that no longer exists in the plan. As of 2026-08-24, Designs is placed in `core` (see "Feature placement: Designs/Blog/Resume/Timeline/Hire Me → `core`" below) — the feature-flag isolation still applies within `core`.

## Decision: Feature placement — Designs, Blog, Resume, Timeline, Hire Me → `core`

- Status: Accepted
- Date: 2026-08-24
- Context: The "Two Django apps — `core`, `projects`" decision above left it unresolved where Designs, Blog, Resume, Timeline, and Hire Me would live, deferring the choice per-feature. The owner has now settled it for all five at once rather than one at a time.
- Decision: Designs, Blog, Resume, Timeline, and Hire Me all live in the `core` app. `projects` is scoped strictly to the owner's projects/works/code — nothing else.
- Reasoning: Owner's explicit direction.
- Consequences: Phases 7 (Blog and Resume) and 8 (Timeline, Contact, Hire Me) now have a settled app target — see `PHASES.md`. Designs still has no phase assigned yet, but when it is scheduled it belongs in `core`. `TASKS.md`'s open-question entry on this is resolved.

## Decision: Build a standalone static visual prototype before production implementation

- Status: Accepted (observed via existing code)
- Date: Unknown exact date; file present in the repository as of 2026-08-23.
- Context: `prototype/index.html` exists as a single, self-contained, framework-free HTML/CSS/JS file implementing a client-side hash-routed mockup (Home, Projects list/detail, About, Contact) with placeholder persona ("Renzo Malik") and placeholder project content — built independently of the planned Django + Tailwind + React stack.
- Observed implementation: See `ARCHITECTURE.md` for full technical detail.
- Original reasoning: To be defined. (No record explains why a standalone vanilla-JS prototype was chosen over prototyping directly within the planned Django + Tailwind stack.)
- Consequences: None outstanding — see the "Prototype is a styling/design reference only" decision below, which resolves how it relates to the production build.

## Decision: Tailwind wired via npm + Tailwind CLI v4 (CSS-first `@theme` config)

- Status: Accepted
- Date: 2026-08-24 (Phase 2)
- Context: Phase 2 required a working Tailwind CSS build, per the confirmed stack. Node v24.18.0/npm 11.16.0 were confirmed available on the dev machine. Tailwind v4 supports CSS-first configuration (`@theme` in the stylesheet itself) instead of a separate `tailwind.config.js`.
- Decision: `package.json` at repo root with `tailwindcss` + `@tailwindcss/cli` as devDependencies. Source stylesheet at `static_src/css/input.css` declares the prototype's exact design tokens (colors, fonts) in an `@theme` block, plus the prototype's hand-written component CSS (nav, hero, sections, footer, etc.) ported near-verbatim rather than rewritten as Tailwind utility classes. Built to `static/css/main.css` via `npm run build:css` (one-shot) / `npm run watch:css` (dev). Build output is gitignored, like `node_modules/`.
- Reasoning: The prototype's design is bespoke art direction (fluid `clamp()` typography, custom color tokens, specific component layouts) rather than a Tailwind-utility-shaped design — porting the CSS as-is guarantees visual fidelity to the prototype (the owner's explicit priority for Phase 2) while still getting Tailwind's build pipeline in place for future utility-based/React-island work.
- Consequences: `main.css` is a build artifact, not checked into git — `npm install && npm run build:css` (or an already-built `static/css/main.css`) is required before `runserver` shows a styled page. As more Tailwind utilities get used going forward, this file will start mixing hand-written component CSS with generated utilities.

## Decision: Phase 2/3 static pages routed directly via `config/`, not an app

- Status: Accepted
- Date: 2026-08-24 (Phase 2)
- Context: Phase 2's Home page needed a working URL + view, but the `core`/`projects` apps aren't scaffolded until Phase 4 (see the "Two Django apps" decision above). Django doesn't require an app for basic template-rendering routes.
- Decision: `config/views.py` holds a plain `home` view; `config/urls.py` routes `path('', views.home, name='home')` directly, with no app involved. Phase 3's additional static pages are expected to follow the same pattern until Phase 4.
- Reasoning: Avoids scaffolding `core`/`projects` prematurely (out of Phase 2/3 scope) while still letting Home be a real, server-routed page rather than a static file.
- Consequences: This routing is expected to move into `core`'s `urls.py`/`views.py` once that app exists in Phase 4 — treat `config/views.py`'s page-rendering views as temporary, not a long-term pattern. **Done as of Phase 4, 2026-08-24** — see the `core.urls` decision below.

## Decision: `core.urls` as `ROOT_URLCONF`; `config/` holds only settings/WSGI/ASGI

- Status: Accepted
- Date: 2026-08-24 (Phase 4)
- Context: Phase 4 scaffolded `core` and `projects` and moved all routing out of `config/`, per the owner's explicit instruction that `config/` should end up containing only `settings.py`, `wsgi.py`, and `asgi.py` — no `urls.py`, no `views.py`. Django's `ROOT_URLCONF` setting must point at some module with a `urlpatterns` list, so removing `config/urls.py` entirely meant that module had to become something else.
- Decision: `ROOT_URLCONF = 'core.urls'` in `config/settings.py`. `core/urls.py` holds the full `urlpatterns` list, including `path('admin/', admin.site.urls)` — `core/views.py` holds all page views (`home`, `about`, `contact`, `projects`, `github`), moved verbatim from `config/`. It is included unnamespaced (there is no `include()` layer at all — `core.urls` *is* the root), so every existing `{% url 'home' %}`/`'about'`/`'contact'`/`'projects'`/`'github'` template reference kept working with zero template changes.
- Reasoning: This matches `core`'s own documented job description (`ARCHITECTURE.md`/the "Two Django apps" decision above: *"views, URLs, and the main routing of the site"*) — `core` acting as the actual root router isn't a workaround, it's what the app boundary was defined to do.
- Consequences: Any future app-specific urls (e.g. a `projects/urls.py`, once that app grows beyond empty) would be `include()`d from `core/urls.py`, not from a project-level `config/urls.py` — there isn't one. `core` permanently doubles as the site's top-level router. If a future phase ever needs project-level URL concerns (e.g. i18n URL prefixing, a maintenance-mode toggle) that don't belong in `core`, that would need revisiting this decision rather than silently reintroducing `config/urls.py`.

## Decision: Generic placeholder content for pre-content-model pages

- Status: Accepted
- Date: 2026-08-24 (Phase 2)
- Context: The prototype's text (name "Renzo Malik," bio, projects, socials) is fictional and, per `CLAUDE.md`, must not be reused as real content. The owner's real bio/project/contact content does not exist yet, and no content models exist until later phases.
- Decision: Pages built before real content or content models exist (starting with the Phase 2 Home page) use clearly generic, non-identity placeholder copy (e.g. "YOUR NAME," "ROLE / ROLE / ROLE," "Placeholder paragraph about you") hardcoded directly in the template — not the prototype's persona, and not passed via view context yet.
- Reasoning: Owner's explicit direction — real content decision deferred rather than fabricated.
- Consequences: Every page built under this decision will need its placeholder copy revisited once real content or content-backed models exist. Do not treat any placeholder string as real biographical/project data.

## Decision: Hero portrait redesigned as a large overlapping image, diverging from the prototype

- Status: Accepted
- Date: 2026-08-24 (Phase 2, post-completion refinement)
- Context: The Phase 2 Home page initially ported the prototype's hero portrait treatment as-is: a small (`clamp(150–300px)` wide) image floated right, with text wrapping around it via `shape-outside`. After adding the real portrait photo, the owner asked for a materially different treatment: an image spanning roughly half the screen, sized to its actual aspect ratio (head-to-stomach fully visible, no cropping), positioned top-right just below the sticky nav (slightly overlapping under it), with the hero text (`I BUILD.` / `I WRITE.` / name / `I EXPLORE.`) layered on top of the image via `z-index` rather than flowing around it.
- Decision: `.hero-portrait-slot` uses `position: absolute` sized by `height` + `aspect-ratio: 1149 / 1369` (the photo's real ratio) instead of the prototype's fixed float box; hero text gets `position: relative; z-index: 2` plus a soft `text-shadow` to stay legible over the photo.
- Reasoning: Owner's explicit direction, given after seeing the ported-as-is version rendered — the float/wrap treatment worked for the prototype's small decorative portrait but not for a large, real photo meant to anchor the hero.
- Consequences: This is an intentional, confirmed deviation from "match the prototype's structure" for this one element — do not "fix" it back toward the prototype's float-based layout. Other Home sections (featured project, statement, about snapshot, CTA, nav/footer) still follow the prototype's structure as recorded in the Phase 2 completion note in `PHASES.md`.

## Decision: GitHub gets a custom in-site profile page; LinkedIn/Email link out directly

- Status: Accepted (page built as a placeholder — live data fetch not yet implemented)
- Date: 2026-08-24 (post-Phase 3 addition, not part of any numbered phase)
- Context: The owner wanted a richer way to surface GitHub, LinkedIn, and Email beyond a bare link. Investigated feasibility for each: GitHub has a public REST API (`api.github.com/users/<username>`) usable without auth for basic profile data, so a live-fetched read-only card is realistic. LinkedIn has no public API for reading arbitrary profile data, and scraping their pages would violate their Terms of Service — a live "fetch my LinkedIn profile" feature isn't viable. Email has no profile to fetch beyond an optional third-party service (Gravatar), which wasn't pursued.
- Decision: Only GitHub gets a dedicated in-site page (`/github/`, `templates/pages/github.html`, new `.profile-card`/`.profile-*` CSS in `input.css`) — for now it renders placeholder content (generic name/bio/stats, no live API call), with live-fetching deferred to later. LinkedIn and Email get no custom UI — wherever they appear (Contact page, Home CTA), they stay plain outbound links. The site footer was trimmed to drop LinkedIn and Email entirely (they're only reachable via the Contact page's list now); the footer's GitHub link now points to the new in-site page instead of out to GitHub directly.
- Reasoning: Owner's explicit direction, given after discussing the technical/legal feasibility of each platform. Treated as a small, ad-hoc addition (one view + one template, no models or apps needed) rather than a new numbered phase — per `CLAUDE.md`'s rule that phase count/order is the owner's call, and this was scoped the same way the Phase 2 hero-portrait addition was (see the decision above).
- Consequences: The GitHub page currently shows placeholder data only (`&mdash;` stat counts, generic name/bio) with a `.form-note`-style disclaimer that live data isn't connected yet — a future addition should replace this with a real `requests.get()` call to GitHub's API (server-side, cached) once the owner wants that built. If LinkedIn or Email ever get their own API-backed integration, that would need a fresh feasibility discussion — the "no custom UI" call here was specifically because no viable public data source exists for them today.

## Decision: Prototype is a styling/design reference only — production build starts from scratch

- Status: Accepted
- Date: 2026-08-24
- Context: The relationship between `prototype/index.html` and the planned Django + Tailwind + React production build was previously unconfirmed (see decision above).
- Decision: The prototype is not to be ported, reused, or built upon as code. Production implementation will be built from scratch on the confirmed stack (Django + Django templates + Tailwind CSS + React/JS + relational database). The prototype's HTML/CSS is retained only as a visual/styling and layout-structure reference to consult while building the real templates and components.
- Reasoning: Owner's explicit direction.
- Consequences: Do not treat `prototype/index.html` as a source to copy code from during production scaffolding (Phase 3) — reimplement the design intent in Django templates/Tailwind/React rather than lifting its vanilla-JS routing/rendering approach. Its placeholder persona ("Renzo Malik") and placeholder project content are not real content and must not carry over either. See `PHASES.md` and `TASKS.md`.
