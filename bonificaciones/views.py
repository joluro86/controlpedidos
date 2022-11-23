from django.shortcuts import render, redirect
from bonificaciones.models import *

def calcalulo_bonificaciones(request):
    calculo_valor_pedidos_perseo()
    calculo_valor_pedidos_fenix()

    redirect('bonificaciones')


def calculo_valor_pedidos_perseo():
    
    pedidos = PedidoBoniPerseo.objects.all().only('pedido')
    for p in pedidos:
        pedido = 0
    

def calculo_valor_pedidos_fenix():
    pass

def reiniciar_acta_bonificaciones(request):
    pass


def bonificaciones(request):
    bonificaciones= ValorBonificacion.objects.all()
    return render(request, 'bonificaciones.html', {'pedidos':bonificaciones})

