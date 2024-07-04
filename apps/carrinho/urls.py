from django.urls import path
from apps.carrinho.views import addCarrinho, detailCarrinho, remCarrinho, updCarrinho

urlpatterns = [
    path("add-carrinho/<int:itemID>/", addCarrinho, name="add-carrinho"),
    path("rem-carrinho/<int:carrinhoItemID>/", remCarrinho, name="rem-carrinho"),
    path("upd-carrinho/<int:carrinhoItemID>/", updCarrinho, name="upd-carrinho"),
    path("carrinho", detailCarrinho, name="detail-carrinho"),
]