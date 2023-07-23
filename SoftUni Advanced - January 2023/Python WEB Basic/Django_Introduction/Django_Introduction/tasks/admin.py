from django.contrib import admin

from Django_Introduction.tasks.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_title', 'task_text')

admin.site.register(Task, TaskAdmin)