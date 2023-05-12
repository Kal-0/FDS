from django.contrib import admin
from .models import Category, Item, Profile, Carrinho

class ListandoCategory(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links =("id", "name")

admin.site.register(Category, ListandoCategory)

class ListandoItem(admin.ModelAdmin):
    list_display =("id", "name", "category", "check_sold")
    list_display_links =("id", "name")
    search_fields = ("name",)
    list_filter = ("category",)
    list_editable = ("check_sold",)
    list_per_page = 10

admin.site.register(Item, ListandoItem)

class ListandoProfile(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links =("id", "user")
    search_fields = ("user",)

admin.site.register(Profile, ListandoProfile)

class ListandoCarrinho(admin.ModelAdmin):
    list_display = ("id", "user", "itens_carrinho", "status")
    list_display_links =("id", "user", "itens_carrinho")
    list_editable = ("status",)

admin.site.register(Carrinho, ListandoCarrinho)