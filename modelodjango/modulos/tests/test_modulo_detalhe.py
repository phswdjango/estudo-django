from django.urls import reverse
import pytest as pytest
from modelodjango.django_assertions import assert_contains
from model_bakery import baker
from modelodjango.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aulas(modulo):
    return baker.make(Aula, 3, modulo=modulo)  # isso diz o atributo 'modulo' da Aula esta conectado com o objeto modulo


@pytest.fixture
def resp(client, modulo, aulas):
    resp = client.get(reverse('modulos:detalhe', args=(modulo.slug,)))
    return resp


def test_detalhes(resp):
    assert resp.status_code == 200


def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.title)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)


def test_aulas_titulos(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.title)


def test_link_aulas(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
