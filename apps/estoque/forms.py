from typing import Any
from django import forms

from apps.estoque.models import Material

class MaterialForms(forms.ModelForm):
    class Meta:
        model = Material
        exclude = []
        labels = {
            "desc":"Descrição",
            "categoria":"Categoria",
            "qtd":"QTD",
            "tipo":"Tipo",
            "foto":"Foto",
        }

        widgets = {
            "desc": forms.TextInput(attrs={"class":"form-control"}),
            "categoria": forms.TextInput(attrs={"class":"form-control"}),
            "qtd": forms.Select(attrs={"class":"form-control"}),
            "tipo": forms.Textarea(attrs={"class":"form-control"}),
            "foto": forms.FileInput(attrs={"class":"form-control"}),
        }