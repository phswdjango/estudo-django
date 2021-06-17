from django.db import models
from ordered_model.models import OrderedModel

# class Modulo(models.Model):
#     title = models.CharField(max_length=64)


class Modulo(OrderedModel):
    title = models.CharField(max_length=64)
    publico = models.TextField()
    descricao = models.TextField()

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title
