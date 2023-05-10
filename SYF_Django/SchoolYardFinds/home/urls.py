from django.urls import path
from home.views import home, feed, perfil, login_user, signup, create_item, page_categoria, produto_detalhes, carrinho, edit_profile, add_to_cart
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
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
]

