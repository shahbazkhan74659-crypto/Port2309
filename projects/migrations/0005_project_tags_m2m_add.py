from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags_m2m',
            field=models.ManyToManyField(blank=True, related_name='projects', to='projects.tag'),
        ),
    ]
