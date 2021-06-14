import pytest
from django.urls import reverse
from modelodjango.django_assertions import assert_contains
from modelodjango.segunda_app.models import Video
from model_bakery import baker


# -----------/Antes do baker
# @pytest.fixture
# def video(db):
#     # a fixture db, serve para emular a conexao com banco. Ela cria um banco de teste apartir das migrations.
#     v = Video(slug='video1', title='Video 01 - segunda_app: ', vimeo_id='558095767')
#     v.save()
#     return v

# -----------/Depois do baker
@pytest.fixture
def video(db):
    return baker.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('segunda_app:video', args=(video.slug,)))
    # reverse(calcular url reversa da app), args(parametros passados na url, com slug "video1")
    # O args tem que ser uma tupla. por isso foi finalizado com virgula.


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('segunda_app:video', args=(video.slug + 'slug_incorreto',)))


def test_resp_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, video):
    assert_contains(resp, video.title)


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}')
