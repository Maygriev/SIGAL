from django.urls import path
from apps.estoque.views import index, home, listMaterial, addMaterial

urlpatterns = [
        path('', index, name='index'),
        path('home', home, name='home'),
        path('list', listMaterial, name='list'),
        path('add-material', addMaterial, name='add-material'),
]