from typing import List
from modelodjango.modulos.models import Modulo, Aula
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por títulos
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> List[Modulo]:
    return get_object_or_404(Modulo, slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo_especifico: Modulo):
    return list(modulo_especifico.aula_set.order_by('order').all())  # aula_set é um manager que pode listar as aulas


def mostrar_aula(slug):
    # return get_object_or_404(Aula, slug=slug)  # nao retorna erro na aplicação(travando tudo)
    # return Aula.objects.get(slug=slug) # essa query e a anterior, geram erro de N+1 na renderização do template.
    return Aula.objects.select_related('modulo').get(slug=slug)

# --/Antes do Prefetch
# def trazer_modulos_com_aulas():
#     return Modulo.objects.order_by('order').prefetch_related('aula_set').all()


def trazer_modulos_com_aulas():  # prefetch_related serve pra evitar o N+1 em busca do lado 'N' pro lado '1'
    aulas_ordenadas = Aula.objects.order_by('order')
    return Modulo.objects.order_by('order').prefetch_related(
        Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')).all()
    # queryset= Atributo utilizado em 'Modulo' que vai conter esse resultado
