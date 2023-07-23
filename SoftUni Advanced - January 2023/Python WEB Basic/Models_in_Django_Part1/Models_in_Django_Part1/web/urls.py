from django.urls import path, include
from Models_in_Django_Part1.web.views import index

urlpatterns = [
    path('', index, name="index"),
]