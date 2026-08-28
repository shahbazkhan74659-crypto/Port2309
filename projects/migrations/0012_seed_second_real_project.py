from django.db import migrations

REAL_TAGS = ["Django", "Python", "PostgreSQL", "JavaScript"]

REAL_PROJECT = {
    "title": "Entry Recorder",
    "slug": "entry-recorder",
    "short_description": (
        "A single-user Django app that replaces a paper logbook for a "
        "manufacturing client's truck-loading records — entries, batches, "
        "PDF exports, and account security, live on Render + PostgreSQL."
    ),
    "description": (
        "Entry Recorder — Truck Loading Record System\n\n"
        "Entry Recorder is a single-user, server-rendered web app built to replace "
        "a manufacturing client's paper logbook for tracking truck loading "
        "records. Every entry captures one truck-loading event: the vehicle, the "
        "date, a globally-shared loading stage (rolls, net weight, workers — one "
        "combined loading crew handles every truck regardless of source), and, "
        "separately, the weight/roll figures each of the client's three "
        "production plants contributed to that load. It's genuinely in daily use, "
        "not a demo — the client reviews and edits real records through it.\n\n"
        "Feature Breakdown\n\n"
        "- Entry management — create, edit, and delete truck-loading records "
        "through plain server-rendered forms; a paginated home-page table (30 "
        "rows/page) with date and vehicle-number search, both narrowing the full "
        "dataset server-side rather than just the current page.\n"
        "- Bulk actions — row checkboxes plus a floating selection bar (Edit / "
        "Group / Delete / Download), each button enabling only when the current "
        "selection count makes it valid (e.g. Edit needs exactly one row).\n"
        "- Batches — entries can be grouped into named batches, and an entry can "
        "belong to multiple batches at once (deliberately many-to-many, corrected "
        "mid-development from an earlier one-batch-per-entry design). Batches get "
        "their own searchable, paginated list, a read-only detail page, and an "
        "edit page for renaming, adding, or removing entries.\n"
        "- PDF export — a landscape-A4, multi-section PDF (built with ReportLab) "
        "covering all records, the last 10/50/100, an arbitrary hand-picked "
        "selection, or a specific batch. A \"Save by Range\" picker generates "
        "dynamic 100-record range buttons for large tables, so any slice of a "
        "multi-thousand-row ledger stays a couple of clicks away.\n"
        "- Account security — a custom login with lockout after repeated failed "
        "attempts, a Forgot Password flow (email OTP, rate-limited against "
        "username enumeration and email-guessing), and an Account Settings page "
        "for changing email (OTP-verified) and password.\n"
        "- Toast notifications and a custom confirm dialog replace native browser "
        "alerts/confirms site-wide, so destructive actions and background "
        "fetch/AJAX flows all get consistent, styled feedback.\n\n"
        "Tech Stack\n\n"
        "- Python, Django, server-rendered templates\n"
        "- PostgreSQL, both locally and in production (originally SQLite/no "
        "database chosen yet during early development)\n"
        "- A small Node/esbuild pipeline bundling client-side JS, with Zod for "
        "client-side form validation\n"
        "- django-anymail (SendGrid HTTP-API backend) for transactional OTP email\n"
        "- ReportLab for PDF generation\n"
        "- Render (hosting) + Neon (managed Postgres) + WhiteNoise (static files) "
        "+ gunicorn\n\n"
        "From Local Development to a Live Deployment\n\n"
        "Netlify was the first deployment target considered and was ruled out "
        "outright — it's a static/serverless host with no persistent process or "
        "writable filesystem, and this app is fully stateful (login sessions, a "
        "real database, PDF generation). Render was picked instead: free, no "
        "card required, and deploys straight from GitHub.\n\n"
        "The database moved twice. It started on Render's own free-tier managed "
        "Postgres, which expires 90 days after creation — a real deadline, not a "
        "hypothetical one. After evaluating Supabase (free-tier projects pause "
        "after 7 days of inactivity, too risky for a lightly-used single-admin "
        "app) and CockroachDB Serverless (wire-compatible but a different "
        "underlying engine), the database was migrated to Neon, an external "
        "always-free Postgres provider. The migration itself used pg_dump/"
        "pg_restore, verified by comparing row counts table-by-table between the "
        "old and new databases before cutting the live app over, and confirmed "
        "again by checking the live site's real entry count after deploy.\n\n"
        "Production email broke in a way local testing never caught: OTP emails "
        "for Forgot Password and Change Email failed with a raw \"Network is "
        "unreachable\" socket error when trying to reach smtp.gmail.com. "
        "Root-caused via Render's own log output rather than guessed at: "
        "Render's platform doesn't reliably support arbitrary outbound raw TCP "
        "(SMTP) connections, only HTTP(S) egress. The fix was to migrate off raw "
        "SMTP entirely to django-anymail's SendGrid HTTP-API backend — the "
        "call site (send_mail()) needed zero changes, only the settings and "
        "environment variables underneath it.\n\n"
        "A second production-only bug surfaced only when actually running "
        "migrations against a real Postgres database instead of the SQLite used "
        "day-to-day: a migration's AddField step for a slug column relied on "
        "SlugField's own default indexing behavior, which silently created an "
        "extra Postgres-specific index that a later step in the same migration "
        "then collided with while adding a uniqueness constraint. SQLite had "
        "masked this completely. It was caught and fixed by actually running the "
        "full migration/build/test pipeline against a throwaway Postgres "
        "container before trusting the deploy, not by reading the code and "
        "assuming it was fine.\n\n"
        "The codebase also went through a full audit pass from four specialized "
        "review focuses — cross-file duplication/dead code, per-site code "
        "quality and reliability, security, and mobile/responsive layout — which "
        "is where the login lockout, the rate-limited forgot-password endpoints, "
        "PDF-field escaping (a free-text remark field was being passed "
        "unescaped into ReportLab's markup-interpreting Paragraph renderer), "
        "and several mobile touch-target and viewport fixes came from, on top of "
        "the deployment-driven hardening above (DEBUG moved from hardcoded True "
        "to environment-controlled, with cookie/HSTS security gated behind it).\n\n"
        "Current Status\n\n"
        "Deployed and live on Render, backed by Neon Postgres, and in active "
        "real-world use for the client's day-to-day truck-loading records — "
        "entry management, batching, bulk actions, search, and PDF export are "
        "all fully live. One piece is still mid-rollout: production email "
        "credentials (a verified SendGrid sender) haven't been filled in on "
        "Render yet, so the Forgot Password / Change Email OTP flows work "
        "end-to-end locally but not yet on the live site.\n\n"
        "What This Project Demonstrates\n\n"
        "Modeling a real operational workflow that took two corrections to get "
        "right — a loading stage first modeled as per-plant, then corrected to "
        "genuinely global once the actual physical process was understood, and "
        "batch grouping rebuilt from a one-batch-per-entry foreign key into a "
        "proper many-to-many relationship once the real requirement (an entry "
        "can belong to several batches at once) became clear. Root-causing two "
        "distinct production-only failures — a platform-level outbound-TCP "
        "restriction masquerading as a generic socket error, and a database-"
        "engine-specific migration ordering bug SQLite couldn't reproduce — down "
        "to their actual underlying cause rather than patching the symptom. A "
        "real security pass: authentication brute-force protection, "
        "enumeration-resistant error messages, PDF markup-injection prevention, "
        "and validating resolved database rows rather than trusting "
        "client-submitted IDs. And iterating UI/UX details — pagination link "
        "grouping, mobile touch targets, a custom confirm dialog replacing "
        "native browser alerts — directly against real client feedback on a "
        "tool someone actually uses every day."
    ),
    "category": "Web App",
    "role": "Freelance Developer",
    "year": 2026,
    "status": "Live",
    "github_url": "https://github.com/shahbazkhan74659-crypto/RecordEntryApp",
    "live_url": "https://entryrecorder.onrender.com",
    "order": 1,
    "featured": True,
}


def seed_second_project(apps, schema_editor):
    Tag = apps.get_model("projects", "Tag")
    Project = apps.get_model("projects", "Project")

    tags = [Tag.objects.get_or_create(name=name)[0] for name in REAL_TAGS]
    project = Project.objects.create(**REAL_PROJECT)
    project.tags.set(tags)

    Project.objects.filter(slug="ts-library").update(featured=False, order=2)


def unseed_second_project(apps, schema_editor):
    Project = apps.get_model("projects", "Project")

    Project.objects.filter(slug=REAL_PROJECT["slug"]).delete()
    Project.objects.filter(slug="ts-library").update(featured=True, order=1)


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0011_seed_real_first_project"),
    ]

    operations = [
        migrations.RunPython(seed_second_project, unseed_second_project),
    ]
