from django.contrib import admin

from .models import Experiment, Image

admin.site.register(Image)
admin.site.register(Experiment)
