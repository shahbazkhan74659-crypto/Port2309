from django.db import migrations

SLUG = "entry-recorder"
LIVE_URL = "https://entryrecorder.onrender.com"


def remove_live_url(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(slug=SLUG).update(live_url="")


def restore_live_url(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(slug=SLUG).update(live_url=LIVE_URL)


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0012_seed_second_real_project"),
    ]

    operations = [
        migrations.RunPython(remove_live_url, restore_live_url),
    ]
