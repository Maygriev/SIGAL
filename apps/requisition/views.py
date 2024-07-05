from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.core.paginator import Paginator

from apps.carrinho.models import Carrinho
from apps.requisition.models import Requisition, RequisitionItem

def viewRequisition(request, reqID):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    req = get_object_or_404(Requisition, id=reqID)
        
    return render(request, 'requisition/viewRequisition.html', {'req':req})

def addRequisition(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    carrinho = Carrinho.objects.filter(user=request.user)

    req = Requisition.objects.create(user=request.user)

    for itemCart in carrinho:
        reqItem = RequisitionItem.objects.create(itemReq=req, itemMat=itemCart.item, itemQtd=itemCart.qtd)
        reqItem.save()
        itemCart.delete()

    req.save()

    messages.success(request, 'Requisição enviada com sucesso')

    response = redirect("my-requisitions")
    response.delete_cookie("totalCarrinho")

    return response

def myRequisitions(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    items = Requisition.objects.order_by("-dateReq")
    items = Paginator(items, 20)
    page_number = request.GET.get("page")
    page_obj = items.get_page(page_number)
    
    return render(request, 'requisition/myRequisition.html', {"cards": page_obj})