from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_migrate_project_tags_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tags',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='tags_m2m',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(related_name='projects', to='projects.tag'),
        ),
    ]
