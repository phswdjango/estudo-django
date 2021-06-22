from django.db import models
from ordered_model.models import OrderedModel
from django.shortcuts import reverse

# class Modulo(models.Model):
#     title = models.CharField(max_length=64)


class Modulo(OrderedModel):
    title = models.CharField(max_length=64)
    publico = models.TextField()
    descricao = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('modulos:detalhe', kwargs={'slug': self.slug})


class Aula(OrderedModel):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    modulo = models.ForeignKey('Modulo', on_delete=models.PROTECT)  # será adicionado or um seletor(no admin do django)
    # on_delete: o que fazer quando o modulo for apagado?: o modulo so podera ser excluido quando nao houver aulas nele
    order_with_respect_to = 'modulo'  # do OrderdModel: define como sera o ordenamento de Aula.
    vimeo_id = models.CharField(max_length=30)
    descricao = models.TextField(default="sem descrição")

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('modulos:aula', kwargs={'slug': self.slug})
