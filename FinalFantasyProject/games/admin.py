from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Game, Genre, Character, Job

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Character)
admin.site.register(Job)


