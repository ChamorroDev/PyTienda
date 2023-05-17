from django.urls import path

from .views import *




urlpatterns = [
    path('', procesar_pedido, name="procesar_pedido"),
    path('iniciar_pago/', iniciar_pago, name='iniciar_pago'),
    path('retorno_pago/', retorno_pago, name='retorno_pago'),
]