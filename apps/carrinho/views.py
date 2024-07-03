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
    
    itemCarrinho = get_object_or_404(Carrinho, id=carrinhoItemID)

    if itemCarrinho.user == request.user:
        itemCarrinho.delete()
        messages.success(request, itemCarrinho + " removido do seu Carrinho.")

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

    return render(request, "carrinho/detailCarrinho.html", contexto)