from django.contrib import admin

from apps.estoque.models import Material

class ListandoMaterial(admin.ModelAdmin):
    list_display = ("id", "desc", "categoria", "qtd", "tipo")
    list_display_links = ("id","desc")
    search_fields = ("desc",)
    list_filter = ("categoria",)
    list_per_page = 10

admin.site.register(Material, ListandoMaterial)