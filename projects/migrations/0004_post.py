from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('short_description', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('published_at', models.DateField()),
                ('tags', models.ManyToManyField(related_name='posts', to='projects.tag')),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
    ]
