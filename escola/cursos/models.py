from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(default="Descrição do curso.")
    carga_horaria = models.IntegerField()
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome