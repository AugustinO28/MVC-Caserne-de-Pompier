# Generated by Django 2.2.28 on 2024-11-15 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caserne', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipement',
            old_name='photo',
            new_name='lieu_photo',
        ),
        migrations.RemoveField(
            model_name='character',
            name='team',
        ),
        migrations.RemoveField(
            model_name='character',
            name='type',
        ),
    ]