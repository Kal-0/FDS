from django.urls import path
from home.views import home, feed, perfil, test, login_user, signup

urlpatterns = [
    path('', home, name='home'),
    path('test/', test, name='test'),
    path('feed/', feed, name='feed'),
    path('perfil/', perfil, name='perfil'),
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
]