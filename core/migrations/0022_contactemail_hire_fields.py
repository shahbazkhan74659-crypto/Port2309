from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_seed_contact_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactemail',
            name='available_for_label',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactemail',
            name='available_for',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactemail',
            name='stack_label',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactemail',
            name='stack',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
