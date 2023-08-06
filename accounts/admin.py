from django.contrib import admin

from . import models


@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'completed_profile']
    fields = ['first_name', 'last_name', 'email', 'completed_profile']


@admin.register(models.Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['picture', 'user', 'phone_number']
    fields = ['picture', 'user', 'phone_number']
