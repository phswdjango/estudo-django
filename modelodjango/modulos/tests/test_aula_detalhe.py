from django.urls import reverse
import pytest as pytest
from modelodjango.django_assertions import assert_contains
from model_bakery import baker
from modelodjango.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)  # isso diz o atributo 'modulo' da Aula esta conectado com o objeto modulo


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', args=(aula.slug,)))
    return resp


def test_aula(resp):
    assert resp.status_code == 200


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.title)


def test_descricao_aula(resp, aula: Aula):
    assert_contains(resp, aula.descricao)


def test_video_aula(resp, aula: Aula):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{aula.vimeo_id}')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f' <li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.title}</a></li>')
