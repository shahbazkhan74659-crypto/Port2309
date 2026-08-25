from django.db import migrations


def migrate_quote_data(apps, schema_editor):
    HeroContent = apps.get_model("core", "HeroContent")
    Quote = apps.get_model("core", "Quote")
    quote_row = HeroContent.objects.filter(role="quote").order_by("pk").first()
    if quote_row is None:
        return
    Quote.objects.create(statement=quote_row.statement)
    HeroContent.objects.filter(role="quote").delete()


def unmigrate_quote_data(apps, schema_editor):
    HeroContent = apps.get_model("core", "HeroContent")
    Quote = apps.get_model("core", "Quote")
    quote = Quote.objects.order_by("-updated_at").first()
    if quote is not None:
        HeroContent.objects.create(role="quote", statement=quote.statement)
    Quote.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_quote'),
    ]

    operations = [
        migrations.RunPython(migrate_quote_data, unmigrate_quote_data),
    ]
