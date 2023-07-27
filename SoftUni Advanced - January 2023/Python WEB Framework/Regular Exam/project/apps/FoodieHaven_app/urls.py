from django.urls import path, include

from apps.FoodieHaven_app.views import index

urlpatterns = [
    path('', index, name="index"),
]