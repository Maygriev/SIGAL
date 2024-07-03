from django.db import models
from django.contrib.auth.models import User
from apps.estoque.models import Material
from django.urls import reverse

class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Material, on_delete=models.CASCADE)
    itemDesc = models.CharField(max_length=100, null=False, blank=False)
    qtd = models.DecimalField(default=1, max_digits=8, decimal_places=1, null=False, blank=False)

    def __str__(self):
        return f"{self.qtd} x {self.itemDesc}"

    def get_absolute_url(self):
        return reverse("carrinho:detailCarrinho")