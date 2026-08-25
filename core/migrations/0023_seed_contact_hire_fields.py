from django.db import migrations

AVAILABLE_FOR_LABEL = "Available for"
AVAILABLE_FOR = "Freelance / contract"
STACK_LABEL = "Stack"
STACK = "Django · React · Tailwind"


def seed_hire_fields(apps, schema_editor):
    ContactEmail = apps.get_model("core", "ContactEmail")
    contact = ContactEmail.objects.first()
    if contact is None:
        return
    contact.available_for_label = AVAILABLE_FOR_LABEL
    contact.available_for = AVAILABLE_FOR
    contact.stack_label = STACK_LABEL
    contact.stack = STACK
    contact.save(update_fields=["available_for_label", "available_for", "stack_label", "stack"])


def unseed_hire_fields(apps, schema_editor):
    ContactEmail = apps.get_model("core", "ContactEmail")
    contact = ContactEmail.objects.first()
    if contact is None:
        return
    contact.available_for_label = ""
    contact.available_for = ""
    contact.stack_label = ""
    contact.stack = ""
    contact.save(update_fields=["available_for_label", "available_for", "stack_label", "stack"])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_contactemail_hire_fields'),
    ]

    operations = [
        migrations.RunPython(seed_hire_fields, unseed_hire_fields),
    ]
