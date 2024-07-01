from django.urls import path
from apps.estoque.views import index, home, list_material, add_material

urlpatterns = [
        path('', index, name='index'),
        path('home', home, name='home'),
        path('list', list_material, name='list'),
        path('add-material', add_material, name='add-material'),
]