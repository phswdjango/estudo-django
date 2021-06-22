from typing import List

from django.urls import reverse
import pytest as pytest
from modelodjango.django_assertions import assert_contains
from model_bakery import baker
from modelodjango.modulos.models import Modulo, Aula


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def aulas(modulos):
    aulas = []
    for modulo in modulos:
        aulas.extend(baker.make(Aula, 3, modulo=modulo))
        # isso diz o atributo 'modulo' da Aula esta conectado com o objeto modulo
    return aulas


@pytest.fixture
def resp(client, modulos: List[Modulo], aulas: List[Modulo]):
    resp = client.get(reverse('modulos:indice'))
    return resp


def test_indice(resp):
    assert resp.status_code == 200


def test_titulo_modulos(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.title)


def test_publico_modulos(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)


def test_descricao_modulos(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)


def test_titulo_aulas(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.title)


def test_link_aulas(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
