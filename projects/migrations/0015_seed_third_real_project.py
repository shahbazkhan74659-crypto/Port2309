from django.db import migrations

REAL_TAGS = ["Django", "React", "TypeScript", "PostgreSQL", "REST APIs"]

REAL_PROJECT = {
    "title": "Fire Service Website",
    "slug": "fire-service-website",
    "short_description": (
        "A production business website for a fire & life-safety systems "
        "company, Iconic Techno Service, with a custom admin CMS for "
        "managing every page's content and reviewing leads."
    ),
    "description": (
        "Fire Service Website — Business Site & Admin CMS for Iconic Techno Service\n\n"
        "A real, live production website built for Iconic Techno Service, a fire & "
        "life-safety systems company — not a demo or a template, but the client's "
        "actual public-facing business site plus the private tools they use to run "
        "it day to day. Ten public pages (Home, About, Services, Process, "
        "Clientele, Certifications, Contact, Survey, Consultation, Brochure) cover "
        "the marketing and lead-capture side; a custom Admin Hub behind a "
        "staff-only login covers content management and lead review.\n\n"
        "Feature Breakdown\n\n"
        "- Nine dedicated service pages — each service (fire alarm systems, gas "
        "suppression, fire hydrant systems, safety equipment, and more) gets its "
        "own URL, view, and hand-authored detail page with a real hero photo and "
        "a \"What's Included\" checklist, rather than one generic template driven "
        "by a slug.\n"
        "- Three lead-capture forms — Survey Request, Contact, and Consultation — "
        "built as React islands (mounted into specific page regions, not a full "
        "SPA) with Zod validation on the client and Django REST Framework "
        "serializers as the real trust boundary, so nothing client-side is "
        "trusted for correctness.\n"
        "- Admin Hub — a separate, staff-only CMS (session-authenticated, "
        "deliberately independent from Django's own /admin/) with a React-island "
        "CRUD interface for every piece of editable content: services, products, "
        "client logos, certifications, mission/vision statements, fire-risk "
        "assessment items, process phases, and sitewide numeric stats — all "
        "Add/Edit/Delete, wired live into the public pages that render them.\n"
        "- Lead review dashboard — every Survey/Contact/Consultation submission "
        "lands in a tabbed, paginated, resolvable list in the Admin Hub, plus a "
        "dark \"command center\" home dashboard showing today's lead counts, a "
        "30-day trend chart, and recent activity.\n"
        "- SEO built in from the start — canonical URLs, Open Graph/Twitter tags, "
        "and JSON-LD structured data (LocalBusiness, BreadcrumbList, per-service "
        "offer catalogs) on every page, plus a generated sitemap and robots.txt.\n"
        "- Account security for the Admin Hub — login rate-limiting after "
        "repeated failed attempts, and an email-OTP Forgot Password / Change "
        "Email flow.\n\n"
        "Tech Stack\n\n"
        "- Django 5.2, server-rendered templates, Django REST Framework for the "
        "API surface the React islands talk to\n"
        "- React 19 + TypeScript, built with Vite and injected into templates via "
        "django-vite — islands, not a full client-side app\n"
        "- Zod for client-side validation, mirrored by DRF serializers server-side\n"
        "- PostgreSQL in both development and production\n"
        "- Cloudinary for media storage, SendGrid (via django-anymail) for "
        "transactional OTP email, WhiteNoise for static files, all behind "
        "gunicorn\n\n"
        "From Local Development to a Live Deployment\n\n"
        "The project started on MySQL and was migrated to PostgreSQL once Render "
        "was chosen as the host — Render's free tier only offers managed "
        "Postgres, so rather than fight the platform, the database engine moved "
        "instead, with real data (leads, admin account, content edits) carried "
        "over via dumpdata/loaddata rather than a fresh reseed.\n\n"
        "Because Render's web-service disk is ephemeral and wipes on every "
        "deploy, media storage moved to Cloudinary and static files are served "
        "through WhiteNoise — both necessary specifically because of Render's "
        "platform model, not general best practice for every deployment target. "
        "Email delivery for OTP flows was likewise moved off raw SMTP to "
        "SendGrid's HTTP API partway through the project, after confirming Gmail "
        "SMTP was the more fragile choice for a PaaS-hosted app.\n\n"
        "A subtler bug surfaced around session handling: resetting a user's "
        "password directly (e.g. to recover a forgotten Admin Hub login) silently "
        "logs out every already-open session for that account, because Django "
        "ties each session to a hash of the current password. The fix was calling "
        "Django's own update_session_auth_hash() alongside any manual password "
        "reset — an easy detail to miss since the resulting symptom (a generic "
        "\"Something went wrong\" in the UI) looks nothing like an auth problem "
        "on the surface.\n\n"
        "Current Status\n\n"
        "Live in production on Render, backed by Neon PostgreSQL, serving real "
        "leads for the client today. Render's free tier spins the web service "
        "down after 15 minutes of inactivity, so the client's main complaint has "
        "been the resulting cold-start delay on the first visitor after a quiet "
        "period — the site is currently being migrated to a self-hosted VM on "
        "Oracle Cloud's Always Free tier, which stays on permanently with no "
        "spin-down, as the longer-term fix.\n\n"
        "What This Project Demonstrates\n\n"
        "Building for a real client with real constraints rather than a "
        "greenfield toy problem: a hybrid server-rendered-plus-React-islands "
        "architecture chosen deliberately over a full SPA, a genuinely separate "
        "admin CMS built from scratch instead of just exposing Django's default "
        "admin, SEO treated as a first-class requirement rather than an "
        "afterthought, and infrastructure decisions (database engine, media "
        "storage, email transport, and now the hosting platform itself) driven "
        "by the actual constraints of the chosen host and the client's real "
        "budget and reliability needs — including knowing when a platform choice "
        "has been outgrown and it's time to migrate rather than work around it "
        "again."
    ),
    "category": "Web App",
    "role": "Freelance Developer",
    "year": 2026,
    "status": "Live",
    "github_url": "https://github.com/shahbazkhan74659-crypto/FireService.git",
    "live_url": "https://iconic-techno-service.onrender.com",
    "order": 1,
    "featured": True,
}


def seed_third_project(apps, schema_editor):
    Tag = apps.get_model("projects", "Tag")
    Project = apps.get_model("projects", "Project")

    tags = [Tag.objects.get_or_create(name=name)[0] for name in REAL_TAGS]
    project = Project.objects.create(**REAL_PROJECT)
    project.tags.set(tags)

    Project.objects.filter(slug="loadgate").update(featured=False, order=2)
    Project.objects.filter(slug="ts-library").update(order=3)


def unseed_third_project(apps, schema_editor):
    Project = apps.get_model("projects", "Project")

    Project.objects.filter(slug=REAL_PROJECT["slug"]).delete()
    Project.objects.filter(slug="loadgate").update(featured=True, order=1)
    Project.objects.filter(slug="ts-library").update(order=2)


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0014_entry_recorder_rename_loadgate"),
    ]

    operations = [
        migrations.RunPython(seed_third_project, unseed_third_project),
    ]
