from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_seed_placeholder_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
