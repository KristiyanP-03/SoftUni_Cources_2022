from django.urls import path, include
from apps.FoodieHaven_app.views import *

urlpatterns = [
    #Main Page
    path('', index, name="index"),

    #Public Page
    path('recipes/', recipes, name="recipes"),

    #Profile URLs
    path('profile/register/', RegisterView.as_view(), name='register'),
    path('profile/login/', LoginView.as_view(), name='login'),
    path('profile/logout/', LogoutView.as_view(), name='logout'),
    path('profile/details/', ProfileView.as_view(), name="profile details"),
    path('profile/edit/', EditProfileView.as_view(), name="profile edit"),
    path('profile/delete/', DeleteProfileView.as_view(), name="profile delete"),

    # PK recipes
    path('kitchen/', user_recepies, name="user recepies"),
    path('kitchen/write/', recepie_create, name="recepie create"),
    path('kitchen/<int:pk>/details/', recepie_details, name="recepie details"),
    path('kitchen/<int:pk>/edit/', recepie_edit, name="recepie edit"),
    path('kitchen/<int:pk>/delete/', recepie_delete, name="recepie delete"),
]