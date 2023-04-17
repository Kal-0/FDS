from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category        = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, blank= True)
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
    description = models.TextField(default="Escreva sua descrição", max_length= 150, blank= True)
    profile_image = models.ImageField(upload_to="user/%Y/%m/%d/", blank=True , null=True)

    def __int__(self):
        return self.id
