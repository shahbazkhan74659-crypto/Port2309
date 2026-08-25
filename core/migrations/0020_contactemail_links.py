from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_seed_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactemail',
            name='github_display',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactemail',
            name='linkedin_display',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
