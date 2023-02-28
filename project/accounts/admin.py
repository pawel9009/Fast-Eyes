from django.contrib import admin

from django.contrib.auth.admin import UserAdmin


from .models import User


fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields':('first_name', 'last_name', 'email', 'age','sex')})

UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)
