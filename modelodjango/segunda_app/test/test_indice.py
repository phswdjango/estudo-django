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


@pytest.mark.parametrize(
    'slug',
    ['video1', 'video2']
)
def test_slug_link_video(resp, slug):
    video_link = reverse('segunda_app:video', args=(slug,))  # retorna /segunda_app/video1
    assert_contains(resp, f'href="{video_link}"')
