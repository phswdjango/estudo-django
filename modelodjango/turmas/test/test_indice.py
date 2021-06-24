import pytest
from django.urls import reverse
from modelodjango.django_assertions import assert_contains
from model_bakery import baker
from modelodjango.turmas.models import Turma


@pytest.fixture
def turmas(db):
    return baker.make(Turma, 2)


@pytest.fixture
def resp(client, turmas):
    resp = client.get(reverse('turmas:indice'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_turmas_nome(resp, turmas):
    for turma in turmas:
        assert_contains(resp, turma.nome)


# def test_turmas_inicio(resp, turmas):
#     for turma in turmas:
#         assert_contains(resp, turma.inicio)
#
#
# def test_turmas_fim(resp, turmas):
#     for turma in turmas:
#         assert_contains(resp, turma.fim)
