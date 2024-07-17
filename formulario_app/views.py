from django.shortcuts import render, redirect
from .models import Formulario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FormularioForm, CustomUserCreationForm, CustomAuthenticationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para o login
    else:
        form = CustomUserCreationForm()
    return render(request, 'formulario_app/register.html', {'form': form})

@login_required(login_url='login')  # Requer login
def formulario_view(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FormularioForm()
    return render(request, 'formulario_app/formulario.html', {'form': form})

def success_view(request):
    return render(request, 'formulario_app/success.html')

def listar_formularios_view(request):
    formularios = Formulario.objects.all()
    return render(request, 'formulario_app/listar_formularios.html', {'formularios': formularios})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)  # Use AuthenticationForm
        if form.is_valid():
            # Autenticação e login
            user = form.get_user()
            login(request, user)
            return redirect('formulario')  # Redireciona para o formulário
    else:
        form = CustomAuthenticationForm()
    return render(request, 'formulario_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login