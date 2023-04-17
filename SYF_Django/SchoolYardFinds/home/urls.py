from django.urls import path
from home.views import home, feed, perfil, login_user, signup, create_item, buscar, page_categoria, produto_detalhes

urlpatterns = [
    path('home/', home, name='home'),#2
    path('feed/', feed, name='feed'),#3
    path('perfil/', perfil, name='perfil'),
    path('', login_user, name='login'),#1
    path('signup/', signup, name='signup'),#1.1
    path('publicacao/', create_item, name='create_item'),
    path('categoria/<int:foto_id>', page_categoria, name='categoria'),
    path('produto/<int:foto_id>', produto_detalhes, name='produto'),
]