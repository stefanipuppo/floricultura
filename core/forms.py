from django import forms
from .models import Planta
from .models import Cliente

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['nome', 'especie', 'descricao', 'preco', 'estoque']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'senha']  