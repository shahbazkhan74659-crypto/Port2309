from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_migrate_about_skills_data'),
    ]

    operations = [
        migrations.RemoveField(model_name='about', name='languages'),
        migrations.RemoveField(model_name='about', name='frameworks'),
        migrations.RemoveField(model_name='about', name='learning'),
        migrations.RenameField(model_name='about', old_name='languages_m2m', new_name='languages'),
        migrations.RenameField(model_name='about', old_name='frameworks_m2m', new_name='frameworks'),
        migrations.RenameField(model_name='about', old_name='learning_m2m', new_name='learning'),
        migrations.AlterField(
            model_name='about',
            name='languages',
            field=models.ManyToManyField(related_name='about_languages', to='projects.tag'),
        ),
        migrations.AlterField(
            model_name='about',
            name='frameworks',
            field=models.ManyToManyField(related_name='about_frameworks', to='projects.tag'),
        ),
        migrations.AlterField(
            model_name='about',
            name='learning',
            field=models.ManyToManyField(related_name='about_learning', to='projects.tag'),
        ),
    ]
