from django.db import migrations

GITHUB_DISPLAY = "github.com/shahbazkhan74659-crypto"
LINKEDIN_DISPLAY = "linkedin.com/in/shahbaz-khan-471aa2418"


def seed_contact_links(apps, schema_editor):
    ContactEmail = apps.get_model("core", "ContactEmail")
    contact = ContactEmail.objects.first()
    if contact is None:
        return
    contact.github_display = GITHUB_DISPLAY
    contact.linkedin_display = LINKEDIN_DISPLAY
    contact.save(update_fields=["github_display", "linkedin_display"])


def unseed_contact_links(apps, schema_editor):
    ContactEmail = apps.get_model("core", "ContactEmail")
    contact = ContactEmail.objects.first()
    if contact is None:
        return
    contact.github_display = ""
    contact.linkedin_display = ""
    contact.save(update_fields=["github_display", "linkedin_display"])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_contactemail_links'),
    ]

    operations = [
        migrations.RunPython(seed_contact_links, unseed_contact_links),
    ]
