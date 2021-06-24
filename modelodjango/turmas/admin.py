from django.contrib import admin
from modelodjango.turmas.models import Turma


class MatriculaInline(admin.TabularInline):  # tbm tem o 'StackedInline'
    model = Turma.alunos.through
    extra = 1  # por default vao aparecer 3 campos(para adicionar 3 matriculas por vez, mas vc pode alterar)
    readonly_fields = ('data',)   # campos que vao aparecer mas nao poderam ser editados
    autocomplete_fields = ('usuario',)  # campo de buscar por nome
    ordering = ('-data',)  # ordenação decrescente por data.


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):  # a classe TurmaAdmin será responsavel por administrar o modelo Turma
    inlines = [MatriculaInline]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)  # ordenar de forma decrescente de acordo com o 'inicio'.
