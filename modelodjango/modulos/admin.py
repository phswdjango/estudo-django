from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from modelodjango.modulos.models import Modulo, Aula


@admin.register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('title', 'publico', 'move_up_down_links')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Aula)
class AulaAdmin(OrderedModelAdmin):
    list_display = ('title', 'modulo', 'order', 'move_up_down_links')
    list_filter = ('modulo',)  # adiciona um filtro o admin
    ordering = ('modulo', 'order')
# ordena primeiro por modulo, dps por order(que é um indice que determina uma ordem arbitraria, q vem do OrderedModels)
    prepopulated_fields = {'slug': ('title',)}
