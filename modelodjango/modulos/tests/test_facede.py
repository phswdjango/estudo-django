from modelodjango.modulos import facede
import pytest
from model_bakery import baker
from modelodjango.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


def test_listar_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.order)) == facede.listar_modulos_ordenados()
