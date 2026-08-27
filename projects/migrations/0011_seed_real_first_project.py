from django.db import migrations

PLACEHOLDER_SLUGS = ["project-one", "project-two", "project-three"]
PLACEHOLDER_TAG_NAME = "Tag"

REAL_TAGS = ["Java", "Spring Boot", "Thymeleaf", "MySQL", "Docker"]

REAL_PROJECT = {
    "title": "TS Library",
    "slug": "ts-library",
    "short_description": (
        "A server-rendered library management system for tracking books, "
        "members, issues, and returns — built with Spring Boot, Thymeleaf, "
        "and MySQL."
    ),
    "description": (
        "TS Library — Library Management System\n\n"
        "TS Library is a server-rendered library management system built to handle "
        "the day-to-day operations of a small library: cataloging books, registering "
        "members, issuing books on loan, and processing returns, all backed by a live "
        "dashboard of key stats.\n\n"
        "Overview\n\n"
        "The application is built with a classic, server-rendered architecture — "
        "Spring Boot on the backend, Thymeleaf for HTML rendering, and MySQL for "
        "persistence. There is no separate frontend framework or API layer; every "
        "page is rendered on the server and returned as HTML, keeping the stack "
        "simple, fast to reason about, and easy to deploy as a single service.\n\n"
        "The core workflow the app supports:\n"
        "1. A librarian adds books to the catalog, each with a title, author, "
        "category, published date, and a starting quantity.\n"
        "2. Members are registered with their name, email, mobile number, address, "
        "and join date.\n"
        "3. When a member wants to borrow a book, staff issue it to them with a due "
        "date. The book's available quantity is decremented automatically.\n"
        "4. When the book comes back, staff process the return. The system records "
        "the return in history and restores the book's available quantity.\n"
        "5. At any point, the dashboard shows a live summary: total books, available "
        "books, issued books, and total members.\n\n"
        "Feature Breakdown\n\n"
        "- Dashboard — A landing page summarizing total books, available books, "
        "currently issued books, and total registered members, giving staff an "
        "at-a-glance view of library state.\n"
        "- Book management — Add, list, and delete books. Each book tracks both its "
        "total quantity and its currently available quantity, so the system always "
        "knows how many copies of a title can still be issued.\n"
        "- Member management — Add, list, and delete members, with contact and "
        "address details stored for each.\n"
        "- Issue books — Staff can issue any available book to a registered member, "
        "specifying a due date. The system automatically decrements the book's "
        "available-quantity counter so the catalog stays accurate in real time.\n"
        "- Return books — Returning a book records the transaction in a dedicated "
        "return-history table (capturing the book, member, issue date, and return "
        "date) and restores the book's available quantity.\n"
        "- About page — A static informational page.\n\n"
        "Data Model\n\n"
        "The application is built around four core JPA entities:\n"
        "- Book (table books) — title, author, category, publishedDate, quantity, "
        "availableQuantity.\n"
        "- Member (table members) — name, email, mobile, address, joinedDate.\n"
        "- IssuedBook (table issued_books) — bookId, bookName, memberId, memberName, "
        "issueDate, dueDate.\n"
        "- ReturnedBook (table returned_books) — bookId, bookName, memberId, "
        "memberName, issueDate, returnDate.\n\n"
        "Rather than a fully normalized relational schema with foreign keys "
        "everywhere, IssuedBook and ReturnedBook denormalize the book and member "
        "names alongside their IDs — a pragmatic choice that keeps issue/return "
        "history readable even if a book or member record is later modified or "
        "deleted.\n\n"
        "Schema management uses Hibernate's ddl-auto=update setting, so tables are "
        "created and evolved automatically on startup rather than through manual "
        "migration scripts.\n\n"
        "Tech Stack\n\n"
        "- Java 21\n"
        "- Spring Boot 3.5 (Spring Web, Spring Data JPA, Thymeleaf)\n"
        "- MySQL, via the mysql-connector-j driver\n"
        "- Lombok, to cut down entity/DTO boilerplate\n"
        "- Maven, with the Maven Wrapper so no local Maven install is required\n"
        "- Docker, for containerized deployment (multi-stage build)\n\n"
        "Routes\n\n"
        "The application exposes a straightforward set of server-rendered routes:\n"
        "- GET / — dashboard with live stats\n"
        "- GET /books — list all books\n"
        "- GET /addbooks / POST /addbooks — add-book form and submission\n"
        "- GET /deletebook/{id} — delete a book\n"
        "- GET /members — list all members\n"
        "- GET /addmembers / POST /addmembers — add-member form and submission\n"
        "- GET /deletemember/{id} — delete a member\n"
        "- GET /issuebook/{id} — issue-book form for a given book\n"
        "- POST /issuebook — process issuing a book to a member\n"
        "- GET /returnbooks — list returned books\n"
        "- GET /returnbook/{id} — process returning an issued book\n"
        "- GET /about — static about page\n"
        "- GET /health — lightweight, DB-free health check used by the hosting "
        "platform\n\n"
        "Architecture Notes\n\n"
        "All application routes are handled by a single HomeController, with "
        "entities and Spring Data JPA repositories organized cleanly under entity/ "
        "and repository/ packages. The /health endpoint is deliberately separated "
        "from the dashboard: it returns a plain \"OK\" response with no database "
        "access at all, which turned out to matter a great deal for reliable "
        "deployment (see below).\n\n"
        "From Local Development to a Live Deployment\n\n"
        "Getting this from \"runs on localhost\" to \"live on the internet, for free, "
        "forever\" was its own project within the project, and involved solving a "
        "series of real infrastructure problems rather than just clicking deploy:\n\n"
        "Choosing a hosting combination. Render's free tier only offers managed "
        "PostgreSQL, and even that expires after 30 days — not a fit for an app "
        "built on MySQL. Rather than change the app's database engine just to fit a "
        "host's free tier, the database was hosted separately on Aiven, whose free "
        "MySQL tier is genuinely free forever (1GB storage/RAM, no card required, no "
        "expiry), while Render continued to host the web service itself.\n\n"
        "Making configuration environment-driven. The datasource URL and server "
        "port were changed to read from environment variables with local defaults "
        "preserved (${SPRING_DATASOURCE_URL:jdbc:mysql://localhost:3306/library_db}, "
        "${PORT:8080}), so the exact same code and jar run unmodified in local "
        "development and in production — verified by booting the packaged jar with "
        "and without overrides and confirming both paths behave correctly.\n\n"
        "Containerizing the app. A multi-stage Dockerfile builds the app with Maven "
        "on eclipse-temurin:21 and packages the resulting jar into a slim "
        "eclipse-temurin:21-jre-alpine runtime image, paired with a render.yaml "
        "Blueprint that provisions the Render web service (Docker runtime, free "
        "plan) and prompts for the required secrets rather than committing them.\n\n"
        "Debugging a corrupted environment variable. An early deploy failed with a "
        "cryptic Hibernate/HikariCP error claiming it couldn't accept the JDBC URL. "
        "The root cause turned out to be a stray Windows clipboard-history paste "
        "(Win+V) that had spliced extra text into the middle of the URL when it was "
        "entered into Render's dashboard. Retyping the variable directly, rather "
        "than pasting from clipboard history, resolved it.\n\n"
        "Debugging a deploy timeout that wasn't really a timeout. A later deploy "
        "showed the app successfully booting and serving real requests in its logs, "
        "yet Render still reported the deploy as timed out and failed. The cause: "
        "the health-check path was pointed at the dashboard route, which performs "
        "five database round-trips (three counts plus two full-table scans) against "
        "a remote database on every single request — roughly 2.5 seconds per hit, "
        "dominated by cross-region network latency to Aiven. Render's repeated "
        "health-check polling against that heavy endpoint exceeded its timeout "
        "window even though the application itself was perfectly healthy. The fix "
        "was to add a dedicated /health endpoint that does no database work at all "
        "and point Render's health check at that instead — verified locally to "
        "respond in about 18ms versus the dashboard's ~2.5 seconds.\n\n"
        "Recovering lost local database credentials. At one point the local MySQL "
        "root credentials were forgotten. Rather than guessing, they were recovered "
        "properly: stopping the MySQL service, restarting the server manually in "
        "--skip-grant-tables safe mode, and — specific to Windows — also passing "
        "--enable-named-pipe, since Windows (unlike Linux) provides no local socket "
        "access in safe mode unless a named pipe is explicitly enabled. From there, "
        "a fresh dedicated account was created with the correct privileges, and the "
        "server was restarted normally.\n\n"
        "Finding and resolving schema drift. When seeding the production database "
        "with the same content as local development, a direct dump failed with an "
        "\"unknown column\" error. Investigation revealed the local books table "
        "still carried seven legacy columns left over from an earlier version of "
        "the entity, which Hibernate's additive ddl-auto=update had never removed "
        "even after the entity itself was simplified. The dump was regenerated "
        "using only the columns the current entity actually defines, and the "
        "production seed succeeded — verified by matching row counts across every "
        "table (37 books, 11 members, 2 issued, 4 returned) and by confirming the "
        "live site rendered the seeded catalog correctly.\n\n"
        "Current Status\n\n"
        "The application is deployed and live, running as a Docker container on "
        "Render's free tier with its data persisted in a free-tier Aiven MySQL "
        "instance. Because Render's free tier spins containers down after 15 "
        "minutes of inactivity, the first request after a quiet period takes longer "
        "(a cold start) while the container spins back up — normal free-tier "
        "behavior rather than a defect.\n\n"
        "What This Project Demonstrates\n\n"
        "Beyond the CRUD feature set itself, this project reflects a full path from "
        "a working local application to a genuinely deployed, publicly reachable "
        "service on a zero-cost hosting stack: environment-driven configuration "
        "that behaves identically locally and in production, containerization, "
        "diagnosing real infrastructure failures (a mangled environment variable, a "
        "misconfigured health check masking a healthy app, drifted schema between "
        "environments), and recovering from an operational mistake (lost database "
        "credentials) using the correct, non-destructive procedure rather than a "
        "shortcut."
    ),
    "category": "Web App",
    "role": "Solo Developer",
    "year": 2026,
    "status": "Shipped",
    "github_url": "https://github.com/shahbazkhan74659-crypto/TS_Library_Management_System.git",
    "live_url": "https://ts-library.onrender.com",
    "order": 1,
    "featured": True,
}


def seed_real_project(apps, schema_editor):
    Tag = apps.get_model("projects", "Tag")
    Project = apps.get_model("projects", "Project")

    Project.objects.filter(slug__in=PLACEHOLDER_SLUGS).delete()
    Tag.objects.filter(
        name=PLACEHOLDER_TAG_NAME, projects__isnull=True, posts__isnull=True
    ).delete()

    tags = [Tag.objects.get_or_create(name=name)[0] for name in REAL_TAGS]
    project = Project.objects.create(**REAL_PROJECT)
    project.tags.set(tags)


def unseed_real_project(apps, schema_editor):
    Project = apps.get_model("projects", "Project")

    Project.objects.filter(slug=REAL_PROJECT["slug"]).delete()

    Project.objects.create(
        title="Project One",
        slug="project-one",
        short_description="One-line placeholder description of this project goes here.",
        category="Category",
        role="Role",
        year=2026,
        status="Active",
        order=1,
        featured=True,
    )
    Project.objects.create(
        title="Project Two",
        slug="project-two",
        short_description="One-line placeholder description of this project goes here.",
        category="Category",
        role="Role",
        year=2025,
        status="Shipped",
        order=2,
        featured=False,
    )
    Project.objects.create(
        title="Project Three",
        slug="project-three",
        short_description="One-line placeholder description of this project goes here.",
        category="Category",
        role="Role",
        year=2025,
        status="In progress",
        order=3,
        featured=False,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0010_project_description_projectimage"),
    ]

    operations = [
        migrations.RunPython(seed_real_project, unseed_real_project),
    ]
