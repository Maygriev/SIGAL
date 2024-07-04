from django.db import models
from django.contrib.auth.models import User
from apps.estoque.models import Material

class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Material, on_delete=models.CASCADE)
    itemDesc = models.CharField(max_length=100, null=False, blank=False)
    qtd = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.qtd} x {self.itemDesc}"