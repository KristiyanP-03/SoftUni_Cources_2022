from django.urls import path, include

from exam_app.views import *

urlpatterns = [

    path('', home_page, name="home page"),
    path('dashboard/', dashboard, name="dashboard"),



    path('create/', event_create, name="event create" ),
    path('details/<int:pk>/', event_details, name="event details"),
    path('edit/<int:pk>/', event_edit, name="event edit"),
    path('delete/<int:pk>/', event_delete, name="event delete"),



    path('profile/create/', profile_create, name="profile create"),
    path('profile/details/', profile_details, name="profile details"),
    path('profile/edit/', profile_edit, name="profile edit"),
    path('profile/delete/', profile_delete, name="profile delete"),

]