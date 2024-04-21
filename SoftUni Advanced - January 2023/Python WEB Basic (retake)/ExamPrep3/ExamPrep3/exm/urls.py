from django.urls import path, include

from ExamPrep3.exm.views import *

urlpatterns = [
    path('', index, name='index'),
    path('car/catalogue/', catalogue, name='catalogue'),
    path('car/create/', car_create, name='car_create'),
    path('car/<int:id>/details/', car_id_details, name='car_details'),
    path('car/<int:id>/edit/', car_id_edit, name='car_edit'),
    path('car/<int:id>/delete/', car_id_delete, name='car_delete'),
    path('profile/create/', profile_create, name='profile_create'),
    path('profile/details/', profile_details, name='profile_details'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/delete/', profile_delete, name='profile_delete'),
]
