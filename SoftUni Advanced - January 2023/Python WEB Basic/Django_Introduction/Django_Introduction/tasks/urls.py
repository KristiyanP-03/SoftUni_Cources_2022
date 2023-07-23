#urls for tasks
from django.urls import path, include
from Django_Introduction.tasks.views import index, list_tasks, list_tasks_template

urlpatterns = [
    path('', index),
    path('list/', list_tasks),
    path('template/', list_tasks_template)
]
