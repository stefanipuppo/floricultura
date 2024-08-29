from django.db import models
from core.models import Planta

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    plantas = models.ManyToManyField(Planta, through='PedidoPlanta')
    data_entrega = models.DateField()
 

class PedidoPlanta(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
