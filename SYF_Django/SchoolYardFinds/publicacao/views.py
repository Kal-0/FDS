from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def publicacao_view(request):
    return render(request, "publicacao.html")
