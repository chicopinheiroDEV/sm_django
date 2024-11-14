from django.db import models

# Create your models here.
class Tarefas(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)
    concluido = models.BooleanField(default=False)