from django.urls import path
from publicacao.views import publicacao_view

urlpatterns = [
    path('', publicacao_view, name='publicacao'),
]