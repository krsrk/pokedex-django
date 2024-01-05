from django.shortcuts import render

from .models import Pokemon


def index(request):
    result_set = Pokemon.objects.all()
    return render(request, 'pokedex/index.html', context={'pokemons': result_set})


def about(request):
    return render(request, 'pokedex/about.html')
