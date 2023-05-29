from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category        = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, blank= True, null= True)
    name            = models.CharField(max_length=50)
    price           = models.FloatField()
    description     = models.TextField(default="Escreva sua descrição", max_length= 150, blank= True)
    image           = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True , null=True)
    check_sold      = models.BooleanField(default=False)
    created_by      = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone= models.CharField(default = "0000-0000", max_length=200,null=True)
    profile_image = models.ImageField(upload_to="user/%Y/%m/%d/", blank=True , null=True)
    description = models.TextField(default="Escreva sua descrição", max_length= 150, blank= True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

class Carrinho(models.Model):
    user = models.ForeignKey(Profile, related_name='list_car', on_delete=models.CASCADE)
    itens_carrinho = models.ForeignKey(Item, related_name='list_car', on_delete=models.CASCADE)
    status = models.BooleanField(default="True")

    def __int__(self):
        return self.id
    
class Historico(models.Model):
    user_client = models.ForeignKey(Profile, related_name='hist_client', on_delete=models.CASCADE)
    user_vendodor = models.ForeignKey(Profile, related_name='hist_vendedor', on_delete=models.CASCADE)
    item_id =  models.ForeignKey(Item, related_name='his_item', on_delete=models.CASCADE)
    data_compra = models.DateTimeField(default=datetime.now)

    def __int__(self):
        return self.id

class Noticacao(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    compra_finalizada = models.IntegerField(default=0)
    compra_cancelada = models.IntegerField(default=0)

    def __int__(self):
        return self.id