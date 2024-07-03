from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from apps.carrinho.models import Carrinho

def addCarrinho(request, itemID):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    itemCarrinho = Carrinho.objects.filter(user=request.user, product=itemID).first()

    if itemCarrinho:
        itemCarrinho.qtd += 1
        itemCarrinho.save()
        messages.success(request, itemCarrinho + " adicionado ao Carrinho")
    else:
        Carrinho.objects.create(user=request.user,item=itemID)
        messages.success(request, itemCarrinho + " adicionado ao Carrinho")

    return redirect("cart:detailCarrinho")

def remCarrinho(request, carrinhoItemID):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    itemCarrinho = get_object_or_404(Carrinho, id=carrinhoItemID)

    if itemCarrinho.user == request.user:
        itemCarrinho.delete()
        messages.success(request, itemCarrinho + " removido do seu Carrinho.")

    return redirect("cart:detailCarrinho")

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