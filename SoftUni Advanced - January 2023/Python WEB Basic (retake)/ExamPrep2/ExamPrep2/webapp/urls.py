from django.urls import path

from ExamPrep2.webapp.views import *

urlpatterns = [
    path('', index, name='index'),

    path('album/add/', album_add, name='album add'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', album_edit, name='album edit'),
    path('album/delete/<int:pk>/', album_delete, name='album delete'),

    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),
]
