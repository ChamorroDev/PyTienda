from django.contrib import messages
from django.shortcuts import redirect
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido
from pedidos.models import  Pedido
from django.contrib.auth.decorators import login_required
from tienda.models import Disco


@login_required(login_url="Home")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items():
        lineas_pedido.append(LineaPedido(producto_id=key,cantidad=value["cantidad"],user=request.user,pedido=pedido))
        v_vendidos = Disco.objects.filter(id=key).values('vendidos').first()
        v_vendidos = int(v_vendidos['vendidos'])
        v_stock = Disco.objects.filter(id=key).values('stock').first()
        v_stock = int(v_stock['stock'])
        Disco.objects.filter(id=key).update(vendidos=value["cantidad"]+v_vendidos, stock=v_stock-value["cantidad"])

    LineaPedido.objects.bulk_create(lineas_pedido)
    messages.success(request,"El pedido se ha creado correctamente")
    carro.limpiar_carro()
    return redirect("Tienda")