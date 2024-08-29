from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.cliente_novo, name='cliente_novo'),
]
