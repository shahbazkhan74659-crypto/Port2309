from django.db import migrations


def migrate_about_skills(apps, schema_editor):
    About = apps.get_model("core", "About")
    Tag = apps.get_model("projects", "Tag")
    for about in About.objects.all():
        for field, m2m_field in (
            ("languages", "languages_m2m"),
            ("frameworks", "frameworks_m2m"),
            ("learning", "learning_m2m"),
        ):
            tokens = [t.strip() for t in getattr(about, field).split(",") if t.strip()]
            tags = [Tag.objects.get_or_create(name=token)[0] for token in tokens]
            getattr(about, m2m_field).set(tags)


def reverse_migrate_about_skills(apps, schema_editor):
    About = apps.get_model("core", "About")
    for about in About.objects.all():
        about.languages_m2m.clear()
        about.frameworks_m2m.clear()
        about.learning_m2m.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_about_skills_m2m_add'),
    ]

    operations = [
        migrations.RunPython(migrate_about_skills, reverse_migrate_about_skills),
    ]
