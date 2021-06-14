from django.contrib.admin import ModelAdmin, register
from modelodjango.segunda_app.models import Video


@register(Video)  # serve para informar qual modelo está conectado a esse admin
class VideoAdmin(ModelAdmin):  # Herda de ModelAdmin pois será um admin conectado a um modelo
    list_display = ('title', 'slug', 'creation', 'vimeo_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug': ('title',)}
    # essa funcionalidade permite prepopular um campo('slug') com o valor de um ou mais campos ('title',)
