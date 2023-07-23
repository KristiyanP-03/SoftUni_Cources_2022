from django.urls import path

from apps.Fruitipedia.views import *

urlpatterns = [
    path('', index, name="index"),
    path('dashboard/', dashboard, name="dashboard"),
    path('create/', create, name="create fruit"),
    path('<int:pk>/details/', pk_details, name="fruit details"),
    path('<int:pk>/edit/', pk_edit, name="fruit edit"),
    path('<int:pk>/delete/', pk_delete, name="fruit delete"),
    path('profile/create/', profile_create, name="profile create"),
    path('profile/details/', profile_details, name="profile details"),
    path('profile/edit/', profile_edit, name="profile edit"),
    path('profile/delete/', profile_delete, name="profile delete")
]
