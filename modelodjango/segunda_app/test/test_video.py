import pytest
from django.urls import reverse
from modelodjango.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('segunda_app:video', args=('video1',)))
    # reverse(calcular url reversa da app), args(parametros passados na url, com slug "motivacao")
    # O args tem que ser uma tupla. por isso foi finalizado com virgula.


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1 class="mt-4 mb-3">Video 01 - segunda_app: </h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/558095767')
