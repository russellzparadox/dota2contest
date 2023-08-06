from django.contrib import admin

from . import models


@admin.register(models.Teams)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'creator', 'competition']


@admin.register(models.Competitions)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_date', 'end_date', 'description']
