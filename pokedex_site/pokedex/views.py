from django.shortcuts import render

from .models import Pokemon


def index(request):
    result_set = Pokemon.objects.all()
    return render(request, 'pokedex/index.html', context={
        'pokemons': Pokemon.to_dict(result_set),
        'msg': 'The Pokedex'
    })


def about(request):
    return render(request, 'pokedex/about.html')
