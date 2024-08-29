from django.shortcuts import get_object_or_404, render, redirect
from core.models import Planta
from .models import Pedido, PedidoPlanta
from .forms import PedidoForm

def pedido_form(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            planta_id = request.POST.get('planta')
            quantidade = request.POST.get('quantidade')
            if planta_id and quantidade:
                planta = get_object_or_404(Planta, id=planta_id)
                PedidoPlanta.objects.create(pedido=pedido, planta=planta, quantidade=quantidade)
            return redirect('pedido_lista')
    else:
        form = PedidoForm()
    return render(request, 'pedido/pedido_form.html', {'form': form})

def pedido_lista(request):
    pedidos = Pedido.objects.all()

    return render(request, 'pedido/pedido_lista.html', {'pedidos': pedidos})


def pedido_excluir(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        pedido.delete()
        return redirect('pedido_lista')

