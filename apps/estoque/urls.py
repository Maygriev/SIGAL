from django.urls import path
from apps.estoque.views import index, home, listMaterial, addMaterial, editMaterial, buscaMaterial, detailMaterial

urlpatterns = [
        path('', index, name='index'),
        path('home', home, name='home'),
        path('list', listMaterial, name='list'),
        path('add-material', addMaterial, name='add-material'),
        path("view-material/<int:materialID>", detailMaterial, name="view-material"),
        path("edit-material/<int:materialID>", editMaterial, name="edit-material"),
        path("busca-material", buscaMaterial, name="busca-material"),
]