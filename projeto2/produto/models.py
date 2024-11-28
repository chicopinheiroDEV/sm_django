from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    estoque = models.PositiveBigIntegerField()
    data_criacao = models.DateTimeField(auto_now_add= True)