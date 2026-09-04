from django.db import migrations

OLD_BACKGROUND_PARAGRAPH = (
    "I'm based in Silvassa, Dadra & Nagar Haveli, where I completed a Diploma in "
    "Information Technology after 10th grade. I build full-stack, production-ready "
    "websites and applications, and I'm currently putting those skills into practice "
    "through freelancing."
)
NEW_BACKGROUND_PARAGRAPH = (
    OLD_BACKGROUND_PARAGRAPH
    + " I'm available for freelance and remote work across Silvassa, Vapi, Daman, "
    "and the wider Dadra & Nagar Haveli region."
)

OLD_AVAILABLE_FOR = "Freelance / contract"
NEW_AVAILABLE_FOR = "Freelance / contract — Silvassa, Vapi, Daman & DNH"


def apply_local_seo_copy(apps, schema_editor):
    About = apps.get_model("core", "About")
    about = About.objects.first()
    if about is not None:
        about.background_paragraph = NEW_BACKGROUND_PARAGRAPH
        about.save(update_fields=["background_paragraph"])

    ContactEmail = apps.get_model("core", "ContactEmail")
    contact = ContactEmail.objects.first()
    if contact is not None:
        contact.available_for = NEW_AVAILABLE_FOR
        contact.save(update_fields=["available_for"])


def revert_local_seo_copy(apps, schema_editor):
    About = apps.get_model("core", "About")
    about = About.objects.first()
    if about is not None:
        about.background_paragraph = OLD_BACKGROUND_PARAGRAPH
        about.save(update_fields=["background_paragraph"])

    ContactEmail = apps.get_model("core", "ContactEmail")
    contact = ContactEmail.objects.first()
    if contact is not None:
        contact.available_for = OLD_AVAILABLE_FOR
        contact.save(update_fields=["available_for"])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_alter_resume_file'),
    ]

    operations = [
        migrations.RunPython(apply_local_seo_copy, revert_local_seo_copy),
    ]
