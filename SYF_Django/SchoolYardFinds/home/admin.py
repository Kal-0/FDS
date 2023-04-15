from django.contrib import admin
from publicacao.models import Produto
from django.contrib import admin
from .models import Category, Item


admin.site.register(Category)
admin.site.register(Item)

class ListandoProduto(admin.ModelAdmin):
    list_display =("id", "nome", "categoria", "estoque")
    list_display_links =("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("estoque",)
    list_per_page = 10

admin.site.register(Produto, ListandoProduto)