from django.contrib import admin
from .models import Pedido, PedidoPlanta

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'email', 'data_entrega')

@admin.register(PedidoPlanta)
class PedidoPlantaAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'planta', 'quantidade')
