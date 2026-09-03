from django.db import migrations

OLD_URL = "https://iconic-techno-service.onrender.com"
NEW_URL = "https://iconictechnoservice.com"


def update_live_url(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(slug="fire-service-website").update(live_url=NEW_URL)


def revert_live_url(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(slug="fire-service-website").update(live_url=OLD_URL)


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0015_seed_third_real_project"),
    ]

    operations = [
        migrations.RunPython(update_live_url, revert_live_url),
    ]
