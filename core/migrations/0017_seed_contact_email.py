from django.db import migrations

CONTACT_EMAIL = "shahbazkhan74659@gmail.com"


def seed_contact_email(apps, schema_editor):
    ContactEmail = apps.get_model("core", "ContactEmail")
    if not ContactEmail.objects.exists():
        ContactEmail.objects.create(email=CONTACT_EMAIL)


def unseed_contact_email(apps, schema_editor):
    ContactEmail = apps.get_model("core", "ContactEmail")
    ContactEmail.objects.filter(email=CONTACT_EMAIL).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_contactemail'),
    ]

    operations = [
        migrations.RunPython(seed_contact_email, unseed_contact_email),
    ]
