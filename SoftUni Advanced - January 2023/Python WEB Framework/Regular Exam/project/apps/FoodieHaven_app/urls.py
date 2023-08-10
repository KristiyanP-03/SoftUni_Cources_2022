from django.urls import path, include
from apps.FoodieHaven_app.views import *

urlpatterns = [
    #Main/Public Page
    path('', index, name="index"),

    #Profile URLs
    path('profile/register/', RegisterView.as_view(), name='register'),
    path('profile/login/', LoginView.as_view(), name='login'),
    path('profile/logout/', LogoutView.as_view(), name='logout'),
    path('profile/details/', ProfileView.as_view(), name="profile details"),
    path('profile/edit/', EditProfileView.as_view(), name="profile edit"),
    path('profile/delete/', DeleteProfileView.as_view(), name="profile delete"),

    # PK recipes
    path('kitchen/', user_recipes, name="user recipes"),
    path('kitchen/write/', recipe_create, name="recipe create"),
    path('kitchen/<int:pk>/details/', recipe_details, name="recipe details"),
    path('kitchen/<int:pk>/edit/', recipe_edit, name="recipe edit"),
    path('kitchen/<int:pk>/delete/', recipe_delete, name="recipe delete"),


    path('kitchen/<int:pk>/report/', report_user, name='report_user'),
    path('reporsts/', reports, name="reports")
]