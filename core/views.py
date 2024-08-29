from django.shortcuts import render, get_object_or_404, redirect
from .models import Planta
from .forms import PlantaForm
from .forms import ClienteForm
from django.contrib import messages

def home(request):
    return render(request, 'core/home.html')

def cliente_novo(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente salvo com sucesso!')
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_form.html', {'form': form})

def lista(request):
    plantas = Planta.objects.all()
    return render(request, 'core/lista.html', {'plantas': plantas})

def detalhes(request, pk):
    planta = get_object_or_404(Planta, pk=pk)
    return render(request, 'core/detalhes.html', {'planta': planta})

def planta_nova(request):
    if request.method == 'POST':
        form = PlantaForm(request.POST)
        if form.is_valid():
            planta = form.save()
            return redirect('detalhes', pk=planta.pk)
    else:
        form = PlantaForm()
    return render(request, 'core/editar.html', {'form': form})

def editar(request, pk):
    planta = get_object_or_404(Planta, pk=pk)
    if request.method == 'POST':
        form = PlantaForm(request.POST, instance=planta)
        if form.is_valid():
            planta = form.save()
            return redirect('detalhes', pk=planta.pk)
    else:
        form = PlantaForm(instance=planta)
    return render(request, 'core/editar.html', {'form': form})

def deletar(request, pk):
    planta = get_object_or_404(Planta, pk=pk)
    planta.delete()
    return redirect('lista')

def pedido(request):
    return render(request, 'pedido/pedido_form.html')