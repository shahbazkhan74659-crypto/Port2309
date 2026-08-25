from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_herocontent_role_statement'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSnapshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eyebrow', models.CharField(default='A LITTLE ABOUT ME', max_length=100)),
                ('headline_one', models.CharField(default='CURIOSITY.', max_length=60)),
                ('headline_two', models.CharField(default='CREATION.', max_length=60)),
                ('headline_three', models.CharField(default='EXPERIMENTATION.', max_length=60)),
                ('headline_sub', models.CharField(default='Curiosity starts the question. Creation takes it somewhere new. Experimentation turns it into something real.', max_length=300)),
                ('paragraph', models.TextField(default="I'm a developer, writer, and explorer—drawn to the space where technology, ideas, and imagination meet. I build things to understand how they work, write to make sense of what I discover, and explore simply because there's always something new worth finding. My work is less about following a fixed path and more about turning curiosity into things that didn't exist before.")),
                ('currently_label', models.CharField(default='Currently', max_length=40)),
                ('currently_building', models.CharField(default='An autonomous personal AI assistant', max_length=150)),
                ('currently_learning', models.CharField(default='AI and autonomous systems', max_length=150)),
                ('currently_writing', models.CharField(default='A fantasy story, "The God Valley"', max_length=150)),
                ('currently_exploring', models.CharField(default='Agentic AI tooling and autonomous workflows', max_length=150)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]
