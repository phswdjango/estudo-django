from django.db import models
from django.contrib.auth import get_user_model


class Turma(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    inicio = models.DateField()
    fim = models.DateField()
    alunos = models.ManyToManyField(get_user_model(), through='Matricula')
# 'throught' é a conexão com tabela intermediaria/auxiliar
# 'ManyToManyField' recebe o modelo no qual vc quer relacionar. No caso do usuario, vc pode chamar pela função
# 'get_user_model' que vem do django.contrib.auth (no caso, nos sobrescrevemos no models de base apartir de
# django.contrib.auth.base_user, e o usuario sera achado pois esta definido no settings.py

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    data = models.DateTimeField(auto_now_add=True)  # vai retornar a data exata da adição do registro.
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['usuario', 'turma']]
        ordering = ['turma', 'data']
