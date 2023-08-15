from django.urls import path

from apps.CarCollection_App.views import *

urlpatterns = [
    path('', index, name="index"),
    path('catalogue/', catalogue, name="catalogue"),

    path('profile/create/', profile_create, name="profile create" ),
    path('profile/details/', profile_details, name="profile details" ),
    path('profile/edit/', profile_edit, name="profile edit"),
    path('profile/delete/', profile_delete, name="profile delete"),

    path('car/create/', car_create, name="car create"),
    path('car/<int:pk>/details/', car_details, name="car details"),
    path('car/<int:pk>/edit/', car_edit, name="car edit"),
    path('car/<int:pk>/delete/', car_delete, name="car delete"),
]