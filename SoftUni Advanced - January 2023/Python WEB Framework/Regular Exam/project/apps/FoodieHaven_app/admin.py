from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin, UserAdmin

from apps.FoodieHaven_app.models import *


class ProfileModelAdmin(UserAdmin):  # Inherit from UserAdmin
    list_filter = ['first_name', 'last_name']
    list_display = ['username', 'email', 'first_name', 'last_name', 'profile_picture']
    ordering = ['username']
    search_fields = ['username', 'email']

    # Include permissions fields in fieldsets
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Account Information', {
            'fields': ('username', 'password', 'profile_picture')
        }),
        ('Permissions', {  # Include this section for permissions
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    readonly_fields = ['username', 'email']

# Register your models here.
admin.site.register(ProfileModel, ProfileModelAdmin)
admin.site.register(RecipeModel)
admin.site.register(ReportUserModel)
admin.site.register(AnnouncementModel)