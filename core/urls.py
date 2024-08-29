from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista, name='lista'),
    path('planta/<int:pk>/', views.detalhes, name='detalhes'),
    path('planta/planta_nova/', views.planta_nova, name='planta_nova'),
    path('planta/<int:pk>/editar/', views.editar, name='editar'),
    path('planta/<int:pk>/deletar/', views.deletar, name='deletar'),
    path('cliente_novo/', views.cliente_novo, name='cliente_novo'),
    path('pedido/', views.pedido, name='pedido'),
]
