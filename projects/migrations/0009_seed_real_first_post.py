from django.db import migrations

PLACEHOLDER_POST_SLUG = "post-title-one"
PLACEHOLDER_TAGS = ["Tag One", "Tag Two", "Tag Three"]

REAL_TAGS = ["Django", "Python", "Tailwind CSS", "Relational DB"]

REAL_POST = {
    "title": "Building This Portfolio",
    "slug": "building-this-portfolio",
    "short_description": (
        "Why this site started as a throwaway static mockup, got rebuilt from "
        "scratch in Django, and ended up storing almost everything about itself "
        "in its own database — including this post."
    ),
    "content": (
        "I didn't start this project by writing a Django app. I started it by "
        "building a single, disposable HTML file — one page, inline CSS, inline "
        "JavaScript, a fictional name, fake projects. The point wasn't to ship "
        "that file. The point was to stop guessing at layout and typography in "
        "my head and actually look at it, before committing to a real stack.\n\n"
        "Once the shape of the thing felt right, I threw the prototype away as "
        "production code and started over: a fresh Django project, Tailwind for "
        "styling, and a plan to add React only where a page genuinely needed "
        "interactivity, not everywhere by default. Early on I split the backend "
        "into exactly two apps — core for identity and site-wide routing, "
        "projects for my actual work — after briefly overengineering it into "
        "three. Two was enough. It still is.\n\n"
        "The rule I kept coming back to was simple: don't fabricate real content. "
        "Pages went live with honest, obviously-placeholder text — \"YOUR NAME,\" "
        "generic paragraphs — right up until my real bio, my real projects, or a "
        "real database model existed to back them. It made the site look "
        "unfinished for longer than I'd have liked, but it meant nothing on here "
        "was ever pretending to be real when it wasn't.\n\n"
        "Then, piece by piece, the content stopped being text sitting in template "
        "files and became rows in a database instead. The hero section, the About "
        "page, the contact links, the Hire Me copy — all of it moved into models "
        "I can edit from the admin without touching a line of code. Projects "
        "gained a real model with a slug-based detail page and a modal for "
        "browsing quickly. Tags stopped being comma-separated strings scattered "
        "across three different fields and became one shared Tag model, reused "
        "everywhere a tag shows up.\n\n"
        "The database itself moved too — from SQLite while I was figuring things "
        "out, to a real local PostgreSQL install for day-to-day development, with "
        "a managed Postgres instance on Neon waiting as the production target once "
        "this actually deploys.\n\n"
        "This post is the next piece of that same pattern. The Blog feature had "
        "working models, views, and templates before it had a single real word "
        "written in them — just a seeded placeholder post proving the plumbing "
        "worked. This is what replaces that placeholder: the first real thing I "
        "wrote for this blog, about the site the blog lives on. Everything else "
        "here still needs real content behind it — real projects, a real resume, "
        "more writing than just this. But it starts here."
    ),
    "published_at": "2026-08-26",
}


def seed_real_post(apps, schema_editor):
    Tag = apps.get_model("projects", "Tag")
    Post = apps.get_model("projects", "Post")

    Post.objects.filter(slug=PLACEHOLDER_POST_SLUG).delete()
    Tag.objects.filter(name__in=PLACEHOLDER_TAGS, posts__isnull=True, projects__isnull=True).delete()

    tags = [Tag.objects.get_or_create(name=name)[0] for name in REAL_TAGS]
    post = Post.objects.create(**REAL_POST)
    post.tags.set(tags)


def unseed_real_post(apps, schema_editor):
    Post = apps.get_model("projects", "Post")
    Tag = apps.get_model("projects", "Tag")

    Post.objects.filter(slug=REAL_POST["slug"]).delete()

    placeholder_tags = [Tag.objects.get_or_create(name=name)[0] for name in PLACEHOLDER_TAGS]
    placeholder_post = Post.objects.create(
        title="Post Title One",
        slug=PLACEHOLDER_POST_SLUG,
        short_description="One-line placeholder excerpt of this post goes here.",
        content=(
            "Placeholder body content for this post goes here. Replace with real writing "
            "once it's ready.\n\n"
            "This is a second placeholder paragraph, just to show how a longer post reads "
            "on the detail page."
        ),
        published_at="2026-01-01",
    )
    placeholder_post.tags.set(placeholder_tags)


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_seed_placeholder_blog'),
    ]

    operations = [
        migrations.RunPython(seed_real_post, unseed_real_post),
    ]
