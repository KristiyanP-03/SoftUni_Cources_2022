from django.contrib import admin

from tasks.models import Task


# Register your models here.
@admin.register(Task)              #admin.site.register(Task)   Basic way to register your model
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')        #Admin site display task
