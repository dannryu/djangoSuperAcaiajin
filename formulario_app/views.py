# views.py

from django.shortcuts import render, redirect
from .forms import FormularioForm

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
