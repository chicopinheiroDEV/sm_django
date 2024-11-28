from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    concluido = models.BooleanField()
    data_criacao = models.DateTimeField(auto_now_add=True)
