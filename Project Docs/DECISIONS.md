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
- Consequences: Every page built under this decision will need its placeholder copy revisited once real content or content-backed models exist. Do not treat any placeholder string as real biographical/project data. **Partially revisited in Phase 5** — see "Real content replaces placeholders" below; the Projects page and Home's featured-project card are the deliberate remaining exception until model-backed content exists (Phase 4's `projects` app is scaffolded but still empty).

## Decision: Real content replaces placeholders (Phase 5); Projects/featured-project stay placeholder by choice

- Status: Accepted
- Date: 2026-08-24 (Phase 5)
- Context: The owner's real content (name, bio, skills, contact links, GitHub username) became available and was supplied for Phase 5. The owner explicitly scoped this phase narrower than `PHASES.md`'s original speculative Phase 5 description (real navigation/animation) — see the updated `PHASES.md` Phase 5 entry.
- Decision: Real content now replaces the generic placeholders in `base.html`, `home.html` (except the featured-project card), `about.html`, and `contact.html`. The site brand mark ("S.") is auto-derived from the real first name for now — the owner has a custom badge image to swap in as a separate, explicitly deferred follow-up (they asked to be consulted again before it's added). Home's featured-project card and the entire Projects page (`templates/pages/projects.html`) were explicitly excluded from this content swap by the owner and remain on mockup/placeholder content — not an oversight.
- Reasoning: Owner's explicit direction, given directly in response to a planning-time request for content ("credentials"). Keeping Projects/featured-project on placeholder content avoids describing specific real projects twice (once now as static text, again later as real `Project` model instances in a future phase) — better to wait for the model.
- Consequences: The About-snapshot headline (`ADJECTIVE.` × 3 placeholder) received real single-word content ("CURIOSITY." / "CREATION." / "EXPERIMENTATION.") rather than the owner's original full-sentence answer, which would have overflowed the large display-heading font sizing — the full sentences were kept as a new smaller supporting line (`.about-headline-sub`, new CSS class) underneath instead, per the owner's explicit choice between the two options offered. Any future work on Home's featured project or the Projects page should treat their current placeholder content as still fully "Phase 3 mockup," not real data to preserve.

## Decision: GitHub page fetches live data from the public API (Phase 5)

- Status: Accepted
- Date: 2026-08-24 (Phase 5)
- Context: The `/github/` page (added post-Phase 3) had shown static placeholder profile data with live-fetching left as an explicitly open, unscheduled `TASKS.md` item. The owner chose to implement it now as part of Phase 5, when asked directly.
- Decision: `core/views.py`'s `github` view calls `https://api.github.com/users/shahbazkhan74659-crypto` server-side (5s timeout, wrapped in `try/except requests.RequestException`), passing avatar/name/bio/repo/follower/following counts and the real profile URL into the template context. On any failure, it falls back to hardcoded real static values (not the old generic placeholder) so the page never 500s. `requests` (and its transitive deps: `certifi`, `charset-normalizer`, `idna`, `urllib3`) was added to `requirements.txt`, pinned via `pip freeze`.
- Reasoning: Owner's explicit choice between "live fetch now" and "static real values only" when asked during planning — live fetch keeps the stats always current with minimal extra implementation cost (one HTTP call).
- Consequences: GitHub's unauthenticated API caps out at 60 requests/hour per IP — fine for a low-traffic personal portfolio, but there is no caching yet. A future enhancement could add Django's cache framework if traffic ever approaches that limit; not needed now. The username is a hardcoded constant in `core/views.py` (`GITHUB_USERNAME`) since no settings/config model exists to store it dynamically.

## Decision: GitHub page also lists real repositories in a scrollable panel

- Status: Accepted
- Date: 2026-08-24 (post-Phase 5 addition, not part of any numbered phase)
- Context: The owner asked to also list their real GitHub repositories on `/github/`, read-only, each linking straight out to the repo on GitHub — same pattern as the profile-card fetch, using a hand-drawn mockup to show placement (beside the profile card, its own scrollable section).
- Decision: `core/views.py`'s `github` view makes a second call to `https://api.github.com/users/<username>/repos?sort=updated&per_page=100` (same timeout/error-handling pattern as the profile fetch — falls back to an empty list, not a crash), passing name/description/language/star-count/URL per repo. `templates/pages/github.html` renders them in a new `.repo-list` panel next to `.profile-card` (`.github-layout`, a two-column CSS grid — `grid-template-columns: 1fr 1fr; align-items: stretch;` — so both panels share equal width and height, revised same day after the owner flagged the initial flex layout as mismatched), each repo a full-row link (`.repo-item`) to its real GitHub URL; the panel scrolls internally (fixed `height: 460px; overflow-y: auto`, matching `.profile-card`'s height) rather than growing the page.
- Reasoning: Owner's explicit direction; sorted by most-recently-updated with no cap/filtering (all repos shown, forks included) since the owner didn't ask for either.
- Consequences: Same 60 req/hour unauthenticated rate-limit and no-caching situation as the profile fetch now applies twice per page load (two API calls) — still fine for current traffic, same future-caching note applies. If a repo's `description` is null, only the name/language/star row renders (no empty paragraph).

## Decision: Real "SK" badge image replaces the auto-derived text brand mark

- Status: Accepted
- Date: 2026-08-24 (post-Phase 5 addition, not part of any numbered phase)
- Context: The owner supplied a custom "SK" badge graphic (brushed-metal embossed plate, AI-generated) on a flat gray background with a soft drop shadow and a bright top bevel highlight — this was deliberately deferred back in Phase 5 (see above) with the owner asking to be consulted again before it was added. The owner then confirmed to proceed.
- Decision: Background removed via an edge-based flood fill (not the simple luminance-threshold technique used for the GitHub logo) — the badge's dark drop shadow and bright highlight rim meant no single brightness cutoff could separate it from the flat gray background cleanly, so pixels were grown outward from the image border using per-step luminance-difference tolerance (stopping at sharp edges regardless of whether they went darker or brighter), then only the largest connected foreground region was kept (dropping the small watermark sparkle and stray noise as disconnected islands) — cropped to `static/images/sk-badge.png`. Wired into `templates/base.html` as `.nav-mark-badge` (28px tall) and `.foot-mark-badge` (22px tall) images inside the existing `.nav-mark`/`.foot-mark` links/spans, replacing the "S." text.
- Reasoning: Owner's explicit direction; the two-stage technique (tolerance flood fill + largest-component filter) was necessary because this asset's background/shadow/highlight interplay made the GitHub-logo approach (recolor by luminance, single threshold) unsuitable — verified in-browser at both nav and footer sizes before considering it done.
- Consequences: The badge PNG is a photographic/textured asset (brushed metal, kept in its original shading), unlike the GitHub logo which was recolored flat white — future edits to the nav/footer mark should treat it as a fixed image asset, not something restyleable via CSS `color`.

## Decision: Timeline cut from the roadmap; Phase 6 merged into a redefined Phase 8

- Status: Accepted
- Date: 2026-08-24
- Context: Phase 6 ("Connecting Pages to the Apps, and Modals") was put on hold earlier the same day since no confirmed need for modal UI existed yet. Phase 8 was originally "Vertical Growth Timeline, Contact, and Hire Me." Revisiting Phase 8, the owner decided: the vertical Timeline feature isn't needed at all; Contact is already sufficiently covered by the real Contact page/info shipped in Phases 3 and 5; and Phase 6's held-back scope (a real `Project` model + a modal mechanism for viewing project details) should become Phase 8's actual content instead.
- Decision: Phase 8 is redefined as "Projects App: Modal & Mechanism, and Hire Me" — building the real `projects` app (a `Project` model, replacing the Phase 3/5 mockup content on the Projects page and Home's featured-project card) with a modal-based mechanism for viewing project details, plus the "Hire Me" feature. Phase 6 is marked superseded/merged into Phase 8 rather than left as a separate on-hold phase — its number and history stay in `PHASES.md` (not deleted), but its remaining work now lives under Phase 8. Timeline is removed from `PROJECT.md`'s Core Features list entirely — not deferred, cut. Contact gets no further scheduled work; the "working, backend-processed contact form" idea from the original Phase 8 description is not carried forward (the static Contact page with real email/GitHub/LinkedIn is considered sufficient) unless the owner raises it again later.
- Reasoning: Owner's explicit direction. Folding Phase 6's modal mechanism into Phase 8 avoids two phases doing overlapping "wire Projects up to real data" work, and gives the previously-speculative "modal UI" (see Phase 6's original scope) a concrete, confirmed purpose: project detail modals are exactly the interactivity Phase 6 was guessing at.
- Consequences: `PHASES.md`'s Phase 6 entry keeps its original objective/scope text as a historical record but its status changes to "Superseded — merged into Phase 8." Phase 7 (Blog and Resume) is unaffected and stays the immediate next phase before Phase 8. If Timeline or a working Contact form are ever wanted again, they would need a fresh phase-scope decision — they are not implicitly slotted into any existing phase anymore.

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
