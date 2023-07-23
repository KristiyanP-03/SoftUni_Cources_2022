from django.urls import path, include

from apps.game.views import create_game, details_game, edit_game, delete_game

urlpatterns = [
    path("create/", create_game, name="create_game"),
    path("details/<int:pk>/", details_game, name="details_game"),
    path("edit/<int:pk>/", edit_game, name="edit_game"),
    path("delete/<int:pk>/", delete_game, name="delete_game")
]