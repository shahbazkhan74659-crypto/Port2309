from django.db import migrations

PLACEHOLDER_TAGS = ["Tag One", "Tag Two", "Tag Three"]

PLACEHOLDER_POST = {
    "title": "Post Title One",
    "slug": "post-title-one",
    "short_description": "One-line placeholder excerpt of this post goes here.",
    "content": (
        "Placeholder body content for this post goes here. Replace with real writing "
        "once it's ready.\n\n"
        "This is a second placeholder paragraph, just to show how a longer post reads "
        "on the detail page."
    ),
    "published_at": "2026-01-01",
}


def seed_blog(apps, schema_editor):
    Tag = apps.get_model("projects", "Tag")
    Post = apps.get_model("projects", "Post")

    tags = [Tag.objects.get_or_create(name=name)[0] for name in PLACEHOLDER_TAGS]

    post = Post.objects.create(**PLACEHOLDER_POST)
    post.tags.set(tags)


def unseed_blog(apps, schema_editor):
    Post = apps.get_model("projects", "Post")
    Tag = apps.get_model("projects", "Tag")
    Post.objects.filter(slug=PLACEHOLDER_POST["slug"]).delete()
    Tag.objects.filter(name__in=PLACEHOLDER_TAGS).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_tags_finalize'),
    ]

    operations = [
        migrations.RunPython(seed_blog, unseed_blog),
    ]
