from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from apps.carrinho.models import Carrinho
from apps.estoque.models import Material

def addCarrinho(request, itemID):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    material = Material.objects.get(id=itemID)
    
    itemCarrinho = Carrinho.objects.filter(user=request.user, item=material).first()

    if itemCarrinho:
        itemCarrinho.qtd += 1
        itemCarrinho.save()
        messages.success(request, material.desc + " adicionado ao Carrinho")
    else:
        Carrinho.objects.create(user=request.user, item=material, itemDesc=material.desc)
        messages.success(request, material.desc + " adicionado ao Carrinho")

    return redirect("detail-carrinho")

def remCarrinho(request, carrinhoItemID):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    material = Material.objects.get(id=carrinhoItemID)
    itemCarrinho = get_object_or_404(Carrinho, user=request.user, item=material)

    if itemCarrinho:
        itemCarrinho.delete()
        messages.success(request, material.desc + " removido do seu Carrinho.")

    return redirect("detail-carrinho")

def detailCarrinho(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    itemCarrinho = Carrinho.objects.filter(user=request.user)
    totalItems = sum(item.qtd for item in itemCarrinho)

    contexto = {
        "itemCarrinho": itemCarrinho,
        "totalItems": totalItems,
    }

    request.COOKIES['totalCarrinho'] = totalItems

    response = render(request, "carrinho/detailCarrinho.html", contexto)
    
    response.set_cookie('totalCarrinho', totalItems,samesite='Strict')

    return response