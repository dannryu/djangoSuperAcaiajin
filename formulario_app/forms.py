# forms.py

from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'nome', 'idade', 'telefone', 'endereco', 'planeta_origem',
            'raca_preferida', 'trabalho', 'acai_preferido', 'tamanho_preferido', 'observacoes'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefone': forms.NumberInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'planeta_origem': forms.Select(attrs={'class': 'form-control'}),
            'raca_preferida': forms.Select(attrs={'class': 'form-control'}),
            'trabalho': forms.RadioSelect(attrs={'class': 'form-radio'}),
            'acai_preferido': forms.RadioSelect(choices=Formulario.ACAI_CHOICES, attrs={'class': 'form-radio'}),
            'tamanho_preferido': forms.RadioSelect(choices=Formulario.TAMANHO_CHOICES, attrs={'class': 'form-radio'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
        }
