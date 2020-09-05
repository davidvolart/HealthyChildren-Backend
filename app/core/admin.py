from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'password', 'name', 'height', 'weight', 'age', 'is_superuser']


admin.site.register(models.User, UserAdmin)
