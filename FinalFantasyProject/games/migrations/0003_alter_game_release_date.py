# Generated by Django 5.1.5 on 2025-01-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_rename_characters_character_rename_jobs_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(verbose_name='release date'),
        ),
    ]
