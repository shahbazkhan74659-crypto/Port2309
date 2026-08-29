from django.db import migrations


NEW_INTRO_SUB = (
    "Information Technology diploma student skilled in Python, Django, "
    "JavaScript, and relational databases — seeking a Web Developer role to "
    "apply my skills, contribute to real projects, and keep growing."
)

NEW_LANGUAGES = ["Python", "JavaScript", "TypeScript", "HTML/CSS"]
NEW_FRAMEWORKS = [
    "Django",
    "Tailwind CSS",
    "React Island",
    "Spring Boot",
    "REST APIs",
    "AJAX",
    "Relational DB",
    "Git & GitHub",
]

OLD_LANGUAGES = ["Python", "Java", "JavaScript", "HTML/CSS"]
OLD_FRAMEWORKS = ["Django", "Spring Boot", "React", "Tailwind CSS", "AJAX", "Relational DB"]
OLD_INTRO_SUB = "Placeholder experience and education below — real content goes here once it's ready."

NEW_EXPERIENCE = [
    {
        "role": "Freelance Web Developer",
        "organization": "Iconic Techno Service (Freelance)",
        "period": "2 Months",
        "description": (
            "Built a full-stack Fire & Safety Systems website with Django 5.2 + "
            "PostgreSQL and React (TypeScript) islands, a custom Admin Hub with "
            "DRF REST API, SEO, and production deployment on Render with Neon "
            "Postgres + Cloudinary."
        ),
        "order": 1,
    },
]

OLD_EXPERIENCE = [
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

NEW_EDUCATION = [
    {
        "degree": "Diploma in Information Technology",
        "institution": "Dr. B.B.A. Government Polytechnic, Karad (GTU)",
        "period": "2026",
        "description": "CGPA: 7.81",
        "order": 1,
    },
]

OLD_EDUCATION = [
    {
        "degree": "Degree / Program Placeholder",
        "institution": "Institution Placeholder",
        "period": "20XX — 20XX",
        "description": "One-line placeholder description goes here.",
        "order": 1,
    },
]


def _replace_experience(ResumeExperience, entries):
    ResumeExperience.objects.all().delete()
    for entry in entries:
        ResumeExperience.objects.create(**entry)


def _replace_education(ResumeEducation, entries):
    ResumeEducation.objects.all().delete()
    for entry in entries:
        ResumeEducation.objects.create(**entry)


def seed_real_resume(apps, schema_editor):
    ResumePage = apps.get_model("core", "ResumePage")
    ResumeExperience = apps.get_model("core", "ResumeExperience")
    ResumeEducation = apps.get_model("core", "ResumeEducation")
    Tag = apps.get_model("projects", "Tag")

    page = ResumePage.objects.first()
    if page is not None:
        page.intro_sub = NEW_INTRO_SUB
        page.save()

        page.languages.clear()
        for name in NEW_LANGUAGES:
            tag, _ = Tag.objects.get_or_create(name=name)
            page.languages.add(tag)

        page.frameworks.clear()
        for name in NEW_FRAMEWORKS:
            tag, _ = Tag.objects.get_or_create(name=name)
            page.frameworks.add(tag)

    _replace_experience(ResumeExperience, NEW_EXPERIENCE)
    _replace_education(ResumeEducation, NEW_EDUCATION)


def unseed_real_resume(apps, schema_editor):
    ResumePage = apps.get_model("core", "ResumePage")
    ResumeExperience = apps.get_model("core", "ResumeExperience")
    ResumeEducation = apps.get_model("core", "ResumeEducation")
    Tag = apps.get_model("projects", "Tag")

    page = ResumePage.objects.first()
    if page is not None:
        page.intro_sub = OLD_INTRO_SUB
        page.save()

        page.languages.clear()
        for name in OLD_LANGUAGES:
            tag, _ = Tag.objects.get_or_create(name=name)
            page.languages.add(tag)

        page.frameworks.clear()
        for name in OLD_FRAMEWORKS:
            tag, _ = Tag.objects.get_or_create(name=name)
            page.frameworks.add(tag)

    _replace_experience(ResumeExperience, OLD_EXPERIENCE)
    _replace_education(ResumeEducation, OLD_EDUCATION)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0028_seed_resume_page"),
    ]

    operations = [
        migrations.RunPython(seed_real_resume, unseed_real_resume),
    ]
