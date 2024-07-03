from django.urls import path

from apps.usuario.views import login, cadastro, logout_view

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout_view, name='logout'),
]