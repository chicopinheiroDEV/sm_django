from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    descricao = models.TextField(blank=True, null=True)
    estoque = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)