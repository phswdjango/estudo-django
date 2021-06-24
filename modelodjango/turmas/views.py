from django.shortcuts import render
from . import facade


def indice(request):
    turmas = facade.buscar_turmas()
    return render(request, 'turmas/turmas_indice.html', context={'turmas': turmas})
