import pytest
from django.urls import reverse
from modelodjango.django_assertions import assert_contains
from model_bakery import baker
from modelodjango.segunda_app.models import Video


@pytest.fixture
def videos(db):
    return baker.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('segunda_app:indice'))
    # reverse(calcular url reversa da app), args(parametros passados na url, com slug "motivacao")
    # O args tem que ser uma tupla. por isso foi finalizado com virgula.


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.title)


def test_slug_link_video(resp, videos):
    for video in videos:
        video_link = reverse('segunda_app:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
