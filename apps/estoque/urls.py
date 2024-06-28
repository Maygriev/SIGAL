from django.urls import path
from apps.estoque.views import index

urlpatterns = [
        path('', index, name='index')
]