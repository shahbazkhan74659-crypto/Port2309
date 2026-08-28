from django.db import migrations


LANGUAGES = ["Python", "Java", "JavaScript", "HTML/CSS"]
FRAMEWORKS = ["Django", "Spring Boot", "React", "Tailwind CSS", "AJAX", "Relational DB"]
LEARNING = ["AI Agents", "Autonomous Systems"]

EXPERIENCE = [
    {
        "role": "Role Placeholder",
        "organization": "Company / Client Placeholder",
        "period": "20XX — PRESENT",
        "description": "One-line placeholder description of this role goes here.",
        "order": 1,
    },
    {
        "role": "Role Placeholder",
        "organization": "Company / Client Placeholder",
        "period": "20XX — 20XX",
        "description": "One-line placeholder description of this role goes here.",
        "order": 2,
    },
]

EDUCATION = [
    {
        "degree": "Degree / Program Placeholder",
        "institution": "Institution Placeholder",
        "period": "20XX — 20XX",
        "description": "One-line placeholder description goes here.",
        "order": 1,
    },
]


def seed_resume(apps, schema_editor):
    ResumePage = apps.get_model("core", "ResumePage")
    ResumeExperience = apps.get_model("core", "ResumeExperience")
    ResumeEducation = apps.get_model("core", "ResumeEducation")
    Tag = apps.get_model("projects", "Tag")

    page = ResumePage.objects.create(
        intro_sub="Placeholder experience and education below — real content goes here once it's ready.",
        languages_label="Languages",
        frameworks_label="Frameworks & Tools",
        learning_label="Currently learning",
    )
    for name in LANGUAGES:
        tag, _ = Tag.objects.get_or_create(name=name)
        page.languages.add(tag)
    for name in FRAMEWORKS:
        tag, _ = Tag.objects.get_or_create(name=name)
        page.frameworks.add(tag)
    for name in LEARNING:
        tag, _ = Tag.objects.get_or_create(name=name)
        page.learning.add(tag)

    for entry in EXPERIENCE:
        ResumeExperience.objects.create(**entry)
    for entry in EDUCATION:
        ResumeEducation.objects.create(**entry)


def unseed_resume(apps, schema_editor):
    apps.get_model("core", "ResumePage").objects.all().delete()
    apps.get_model("core", "ResumeExperience").objects.all().delete()
    apps.get_model("core", "ResumeEducation").objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_resumeeducation_resumeexperience_resumepage"),
    ]

    operations = [
        migrations.RunPython(seed_resume, unseed_resume),
    ]
