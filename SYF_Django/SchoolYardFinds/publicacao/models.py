from django.db import models

from datetime import datetime

# Create your models here.

class Produto(models.Model):

    OPCOES_CATEGORIA = [
        ("PROMOÇÃO", "Promoção"),
        ("PARA VOCÊ", "Para você"),
    ]

    nome            = models.CharField(max_length=50)
    preco           = models.DecimalField(decimal_places=2, max_digits=10000)
    # botoar uma referencia para o id do usuario mas n sei como
    descricao       = models.TextField(default="Ecreva sua descrição", max_length= 150, blank= True)
    categoria       = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='') #categoria do produto
    produto_imagem  = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True , null=True) #podemos botar uma data para evitar erros de uma foto com mesmo nome
    estoque         = models.BooleanField(default=True) #se ainda tem no estoque

    def __str__(self):
        return f"Produto [nome={self.nome}]"
