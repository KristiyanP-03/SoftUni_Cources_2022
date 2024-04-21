from django.urls import path, include

from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('recipe/catalogue/', catalogue, name='catalogue'),

    path('recipe/create/', recipe_create, name='create_recipe'),
    path('recipe/<int:pk>/details/', recipe_details, name='details_recipe'),
    path('recipe/<int:pk>/edit/', recipe_edit, name='edit_recipe'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='delete_recipe'),

    path('profile/create/', profile_create, name='create_profile'),
    path('profile/details/', profile_details, name='details_profile'),
    path('profile/edit/', profile_edit, name='edit_profile'),
    path('profile/delete/', profile_delete, name='delete_profile'),
]
