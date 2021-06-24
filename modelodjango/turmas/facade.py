from modelodjango.turmas.models import Turma


def buscar_turmas():
    return Turma.objects.all()
