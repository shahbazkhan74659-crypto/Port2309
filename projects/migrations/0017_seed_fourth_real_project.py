from django.db import migrations

REAL_TAGS = ["Next.js", "React", "TypeScript", "PostgreSQL", "REST APIs"]

REAL_PROJECT = {
    "title": "Track Me",
    "slug": "track-me",
    "short_description": (
        "A personal Next.js/TypeScript attendance and salary tracker — a "
        "clickable calendar logs daily status and advances, with live "
        "earned/net-payable totals, deployed on Render against Neon "
        "PostgreSQL."
    ),
    "description": (
        "Track Me — Personal Attendance & Salary Tracker\n\n"
        "Track Me is a personal, single-owner tool for logging day-by-day "
        "attendance (Present / Half-Day / Leave) and any salary advances "
        "taken, with earned and net-payable salary recalculating live as "
        "each day is logged — replacing an ad hoc manual tally with one "
        "calendar-driven source of truth.\n\n"
        "Overview\n\n"
        "The app started as a client-approved, fully interactive visual "
        "prototype built with Claude Design Components and published as a "
        "Claude Artifact — kept unchanged in the repo as the permanent "
        "visual/interaction reference. Production code was then written "
        "fresh against that reference: a real Next.js/TypeScript frontend "
        "wired end to end to a real PostgreSQL-backed API, not a port or a "
        "reskin of the prototype's in-memory sample data.\n\n"
        "Feature Breakdown\n\n"
        "- Calendar-based Home page — a month/year-navigable calendar where "
        "every date is clickable; a fixed 6x7 grid built with dependency-free, "
        "leap-year-correct, UTC-anchored date arithmetic.\n"
        "- Date-entry modal — clicking any date opens a popup to set its "
        "status (Present / Half-Day / Leave) and, optionally, a salary "
        "advance taken that day; Save is disabled until a status is chosen, "
        "matching the approved prototype's exact rule.\n"
        "- Live stat cards — Earned So Far, Advance Taken, and Net Payable "
        "for the current month, recalculated on the server after every save "
        "and re-fetched immediately so the UI never shows stale totals.\n"
        "- Salary Setup — the owner sets one per-day rate; present/half-day "
        "pay, monthly totals, and net payable are all derived from it "
        "automatically, with no other manual entry.\n"
        "- Real login gate — a single owner-provisioned account (created via "
        "a manual seed script, not a signup form), DB-backed sessions, "
        "bcrypt password hashing, and in-memory rate limiting on failed "
        "login attempts.\n"
        "- Mobile-responsive layout — every card and the calendar itself "
        "reflow down to phone-width screens, including a mobile-only "
        "section reorder (calendar before stat cards) driven entirely by "
        "CSS `order`, not duplicated markup.\n\n"
        "Tech Stack\n\n"
        "- Next.js 16 (App Router) with TypeScript, React 19\n"
        "- PostgreSQL — a local instance for development, Neon (serverless "
        "Postgres) for production — accessed through a dedicated, "
        "least-privilege database role rather than the superuser/owner role "
        "in either environment\n"
        "- Plain `fetch`/`useState`/`useEffect` throughout, no ORM and no "
        "data-fetching library — a deliberate stack lock kept consistent "
        "across the whole codebase, including its own test scripts\n"
        "- bcryptjs for password hashing; opaque random-token sessions "
        "stored server-side, not JWTs\n"
        "- Playwright for both end-to-end tests (real browser, real "
        "database, a dedicated test account) and isolated component tests\n"
        "- Deployed on Render's free tier via a versioned `render.yaml` "
        "Blueprint, with an UptimeRobot monitor pinging a dependency-free "
        "`/api/health` endpoint every 5 minutes to counter the free tier's "
        "15-minute idle spin-down\n\n"
        "From Local Development to a Live Deployment\n\n"
        "Every date/time calculation is computed in the owner's real "
        "timezone (Asia/Kolkata) via `Intl.DateTimeFormat`, independent of "
        "whatever timezone the server process happens to run in — a detail "
        "that matters specifically because Render, Neon, and a Windows dev "
        "machine are three different timezones by default, and \"today\" "
        "silently disagreeing between them would corrupt exactly the "
        "day-by-day log this app exists to keep accurate.\n\n"
        "The Render deploy itself hit two real failures before going live. "
        "First, `render.yaml` set `NODE_ENV=production` for the whole "
        "service, which also reached the build step — npm's "
        "`NODE_ENV=production` behavior silently omits devDependencies, so "
        "`next build`'s own TypeScript type-check lost the `typescript`/"
        "`@types/*` packages it needed and the build failed. Second, even "
        "after removing that variable from `render.yaml`, a plain `git "
        "push` only triggers a code redeploy, not a full Blueprint sync "
        "that reconciles environment variables against the file — the "
        "stale `NODE_ENV` had to be deleted directly from Render's "
        "Environment tab before a rebuild actually picked up the fix. The "
        "resulting deploy was verified directly, not just assumed from a "
        "green build: `curl` against `/api/health` returned `200 "
        "{\"status\":\"ok\"}` with every security header present, and the "
        "root URL served the real dark-themed login page in a live "
        "browser — confirming the app was genuinely serving traffic "
        "against the Neon database.\n\n"
        "Current Status\n\n"
        "Live in production on Render (`https://track-me-9fgr.onrender.com`), "
        "backed by Neon PostgreSQL, with a working login gate, full CRUD "
        "on attendance entries, live salary calculations, and an "
        "UptimeRobot monitor confirmed up. The approved interactive "
        "prototype still exists, unchanged, as a permanent visual/"
        "interaction reference. What remains is a final round of live, "
        "authenticated end-to-end verification using the owner's own real "
        "account and devices rather than the automated test account.\n\n"
        "What This Project Demonstrates\n\n"
        "A complete path from an approved interactive design prototype to "
        "a genuinely deployed, database-backed production app: building "
        "the backend API surface and its persistence layer before any real "
        "frontend existed and verifying it with a standalone HTTP test "
        "script; timezone-safe date handling treated as a first-class "
        "correctness concern rather than an afterthought; a deliberately "
        "minimal, framework-light frontend stack held consistent across an "
        "entire codebase rather than reached for piecemeal; and diagnosing "
        "real platform-specific deployment failures (an environment "
        "variable that broke the build silently, a config change that "
        "needed a full Blueprint sync rather than a plain push) down to "
        "their actual root cause instead of working around the symptom."
    ),
    "category": "Web App",
    "role": "Solo Developer",
    "year": 2026,
    "status": "Live",
    "github_url": "https://github.com/shahbazkhan74659-crypto/Track-Me.git",
    "live_url": "https://track-me-9fgr.onrender.com",
    "order": 2,
    "featured": False,
}


def seed_fourth_project(apps, schema_editor):
    Tag = apps.get_model("projects", "Tag")
    Project = apps.get_model("projects", "Project")

    tags = [Tag.objects.get_or_create(name=name)[0] for name in REAL_TAGS]
    project = Project.objects.create(**REAL_PROJECT)
    project.tags.set(tags)

    Project.objects.filter(slug="loadgate").update(order=3)
    Project.objects.filter(slug="ts-library").update(order=4)


def unseed_fourth_project(apps, schema_editor):
    Project = apps.get_model("projects", "Project")

    Project.objects.filter(slug=REAL_PROJECT["slug"]).delete()
    Project.objects.filter(slug="loadgate").update(order=2)
    Project.objects.filter(slug="ts-library").update(order=3)


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0016_fire_service_custom_domain"),
    ]

    operations = [
        migrations.RunPython(seed_fourth_project, unseed_fourth_project),
    ]
