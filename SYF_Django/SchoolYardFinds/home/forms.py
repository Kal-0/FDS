from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from django.forms import ModelForm
from .models import Item, Profile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password'
    }))

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



class CustomerForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']