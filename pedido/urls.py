from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.pedido_form, name='pedido_novo'),
    path('lista/', views.pedido_lista, name='pedido_lista'),
    path('excluir/<int:pk>/', views.pedido_excluir, name='pedido_excluir'),
    

]
