from django.db import migrations


def migrate_project_tags(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Tag = apps.get_model("projects", "Tag")
    for project in Project.objects.all():
        tokens = [t.strip() for t in project.tags.split(",") if t.strip()]
        tags = [Tag.objects.get_or_create(name=token)[0] for token in tokens]
        project.tags_m2m.set(tags)


def reverse_migrate_project_tags(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    for project in Project.objects.all():
        project.tags_m2m.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_tags_m2m_add'),
    ]

    operations = [
        migrations.RunPython(migrate_project_tags, reverse_migrate_project_tags),
    ]
