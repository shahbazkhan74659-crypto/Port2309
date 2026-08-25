from django.db import migrations


def split_quote_row(apps, schema_editor):
    HeroContent = apps.get_model("core", "HeroContent")
    primary = HeroContent.objects.filter(role="primary").order_by("pk").first()
    if primary is None:
        return
    if HeroContent.objects.filter(role="quote").exists():
        return
    HeroContent.objects.create(role="quote", statement=primary.statement)


def unsplit_quote_row(apps, schema_editor):
    HeroContent = apps.get_model("core", "HeroContent")
    HeroContent.objects.filter(role="quote").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_herocontent_role'),
    ]

    operations = [
        migrations.RunPython(split_quote_row, unsplit_quote_row),
    ]
