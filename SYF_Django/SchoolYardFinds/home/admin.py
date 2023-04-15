from django.contrib import admin
from .models import Category, Item

admin.site.register(Category)

class ListandoItem(admin.ModelAdmin):
    list_display =("id", "name", "Category", "check_sold")
    list_display_links =("id", "name")
    search_fields = ("name",)
    list_filter = ("Category",)
    list_editable = ("check_sold",)
    list_per_page = 10

admin.site.register(Item, ListandoItem)