from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"home.html")

def feed(request):
    return render(request,"Feed_de_Produtos.html")
