from django.contrib import admin

from .models import Image, Experiment

admin.site.register(Image)
admin.site.register(Experiment)