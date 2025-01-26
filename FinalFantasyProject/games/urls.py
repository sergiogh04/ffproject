from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "games"

urlpatterns = [

    path("", views.index, name="index"),
    path("<int:game_id>/", views.game_details, name="game_details"),

    path("characters/", views.character_list, name="character_list"),

    path("characters/<int:character_id>", views.character_details, name="character_details"),

    path("genres/", views.genre_list, name="genre_list")

]