from django.shortcuts import render, redirect

from django.contrib import messages

from apps.estoque.models import Material
from apps.estoque.forms import MaterialForms

def index(request):
        if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')
        
        return render(request, "estoque/index.html")

def home(request):
        if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')
        
        return render(request, "estoque/index.html")

def list_material(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    materiais = Material.objects.order_by("-id")
    return render(request, 'estoque/listar.html', {"cards": materiais})

def add_material(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    form = MaterialForms
    if request.method == 'POST':
        form = MaterialForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo Material Cadastrado!')
            return redirect('index')
    
    return render (request, 'estoque/novo_material.html', {'form': form})