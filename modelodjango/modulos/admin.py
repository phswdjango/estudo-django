from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from modelodjango.modulos.models import Modulo


@admin.register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('title', 'publico', 'move_up_down_links')
