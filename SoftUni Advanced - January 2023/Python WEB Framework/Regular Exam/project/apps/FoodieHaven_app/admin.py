from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin

from apps.FoodieHaven_app.models import ProfileModel


class ProfileModelAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name']

    list_display = ['username', 'email', 'first_name', 'last_name', 'profile_picture']

    ordering = ['username']

    search_fields = ['username', 'email']

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Account Information', {
            'fields': ('username', 'password', 'profile_picture')
        }),
    )

    readonly_fields = ['username', 'email']

# Register your models here.
admin.site.register(ProfileModel, ProfileModelAdmin)
