from django.urls import path
from apps.carrinho.views import addCarrinho, detailCarrinho, remCarrinho

urlpatterns = [
    path("add/<int:product_id>/", addCarrinho, name="addCarrinho"),
    path("remove/<int:cart_item_id>/", remCarrinho, name="remCarrinho"),
    path("cart", detailCarrinho, name="detailCarrinho"),
]