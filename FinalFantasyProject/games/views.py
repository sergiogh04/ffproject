from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse

from games.models import Game, Character, Genre, Job



@login_required
def index(request):

    game = Game.objects.all()
    context = {'games' : game }
    return render(request, 'games/index.html', context)


@login_required

def game_details(request, game_id):

    game = Game.objects.get(pk=game_id)
    context = {'game' : game }
    return render(request, 'games/game_details.html', context)

@login_required

def character_details(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    context = {'character': character}
    return render(request, 'games/character_details.html', context)

@login_required

def character_list(request):

    characters = Character.objects.all()
    context = {'characters' : characters}
    return render(request, 'games/character_list.html', context)

@login_required

def genre_list(request):
    genres = Genre.objects.all()
    context = {'genres' : genres}
    return render(request,'games/genre_list.html',context)

@login_required

def job_list(request):
    jobs = Job.objects.all()
    context = {'jobs' : jobs}
    return render(request, 'games/job_list.html',context)






