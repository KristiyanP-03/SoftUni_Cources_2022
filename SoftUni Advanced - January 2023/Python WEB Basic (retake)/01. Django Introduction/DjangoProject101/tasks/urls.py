from django.urls import path

from tasks.views import *

urlpatterns = [
    path('index/', index),
    path('tasks/', task_tab),
    path('working-template/', working_template)
]
