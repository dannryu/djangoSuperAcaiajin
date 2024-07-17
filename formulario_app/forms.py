# forms.py

from django import forms
from .models import Formulario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

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

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField (
        label='Nome de Usuário',
        help_text=None  # Removendo o help_text
    )

    password1 = forms.CharField(
        label='Senha:',
        help_text=None
    )

    password2 = forms.CharField(
        label='Repita a senha:',
        help_text=None
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')
        labels = {
            'email': 'Endereço de Email',
            'username': 'Nome de Usuário',
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Nome de Usuário',
        #widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text=None  # Remove o help_text do campo username
    )
    password = forms.CharField(
        label='Senha',
        strip=False,
        #widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=None  # Remove o help_text do campo password
    )