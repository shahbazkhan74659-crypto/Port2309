from django.db import migrations

OLD_SLUG = "entry-recorder"
NEW_SLUG = "loadgate"

OLD_TITLE = "Entry Recorder"
NEW_TITLE = "LoadGate"


def rename_to_loadgate(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    project = Project.objects.get(slug=OLD_SLUG)
    project.title = NEW_TITLE
    project.slug = NEW_SLUG
    project.description = project.description.replace(OLD_TITLE, NEW_TITLE)
    project.save()


def rename_to_entry_recorder(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    project = Project.objects.get(slug=NEW_SLUG)
    project.title = OLD_TITLE
    project.slug = OLD_SLUG
    project.description = project.description.replace(NEW_TITLE, OLD_TITLE)
    project.save()


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0013_entry_recorder_remove_live_url"),
    ]

    operations = [
        migrations.RunPython(rename_to_loadgate, rename_to_entry_recorder),
    ]
