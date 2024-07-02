from django.db import models

class Material(models.Model):
    OPCOES_CATEGORIA = [
        ("MAT-TIC", "Material de TIC"),
        ("MAT-EXPEDIENTE", "Material de Expediente"),
        ("MAT-ESCRITORIO", "Material de Escritório"),
    ]

    OPCOES_MEDIDA = [
        ("UND", "Unidade"),
        ("KG", "Quilograma"),
        ("PCT", "Pacote"),
    ]

    desc = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")
    qtd = models.DecimalField(max_digits=8, decimal_places=1, null=False, blank=False)
    tipo = models.CharField(max_length=100, choices=OPCOES_MEDIDA, default="UND")
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.desc