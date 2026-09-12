# Portfolio

A personal portfolio website — a single place for projects, writing, resume, and contact information. Live at **[shahbazkhan.onrender.com](https://shahbazkhan.onrender.com)**.

## What this is

The site markets and showcases the owner's work (Projects, Blog, Resume, About, Contact, Hire Me) and includes a custom, staff-only **Admin Hub** for managing all of it — content, blog posts, project entries, resume/media, leads, and testimonials — without touching code or using Django's default `/admin/`.

## Current status

A static visual prototype (`prototype/index.html`) came first as a pure design/layout reference — it's kept in the repo but is not part of the running site. The real, production Django build has since gone well beyond it:

**Built & live**
- Public pages: Home, About, Projects (with filtering/search/pagination, no page reload), Blog, Resume, Contact, Hire Me, GitHub (live GitHub API data), Feedback/Testimonials
- Real database-backed content throughout — hero section, About, contact details, projects, blog posts/tags — editable from the Admin Hub, not hardcoded in templates
- Two real, non-placeholder featured projects (TS Library, LoadGate) plus a real freelance client project (Fire Service Website for Iconic Techno Service), and one real blog post
- Contact and Hire Me forms are fully backend-processed (validated, persisted, AJAX-submitted with a no-JS fallback)
- SEO: sitemap, robots.txt, canonical URLs, Open Graph/Twitter tags, JSON-LD structured data
- Mobile-responsive off-canvas navigation
- Deployed on Render (Gunicorn + WhiteNoise), PostgreSQL via Neon, media storage via Cloudinary, monitored by UptimeRobot

**Open / in progress**
- Real resume experience/education content and an actual resume PDF (still placeholder)
- More real projects and project screenshots
- Additional blog posts (not gated on any phase — can be authored anytime via the Admin Hub)
- React "islands" for targeted interactivity — planned, not yet introduced (everything dynamic today is vanilla JS + AJAX)

See `Project Docs/TASKS.md` for exactly what's active, and `Project Docs/DECISIONS.md` for why things were built the way they were.

## Tech stack

| Layer | Choice |
|---|---|
| Backend | Python, Django 5.2 |
| Database | PostgreSQL (Neon in production, local Postgres in dev) |
| Frontend | Django templates, Tailwind CSS v4, vanilla JS (AJAX via `fetch()`) — React islands planned, not yet built |
| Media storage | Cloudinary (production), local filesystem (dev) |
| Hosting | Render (Gunicorn + WhiteNoise), UptimeRobot keep-alive |
| Other | `python-dotenv` (env config), `requests` (GitHub API), Pillow (image processing) |

## Project structure

```
core/            Site-wide pages (Home, About, Contact, Hire Me, Feedback), shared models, forms
projects/        Projects and Blog — models (Project, Post, Tag, ProjectImage), views, filtering
adminhub/        Custom staff-only content-management hub (mirrors the public site with inline CRUD)
config/          Django project settings, WSGI/ASGI entrypoints
templates/       Global Django templates (public site + Admin Hub)
static/          Built static assets (Tailwind output, images) — static/css/main.css is a build artifact
static_src/      Tailwind source (static_src/css/input.css)
prototype/       Original static HTML/CSS/JS design mockup — reference only, not part of the live site
Project Docs/    Living documentation set — see below
```

## Getting started

**Prerequisites:** Python 3.11+, Node.js/npm, PostgreSQL (optional locally — SQLite is the dev default).

```bash
# Backend
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
cp .env.example .env             # fill in DJANGO_SECRET_KEY, etc.
python manage.py migrate
python manage.py runserver

# Frontend (Tailwind build, separate terminal)
npm install
npm run watch:css                # or `npm run build:css` for a one-shot minified build
```

Visit `http://localhost:8000`. The Admin Hub is at `/adminhub/`.

### Environment variables (`.env`)

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django secret key |
| `DJANGO_DEBUG` | `True` for local dev |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated allowed hosts |
| `DATABASE_URL` | Optional — a Postgres connection string; omit to use the SQLite dev default |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Required in production (`DEBUG=False`) |
| `CLOUDINARY_CLOUD_NAME` / `CLOUDINARY_API_KEY` / `CLOUDINARY_API_SECRET` | Optional — leave unset for local dev (falls back to local media storage) |

## Documentation

This project keeps a living, six-file documentation set under `Project Docs/`:

| File | Answers |
|---|---|
| `CLAUDE.md` | How should Claude (the AI assistant) behave while working on this project? |
| `PROJECT.md` | What are we building, and why? |
| `PHASES.md` | In what order are we building it? |
| `TASKS.md` | What's being worked on right now? |
| `ARCHITECTURE.md` | How does the system work internally? |
| `DECISIONS.md` | Why did we choose to build it this way? |

## License

All rights reserved — see [`LICENSE`](LICENSE). This is not open-source software.
