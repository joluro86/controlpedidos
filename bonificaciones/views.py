from django.shortcuts import render, redirect
from bonificaciones.models import *
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.db.models import Sum

def gestion_bd_fenix_perseo(request):
    
    """
    pedidos_fenix = PedidoBoniFenix.objects.all()
    cont=0
    identificador_calculado=[]
    for pf in pedidos_fenix:
        try:
            ped = PedidoBoniPerseo.objects.filter(pedido = pf.pedido)
            
            if len(ped)==0:
                pf.instalador = "No está en Perseo"
                pf.save()                
            else:
                for p in ped:
                    p.fecha = p.fecha[0:10]
                    p.save()    
                    if p.pedido in identificador_calculado:
                        
                        pass
                    else:
                        if (p.codigo[0] >= '0' and p.codigo[0] <= '9'):
                            pass
                        else:
                            p.descuento_de_fenix=p.total
                            p.save()                    

                    pf.instalador = p.instalador
                    pf.fecha = p.fecha[0:10]

                    if pf.urbrur=='R':
                        pf.total = (float(pf.valor))*1.27
                    else:
                        pf.total = (float(pf.valor))*1.17

                    pf.save()
        except:
            print(str(pf.pedido)+ " : pedido no esta en perseo")
    """
    calculo_diario_instalador(0, 1)

    return HttpResponse('Ya terminó')

def calculo_diario_instalador(fecha_ini, fecha_fin):

    fecha_inicial_str = '2022-11-01'
    fecha_final_str = '2022-11-10'
    fecha_inicial = datetime.strptime(fecha_inicial_str, '%Y-%m-%d')
    fecha_final = datetime.strptime(fecha_final_str, '%Y-%m-%d')
    
    instaladores = PedidoBoniPerseo.objects.all().only('instalador').order_by('instalador')
    calulados=[]
    for inst in instaladores:
        
        fecha_busqueda = fecha_inicial
        if inst.instalador in calulados:
            
            pass
        else:
            print(fecha_busqueda)
            while fecha_busqueda.date()<=fecha_final.date():
                
                valor_perseo = PedidoBoniPerseo.objects.filter(instalador=inst.instalador, fecha=fecha_busqueda).aggregate(Sum('descuento_de_fenix'))
                valor_fenix = PedidoBoniFenix.objects.filter(instalador=inst.instalador, fecha=fecha_busqueda).aggregate(Sum('total'))
                
                print(inst.instalador)
                print(valor_perseo)
                print(valor_fenix)
                fecha_busqueda = (fecha_busqueda + timedelta(days=7)).date()
            calulados.append(inst.instalador)
        

def calcalulo_bonificaciones(request):
    calculo_valor_pedidos()
    #calcular_bonificacion_diaria()

    return redirect('datos_por_pedido')


def calculo_valor_pedidos():
    pass


# RETORNA EL VALOR DE LOS MATERIALES QUE MEJIA PONE
def calculo_identificador_perseo(pedido):
    pedidos = PedidoBoniPerseo.objects.filter(pedido=pedido)
    valor = 0
    print("tam: " + str(len(pedidos)))

    for p in pedidos:
        if (p.codigo[0] >= '0' and p.codigo[0] <= '9'):
            pass
        else:
            p.descuento_de_fenix=p.total
            p.save()
            valor+=float(p.total)
    print(valor)    




# GUARDA EL VALOR DE LA BONIFICACION POR PEDIDO
def crear_valor_por_pedido(pedido, instalador, fecha, valor_perseo, valor_fenix):
    pass


def reiniciar_acta_bonificaciones(request):
    
    return redirect('datos_por_pedido')


def datos_por_pedido(request):
    pass

def calcular_pducido_diario(fecha_inicial, fecha_final):
    pass


def guardar_bonificacion_diaria(instalador, valor_dia, fecha, bonificacion):
    pass


def producido_diario(request):
    producido = ProducidoDia.objects.all()
    return render(request, 'producido_por_dia.html', {'producido': producido})
