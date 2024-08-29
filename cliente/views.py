from django.shortcuts import render
from .forms import ClienteForm
from .models import Cliente
from django.contrib import messages

def cliente_novo(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente salvo com sucesso!')
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_form.html', {'form': form})
