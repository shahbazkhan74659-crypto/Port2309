from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_migrate_quote_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herocontent',
            name='role',
        ),
        migrations.RemoveField(
            model_name='herocontent',
            name='statement',
        ),
    ]
