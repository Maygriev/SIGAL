from django.db import models

from datetime import datetime
from django.contrib.auth.models import User
from apps.estoque.models import Material

class Requisition(models.Model):
    OPCOES_STATUS = [
        ("PENDENTE", "Pendente"),
        ("APROVADA", "Aprovada"),
        ("CANCELADA", "Cancelada"),
        ("REPROVADA", "Reprovada"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Material, through="RequisitionItem")
    status = models.CharField(max_length=100, choices=OPCOES_STATUS, default="PENDENTE")
    dateReq = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"Requisição #{self.id}"
    
class RequisitionItem(models.Model):
    itemReq = models.ForeignKey(Requisition, on_delete=models.CASCADE)
    itemMat = models.ForeignKey(Material, on_delete=models.CASCADE)
    itemQtd = models.IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.itemQtd} x {self.itemMat.desc}"