from django.urls import path
from Django_Templates.django_template_app import views

urlpatterns = [
    path('index/', views.index)
]
