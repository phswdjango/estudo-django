from modelodjango.modulos import facede


# esse processador de contexto vai ser renderizado para todas as minhas renderizações de contexto, e eu nao vou precisar
# toda view, renderizar isso manualmente.
def listar_modulos(request):
    return {'MODULOS': facede.listar_modulos_ordenados()}
