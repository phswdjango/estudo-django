from django.shortcuts import render
from modelodjango.modulos import facede
from django.contrib.auth.decorators import login_required


def detalhe(request, slug):
    modulo_especifico = facede.encontrar_modulo(slug)
    aulas = facede.listar_aulas_de_modulo_ordenadas(modulo_especifico)
    return render(request, 'modulos/modulo_detalhe.html',
                  context={'contexto_detalhe': modulo_especifico, 'aulas': aulas})


@login_required
def aula(request, slug):
    aula = facede.mostrar_aula(slug)
    return render(request, 'modulos/modulo_aula.html',
                  context={'aula': aula})


def indice(request):
    modulos = facede.trazer_modulos_com_aulas()
    return render(request, 'modulos/modulo_indice.html', context={"modulos": modulos})
