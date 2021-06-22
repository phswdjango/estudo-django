from django.urls import reverse
import pytest as pytest
# server para emular requisições http, usando a view e path configurados.
from modelodjango.django_assertions import assert_contains
from model_bakery import baker
from modelodjango.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home'))
    return resp


def test_titulos_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.title)


def test_link_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.get_absolute_url())
