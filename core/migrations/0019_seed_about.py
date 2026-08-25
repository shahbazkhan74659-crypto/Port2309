from django.db import migrations

ABOUT = {
    "eyebrow": "ABOUT ME",
    "title_line_one": "WHO'S",
    "title_line_two": "BEHIND THIS.",
    "lede": (
        "Developer, writer, and explorer—building ideas, exploring possibilities, "
        "and creating things that feel worth making."
    ),
    "background_heading": "Background",
    "background_paragraph": (
        "I'm based in Silvassa, Dadra & Nagar Haveli, where I completed a Diploma in "
        "Information Technology after 10th grade. I build full-stack, production-ready "
        "websites and applications, and I'm currently putting those skills into practice "
        "through freelancing."
    ),
    "care_heading": "What I care about",
    "care_paragraph": (
        "I care about solving real-world business problems with technology—building "
        "practical systems that improve workflows, reduce complexity, and create "
        "measurable value."
    ),
    "philosophy_eyebrow": "PHILOSOPHY",
    "philosophy_quote": (
        "Code is not merely written to make things work, but to give ideas a structure "
        "through which they can exist."
    ),
    "skills_eyebrow": "SKILLS & TOOLS",
    "languages_label": "Languages",
    "languages": "Python, Java, JavaScript, HTML/CSS",
    "frameworks_label": "Frameworks & Tools",
    "frameworks": "Django, Spring Boot, React, Tailwind CSS, AJAX, Relational DB",
    "learning_label": "Currently learning",
    "learning": "AI Agents, Autonomous Systems",
    "going_eyebrow": "WHERE THIS IS GOING",
    "going_paragraph": (
        "I'm currently building a personal AI agent designed to interact with my digital "
        "world through voice. It can control my laptop, launch applications, perform "
        "tasks, communicate naturally through voice, and eventually extend that control "
        "to my phone and other connected devices."
    ),
}


def seed_about(apps, schema_editor):
    About = apps.get_model("core", "About")
    if not About.objects.exists():
        About.objects.create(**ABOUT)


def unseed_about(apps, schema_editor):
    About = apps.get_model("core", "About")
    About.objects.filter(eyebrow=ABOUT["eyebrow"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_about'),
    ]

    operations = [
        migrations.RunPython(seed_about, unseed_about),
    ]
