from django.urls import path
from home.views import home, feed, perfil, test, login_user, signup, buscar

urlpatterns = [
    path('home/', home, name='home'),#2
    path('test/', test, name='test'),
    path('feed/', feed, name='feed'),#3
    path('perfil/', perfil, name='perfil'),
    path('', login_user, name='login'),#1
    path('signup/', signup, name='signup'),#1.1
    path('buscar', buscar, name='buscar')
]