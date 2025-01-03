from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'descripition']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'qunatity': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):  # Validando se ha quantidade suficiente para dar Saida.
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade em estoque para o produto {product.title} é de {product.quantity} unidades'
            )

        return quantity
