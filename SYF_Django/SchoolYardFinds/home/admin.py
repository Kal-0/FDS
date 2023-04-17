from django.contrib import admin
from .models import Category, Item

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