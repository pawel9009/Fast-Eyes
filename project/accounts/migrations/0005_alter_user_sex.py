# Generated by Django 4.0.10 on 2023-03-02 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_ailments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default=None, max_length=10),
        ),
    ]
