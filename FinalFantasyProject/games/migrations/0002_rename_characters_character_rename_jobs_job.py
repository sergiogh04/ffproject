# Generated by Django 5.1.5 on 2025-01-25 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Characters',
            new_name='Character',
        ),
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
    ]
