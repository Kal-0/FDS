from django.db import models

# Create your models here.

class Produto(models.Model):
    nome        = models.CharField(max_length=50)
    preco       = models.DecimalField(decimal_places=2, max_digits=10000)
    descricao   = models.TextField(default="Ecreva sua descrição", max_length= 150, blank= False)

    