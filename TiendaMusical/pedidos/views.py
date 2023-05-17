from django.contrib import messages
from django.shortcuts import redirect,render
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido
from pedidos.models import  Pedido
from django.contrib.auth.decorators import login_required
from tienda.models import Disco
from transbank.webpay.webpay_plus.transaction import Transaction
from django.http import HttpResponse
from django.conf import settings

import random

def iniciar_pago(request,response):
   

    # Redirecciona al usuario a Webpay
    return render(request,'create.html', {"response":response})



def retorno_pago(request):
    print(request)

    token = request.GET.get('token_ws')  # Obtén el token de la transacción desde la URL
    print("commit for token_ws: {}".format(token))
    # Obtén los detalles de la transacción desde Webpay
    response = (Transaction()).commit(token=token)
    
    if response['status']== 'AUTHORIZED' :
        pedido= LineaPedido.objects.filter(pedido_id=int(response['buy_order']))
        for ped in pedido:
            
             v_vendidos = Disco.objects.filter(id=ped.producto_id).values('vendidos').first()
             v_vendidos = int(v_vendidos['vendidos'])
             v_stock = Disco.objects.filter(id=ped.producto_id).values('stock').first()
             v_stock = int(v_stock['stock'])
             Disco.objects.filter(id=ped.producto_id).update(vendidos=ped.cantidad+v_vendidos, stock=v_stock-ped.cantidad)
        LineaPedido.objects.bulk_create(pedido)
        messages.success(request,"El pago confirmado correctamente")

        # Transacción exitosa, actualiza el estado del pedido en tu base de datos
        # y muestra una página de confirmación al usuario
        return render(request, 'confirmacion.html')
    if response['status']== 'FAILED':
        # Transacción fallida, muestra una página de error al usuario
        return render(request, 'error.html')


@login_required(login_url="Home")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    total=0
    for key,value in request.session["carro"].items():
            total=total+(int(value["precio"])) 

    orden_compra = str(pedido.id) 
    return_url= 'http://localhost:8000/pedidos/retorno_pago/'
    s_id=str(random.randrange(1000000, 99999999))

    response = (Transaction()).create(orden_compra, s_id, total, return_url)

    return render(request,"create.html", {"response":response})


"""
response: {'vci': 'TSY', 'amount': 1, 'status': 'AUTHORIZED', 'buy_order': '64333337',
            'session_id': '39998857', 'card_detail': {'card_number': '6623'},
              'accounting_date': '0516', 'transaction_date': '2023-05-16T15:27:57.247Z', 'authorization_code': '1213',
            'payment_type_code': 'VN', 'response_code': 0, 'installments_number': 0}"""