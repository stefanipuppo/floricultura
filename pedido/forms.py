from django import forms
from .models import Pedido
from core.models import Planta
from cliente.models import Cliente


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'email', 'data_entrega']

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=False)
    planta = forms.ModelChoiceField(queryset=Planta.objects.all(), required=False)
    quantidade = forms.IntegerField(min_value=1, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['planta'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['data_entrega'].widget = forms.DateInput(attrs={'type': 'date'})