from django.test import Client
# server para emular requisições http, usando a view e path configurados
from modelodjango.django_assertions import assert_contains


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_title(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<title>Python Pro</title>')
