# Generated by Django 4.0.10 on 2023-04-02 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('img', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=100)),
                ('correct', models.IntegerField(default=0, null=True)),
                ('incorrect', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pass_rate', models.FloatField(default=0, null=True)),
                ('samples', models.CharField(default=None, max_length=256)),
                ('duration', models.IntegerField(default=500, null=True)),
                ('challenge', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
