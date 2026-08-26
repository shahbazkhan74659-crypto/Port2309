from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_seed_contact_hire_fields'),
        ('projects', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='languages_m2m',
            field=models.ManyToManyField(blank=True, related_name='about_languages', to='projects.tag'),
        ),
        migrations.AddField(
            model_name='about',
            name='frameworks_m2m',
            field=models.ManyToManyField(blank=True, related_name='about_frameworks', to='projects.tag'),
        ),
        migrations.AddField(
            model_name='about',
            name='learning_m2m',
            field=models.ManyToManyField(blank=True, related_name='about_learning', to='projects.tag'),
        ),
    ]
