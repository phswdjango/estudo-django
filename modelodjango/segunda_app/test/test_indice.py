import pytest
from django.urls import reverse
from modelodjango.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('segunda_app:indice'))
    # reverse(calcular url reversa da app), args(parametros passados na url, com slug "motivacao")
    # O args tem que ser uma tupla. por isso foi finalizado com virgula.


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'title',
    ['Video 01 - segunda_app: ', 'Video 02 - segunda_app: ']
)
def test_titulo_video(resp, title):
    assert_contains(resp, title)


# def test_conteudo_video(resp):
#     assert_contains(resp, '<iframe src="https://player.vimeo.com/video/558095767')
