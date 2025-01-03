from django import forms
from . import models


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = ['name', 'descripition']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'descripition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nome',
            'descripition': 'Descrição',
        }
