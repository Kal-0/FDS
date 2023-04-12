from django.urls import path
from home.views import home, feed, perfil

urlpatterns = [
    path('', home, name='home'),
    path('feed/', feed, name='feed'),
    path('perfil/', perfil, name='perfil'),
]