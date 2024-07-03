from django.shortcuts import render, redirect

from django.contrib import messages
from django.core.paginator import Paginator

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

def listMaterial(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    materiais = Material.objects.order_by("-id")
    materiais = Paginator(materiais, 20)
    page_number = request.GET.get("page")
    page_obj = materiais.get_page(page_number)
    return render(request, 'estoque/listar.html', {"cards": page_obj})

def addMaterial(request):
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
    
    return render (request, 'estoque/novoMaterial.html', {'form': form})

def editMaterial(request, materialID):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    material = Material.objects.get(id=materialID)
    form = MaterialForms(instance=material)

    if request.method == 'POST':
        form = MaterialForms(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material Editado com Sucesso!')
            return redirect('index')
        
    return render(request, 'estoque/editMaterial.html', {'form':form, 'materialID':materialID})

def buscaMaterial(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    materiais = Material.objects.order_by("-id")

    if request.GET['q']:
        itemBusca = request.GET['q']
        if itemBusca:
             materiais = materiais.filter(desc__icontains=itemBusca)

    materiais = Paginator(materiais, 20)
    page_number = request.GET.get("page")
    page_obj = materiais.get_page(page_number)
    return render(request, 'estoque/listar.html', {"cards": page_obj})

def detailMaterial(request, materialID):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    material = Material.objects.get(id=materialID)
    form = MaterialForms(instance=material)
        
    return render(request, 'estoque/detailMaterial.html', {'form':form, 'materialID':materialID})