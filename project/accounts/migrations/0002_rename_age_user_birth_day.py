# Generated by Django 4.0.10 on 2023-02-28 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='age',
            new_name='birth_day',
        ),
    ]
