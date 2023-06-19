from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

fields = list(UserAdmin.fieldsets)

UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)
