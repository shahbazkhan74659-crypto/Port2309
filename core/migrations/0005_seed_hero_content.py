from django.db import migrations

HERO_CONTENT = {
    "greeting": "HELLO, I'M SHAHBAZ.",
    "line_one": "I BUILD.",
    "line_two": "I WRITE.",
    "name_first": "SHAHBAZ",
    "name_last": "KHAN",
    "line_three": "I EXPLORE.",
    "roles": "DEVELOPER / FREELANCER / WRITER",
    "meta_line_one": "CURRENTLY EXPLORING AI & AUTONOMOUS SYSTEMS",
    "meta_line_two": "BUILDING A PERSONAL AI AGENT TO HANDLE MY WORK",
    "meta_line_three": "WRITING A FANTASY STORY BEYOND THIS WORLD",
    "year": "2026",
    "location": "SILVASSA, DADRA & NAGAR HAVELI",
}


def seed_hero_content(apps, schema_editor):
    HeroContent = apps.get_model("core", "HeroContent")
    if not HeroContent.objects.exists():
        HeroContent.objects.create(**HERO_CONTENT)


def unseed_hero_content(apps, schema_editor):
    HeroContent = apps.get_model("core", "HeroContent")
    HeroContent.objects.filter(greeting=HERO_CONTENT["greeting"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_herocontent'),
    ]

    operations = [
        migrations.RunPython(seed_hero_content, unseed_hero_content),
    ]
