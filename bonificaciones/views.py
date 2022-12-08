from django.shortcuts import render, redirect
from bonificaciones.models import *
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.db.models import Sum


def gestion_fenix(request):

    
    print("llegue carajo")
    """
    # analisis_fechas_pedidos_perseo()
    pedidos_fenix = Fenix.objects.all()
    pedidos_modificados = []
    cont = 0

    for pf in pedidos_fenix:
        try:
            if pf.tipo == "CON":
                if pf.urbrur == "R":
                    pf.total = float(pf.valor)*1.27
                else:
                    pf.total = float(pf.valor)*1.17
            pf.save()
        except Exception as e:
            print("excepcion total: " + str(e))

        if pf.pedido in pedidos_modificados:
            pass
        else:
            try:
                primer = Perseo.objects.filter(pedido=pf.pedido).first()
                Fenix.objects.filter(pedido=primer.pedido).update(
                    instalador=primer.instalador, fecha=primer.fecha[:10])
                con = Fenix.objects.filter(pedido=primer.pedido)
                print(len(con))
                pedidos_modificados.append(pf.pedido)
            except Exception as e:
                pass

    pedidos_perseo = Perseo.objects.all()
    print(len(pedidos_perseo))
    for pp in pedidos_perseo:
        try:
            print(pp)
            pp.calculo_descuento_fenix()
        except Exception as e:
            print(e)
    """

    calculo_diario_instalador(0,1)

    return HttpResponse('Ya terminó FENIX')


def analisis_fechas_pedidos_perseo():
    pedidos = Perseo.objects.only('pedido')
    analizados = []
    cont = 0
    for p in pedidos:
        if p.pedido in analizados:
            pass
        else:
            ped = Perseo.objects.filter(pedido=p.pedido).only('pedido')
            encontrados = []
            for pe in ped:

                if pe.fecha[:10] in encontrados:
                    pass
                else:
                    encontrados.append(pe.fecha[:10])

            if len(encontrados) > 1:
                novedad = NovedadBonificacion()
                novedad.pedido = p.pedido
                novedad.descripcion = "Pedido con mas de una fecha"
                novedad.save()

            analizados.append(p.pedido)


def calculo_diario_instalador(fecha_ini, fecha_fin):
    print("llegue al calculo")
    fecha_inicial = '2022-11-01'
    fecha_final_str = '2022-12-03'

    instaladores = Perseo.objects.all().only('instalador').order_by('instalador')
    instaladores_calCulados = []
    cont = 0
    for inst in instaladores:

        cont += 1
        fecha_busqueda = datetime.strptime(fecha_inicial, '%Y-%m-%d')
        fecha_final = datetime.strptime(fecha_final_str, '%Y-%m-%d')

        if inst.instalador in instaladores_calCulados:
            pass
        else:

            while fecha_busqueda <= fecha_final:
                print(fecha_busqueda)
                try:
                    valor_perseo = Perseo.objects.filter(instalador=inst.instalador).filter(
                        fecha=fecha_busqueda.strftime('%Y-%m-%d')).aggregate(Sum('descuento_de_fenix'))
                    valor_fenix = Fenix.objects.filter(instalador=inst.instalador).filter(
                        fecha=fecha_busqueda.strftime('%Y-%m-%d')).aggregate(Sum('total'))
                    if valor_fenix['total__sum'] is None and valor_perseo['descuento_de_fenix__sum'] is None:
                        print(valor_fenix)
                        print(valor_perseo)
                        producido_dia = ProducidoDia()
                        producido_dia.instalador = inst.instalador
                        producido_dia.fecha = fecha_busqueda.strftime(
                            '%Y-%m-%d')
                        producido_dia.valor_fenix = str(
                            valor_fenix['total__sum'])
                        producido_dia.valor_perseo_descuento = str(
                            valor_perseo['descuento_de_fenix__sum'])
                        producido_dia.producido = float(
                            valor_fenix['total__sum'])-float(valor_perseo['descuento_de_fenix__sum'])
                        producido_dia.save()

                except Exception as e:
                    print(str(e)+ " " + str(inst.instalador))

                fecha_busqueda = (fecha_busqueda + timedelta(days=1))
            instaladores_calCulados.append(inst.instalador)
    
    return HttpResponse('Ya terminó calculo')

def calcalulo_bonificaciones(request):
    calculo_valor_pedidos()
    # calcular_bonificacion_diaria()

    return redirect('datos_por_pedido')


def calculo_valor_pedidos():
    pass


# RETORNA EL VALOR DE LOS MATERIALES QUE MEJIA PONE
def calculo_identificador_perseo(pedido):
    pedidos = Perseo.objects.filter(pedido=pedido)
    valor = 0
    print("tam: " + str(len(pedidos)))

    for p in pedidos:
        if (p.codigo[0] >= '0' and p.codigo[0] <= '9'):
            pass
        else:
            p.descuento_de_fenix = p.total
            p.save()
            valor += float(p.total)
    print(valor)

# GUARDA EL VALOR DE LA BONIFICACION POR PEDIDO


def crear_valor_por_pedido(pedido, instalador, fecha, valor_perseo, valor_fenix):
    pass


def reiniciar_acta_bonificaciones(request):
    Fenix.objects.all().delete()
    Perseo.objects.all().delete()
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
