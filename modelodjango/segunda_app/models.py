from django.db import models
from django.urls import reverse


class Video(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    vimeo_id = models.CharField(max_length=30)
    creation = models.DateTimeField(auto_now_add=True)  # atribui ao atributo, a data atual.

    def get_absolute_url(self):   # existe uma conveção no django de criar esse metodo para retorar a url
        return reverse('segunda_app:video', args=(self.slug,))

    def __str__(self):
        return f'Video: {self.title}'
