from django.urls import path
from apps.carrinho.views import addCarrinho, detailCarrinho, remCarrinho

urlpatterns = [
    path("add/<int:itemID>/", addCarrinho, name="add-carrinho"),
    path("remove/<int:carrinhoItemID>/", remCarrinho, name="rem-carrinho"),
    path("cart", detailCarrinho, name="detail-carrinho"),
]