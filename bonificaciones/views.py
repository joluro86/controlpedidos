from django.shortcuts import render, redirect
from bonificaciones.models import *
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.db.models import Sum

def gestion_bd_fenix_perseo(request):
    
    analisis_fechas_pedidos_perseo()
    pedidos_fenix = PedidoBoniFenix.objects.all()

    identificador_calculado=[]
    for pf in pedidos_fenix:

        if pf.pedido in identificador_calculado:
            pass
        else:
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

                        pf.save()
            except:
                pass
        
        if str(pf.tipo)=='CON':
            print("entre a con")
            if pf.urbrur=='R':
                pf.total = (float(pf.valor))*1.27
            else:
                pf.total = (float(pf.valor))*1.17
            pf.save()

        identificador_calculado.append(pf.pedido)
    
    calculo_diario_instalador(0, 1)  

    return HttpResponse('Ya terminó')

def analisis_fechas_pedidos_perseo():
    pedidos = PedidoBoniPerseo.objects.only('pedido')
    analizados = []
    cont=0
    for p in pedidos:
        if p.pedido in analizados:
            pass
        else:
            ped = PedidoBoniPerseo.objects.filter(pedido=p.pedido).only('pedido')
            print(len(ped))
            encontrados = []
            for pe in ped:
                
                if pe.fecha[:10] in encontrados:
                    pass
                else:
                        encontrados.append(pe.fecha[:10])
                        
            if len(encontrados)>1:
                novedad = NovedadBonificacion()
                novedad.pedido = p.pedido
                novedad.descripcion = "Pedido con mas de una fecha"
                novedad.save()

            analizados.append(p.pedido)

def calculo_diario_instalador(fecha_ini, fecha_fin):
    print("llegue al calculo")
    fecha_inicial = '2022-11-21'
    fecha_final_str = '2022-11-25'
    
    instaladores = PedidoBoniPerseo.objects.all().only('instalador').order_by('instalador')
    calulados=[]
    for inst in instaladores:
        
        fecha_busqueda = datetime.strptime(fecha_inicial, '%Y-%m-%d')
        fecha_final = datetime.strptime(fecha_final_str, '%Y-%m-%d')

        if inst.instalador in calulados:            
            pass
        else:
            while fecha_busqueda<=fecha_final:
                try:
                    valor_perseo = PedidoBoniPerseo.objects.filter(instalador=inst.instalador).filter(fecha=fecha_busqueda.strftime('%Y-%m-%d')).aggregate(Sum('descuento_de_fenix'))
                    valor_fenix = PedidoBoniFenix.objects.filter(instalador=inst.instalador).filter(fecha=fecha_busqueda.strftime('%Y-%m-%d')).aggregate(Sum('total'))
                    
                    producido_dia = ProducidoDia()
                    producido_dia.instalador = inst.instalador
                    producido_dia.fecha = fecha_busqueda.strftime('%Y-%m-%d')
                    producido_dia.valor_fenix = str(valor_fenix['total__sum'])
                    producido_dia.valor_perseo_descuento = str(valor_perseo['descuento_de_fenix__sum'])
                    producido_dia.producido = float(valor_fenix['total__sum'])-float(valor_perseo['descuento_de_fenix__sum'])
                    producido_dia.save()
        
                    print(inst.instalador)
                    print(fecha_busqueda)
                    print("tamaño perseo: " + str((valor_perseo['descuento_de_fenix__sum'])))
                    print("tamaño fenix: " + str((valor_fenix['total__sum'])))
                except:
                    pass                   
                
                
                fecha_busqueda = (fecha_busqueda + timedelta(days=1))
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
    PedidoBoniFenix.objects.all().delete()
    PedidoBoniPerseo.objects.all().delete()
    ProducidoDia.objects.all().delete()

    producido = ProducidoDia.objects.all()
    return render(request, 'producido_por_dia.html', {'producido': producido})



def datos_por_pedido(request):
    pass

def calcular_pducido_diario(fecha_inicial, fecha_final):
    pass


def guardar_bonificacion_diaria(instalador, valor_dia, fecha, bonificacion):
    pass


def producido_diario(request):
    producido = ProducidoDia.objects.all()
    return render(request, 'producido_por_dia.html', {'producido': producido})
