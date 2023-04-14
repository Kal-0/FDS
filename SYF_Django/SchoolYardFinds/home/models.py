from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class CreateUserForm(UserCreationForm):
    class Meta:
        mode= User
        fields = ['usarname', 'usersurname', 'email', 'password1', 'password2']
