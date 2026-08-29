from django.db import migrations


NEW_LANGUAGES = ["Python", "JavaScript", "TypeScript", "HTML/CSS"]
NEW_FRAMEWORKS = [
    "Django",
    "Tailwind CSS",
    "React Island",
    "Spring Boot",
    "REST APIs",
    "AJAX",
    "Relational DB",
    "Git & GitHub",
]

OLD_LANGUAGES = ["HTML/CSS", "Java", "JavaScript", "Python"]
OLD_FRAMEWORKS = ["AJAX", "Django", "React", "Relational DB", "Spring Boot", "Tailwind CSS"]


def _set_tags(page, field_name, names, Tag):
    manager = getattr(page, field_name)
    manager.clear()
    for name in names:
        tag, _ = Tag.objects.get_or_create(name=name)
        manager.add(tag)


def sync_about_skills(apps, schema_editor):
    About = apps.get_model("core", "About")
    Tag = apps.get_model("projects", "Tag")

    about = About.objects.first()
    if about is not None:
        _set_tags(about, "languages", NEW_LANGUAGES, Tag)
        _set_tags(about, "frameworks", NEW_FRAMEWORKS, Tag)


def unsync_about_skills(apps, schema_editor):
    About = apps.get_model("core", "About")
    Tag = apps.get_model("projects", "Tag")

    about = About.objects.first()
    if about is not None:
        _set_tags(about, "languages", OLD_LANGUAGES, Tag)
        _set_tags(about, "frameworks", OLD_FRAMEWORKS, Tag)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0029_seed_real_resume_content"),
    ]

    operations = [
        migrations.RunPython(sync_about_skills, unsync_about_skills),
    ]
