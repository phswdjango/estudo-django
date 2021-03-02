from django.test import Client
# server para emular requisições http, usando a view e path configurados


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
