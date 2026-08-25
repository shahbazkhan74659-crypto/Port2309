from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_split_quote_row'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(default='Good ideas deserve more than thought—they deserve to be built.', max_length=300)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]
