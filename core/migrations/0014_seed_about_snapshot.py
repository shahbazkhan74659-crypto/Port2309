from django.db import migrations

ABOUT_SNAPSHOT = {
    "eyebrow": "A LITTLE ABOUT ME",
    "headline_one": "CURIOSITY.",
    "headline_two": "CREATION.",
    "headline_three": "EXPERIMENTATION.",
    "headline_sub": "Curiosity starts the question. Creation takes it somewhere new. Experimentation turns it into something real.",
    "paragraph": (
        "I'm a developer, writer, and explorer—drawn to the space where technology, ideas, and "
        "imagination meet. I build things to understand how they work, write to make sense of what I "
        "discover, and explore simply because there's always something new worth finding. My work is "
        "less about following a fixed path and more about turning curiosity into things that didn't "
        "exist before."
    ),
    "currently_label": "Currently",
    "currently_building": "An autonomous personal AI assistant",
    "currently_learning": "AI and autonomous systems",
    "currently_writing": 'A fantasy story, "The God Valley"',
    "currently_exploring": "Agentic AI tooling and autonomous workflows",
}


def seed_about_snapshot(apps, schema_editor):
    AboutSnapshot = apps.get_model("core", "AboutSnapshot")
    if not AboutSnapshot.objects.exists():
        AboutSnapshot.objects.create(**ABOUT_SNAPSHOT)


def unseed_about_snapshot(apps, schema_editor):
    AboutSnapshot = apps.get_model("core", "AboutSnapshot")
    AboutSnapshot.objects.filter(eyebrow=ABOUT_SNAPSHOT["eyebrow"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_aboutsnapshot'),
    ]

    operations = [
        migrations.RunPython(seed_about_snapshot, unseed_about_snapshot),
    ]
