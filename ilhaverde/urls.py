from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('novo/', include('cliente.urls')),
    path('pedido/', include('pedido.urls')),
    
]
