from pathlib import Path

from django.conf import settings
from django.core.files.base import ContentFile
from django.db import migrations

SOURCE_PATH = Path(settings.BASE_DIR) / "static" / "images" / "hero-portrait.png"


def backfill_portrait(apps, schema_editor):
    HeroContent = apps.get_model("core", "HeroContent")
    hero = HeroContent.objects.first()
    if hero is None or hero.portrait or not SOURCE_PATH.exists():
        return
    with open(SOURCE_PATH, "rb") as f:
        hero.portrait.save("hero-portrait.png", ContentFile(f.read()), save=True)


def clear_portrait(apps, schema_editor):
    HeroContent = apps.get_model("core", "HeroContent")
    hero = HeroContent.objects.first()
    if hero and hero.portrait:
        hero.portrait.delete(save=True)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_seed_hero_content'),
    ]

    operations = [
        migrations.RunPython(backfill_portrait, clear_portrait),
    ]
