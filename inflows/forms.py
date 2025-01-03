from django import forms
from . import models


class InflowForm(forms.ModelForm):

    class Meta:
        model = models.Inflow
        fields = ['supplier', 'product', 'quantity', 'descripition']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'qunatity': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'descripition': 'Descrição',
        }
