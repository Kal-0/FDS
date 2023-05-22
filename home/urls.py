from django.urls import path
from home.views import home, feed, perfil, login_user, signup, create_item, page_categoria, produto_detalhes, carrinho, edit_profile, add_to_cart, remove_cart, finalizar_cart, painel_de_vendas, config, busca
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', home, name='home'),#2
    path('feed/', feed, name='feed'),#3
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', edit_profile, name='edit'),
    path('', login_user, name='login'),#1
    path('signup/', signup, name='signup'),#1.1
    path('publicacao/', create_item, name='create_item'),
    path('categoria/<int:foto_id>', page_categoria, name='categoria'),
    path('produto/<int:foto_id>', produto_detalhes, name='produto'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('carrinho/', carrinho, name='carrinho'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('remove_cart/<int:car_id>/', remove_cart, name='remove_cart'),
    path('finalizar_cart/<int:car_id>/', finalizar_cart, name='finalizar_cart'),
    path('painel_de_vendas/', painel_de_vendas, name='painel_de_vendas'),
    path('configurações/', config, name='config'),
    path('busca/', busca, name='busca'),
]