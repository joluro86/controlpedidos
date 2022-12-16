from django.shortcuts import render, redirect
from bonificaciones.models import *
from datetime import datetime, timedelta
from django.db.models import Sum, Avg, Count, F
import time


def gestion_fenix(request):
    inicio = time.time()
    todos = Fenix.objects.all()
    try:
        pedidos_rurales = todos.filter(tipo="CON", urbrur="R")
        pedidos_rurales.update(total=F('valor')*1.27)

        pedidos_urbanos = todos.filter(tipo="CON", urbrur="U")
        pedidos_urbanos.update(total=F('valor')*1.17)
    except Exception as e:
        print("excepcion al calculo valor segun urbano o rural" + str(e))

    pedidos_fenix = Fenix.objects.distinct('pedido')

    for pf in pedidos_fenix:
        try:
            pedido_perseo = Perseo.objects.filter(pedido=pf.pedido).first()
            pedidos_perseo_update_fecha = Perseo.objects.filter(
                pedido=pf.pedido)
            pedidos_perseo_update_fecha.update(fecha=pedido_perseo.fecha[:10])

            pedidos_fenix = Fenix.objects.filter(pedido=pf.pedido)
            pedidos_fenix.update(
                instalador=pedido_perseo.instalador, fecha=pedido_perseo.fecha[:10])

        except Exception as e:
            pass

    todos_perseo = Perseo.objects.all()
    print(len(todos_perseo))
    pedidos_perseo_descuento = todos_perseo.filter(codigo__startswith="M") | todos_perseo.filter(codigo__startswith="G")
    
    print(len(pedidos_perseo_descuento))
    pedidos_perseo_descuento.update(descuento_de_fenix=F('total'))

    fin = time.time()

    print("tiempo: " + str(fin-inicio))

    return render(request, 'proceso_gestion.html')

def producido_rango_fechas(request):
    return render(request, 'proceso_gestion.html')

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


def calculo_diario_instalador(request):
    if request.method == 'POST':
        
        try:
            fecha_inicial = request.POST['fecha_inicial']
            fecha_final_str = request.POST['fecha_final']

            instaladores = Perseo.objects.distinct('instalador')

            for inst in instaladores:

                fecha_busqueda = datetime.strptime(fecha_inicial, '%Y-%m-%d')
                fecha_final = datetime.strptime(fecha_final_str, '%Y-%m-%d')
                print(inst.instalador)

                while fecha_busqueda <= fecha_final:
                    print(fecha_busqueda)

                    res_perseo = sumar_por_fecha_persona(Perseo, fecha_busqueda.strftime(
                        '%Y-%m-%d'), inst.instalador, 'descuento_de_fenix')
                    res_fenix = sumar_por_fecha_persona(
                        Fenix, fecha_busqueda.strftime('%Y-%m-%d'), inst.instalador, 'total')

                    if (res_perseo['descuento_de_fenix__sum']) is None:
                        novedad = NovedadBonificacion()
                        novedad.pedido = inst.instalador
                        novedad.descripcion = str(fecha_busqueda) + " sin material de Mejía"
                        novedad.save()

                    if (res_fenix['total__sum']) is not None:
                        if (res_perseo['descuento_de_fenix__sum']) is None:
                            res_perseo['descuento_de_fenix__sum'] = 0

                        print("fenix: " +
                              str(res_perseo['descuento_de_fenix__sum']))
                        print("perseo: " + str(res_fenix['total__sum']))

                        valor_diario = ProducidoDia()
                        valor_diario.instalador = inst.instalador
                        valor_diario.fecha = fecha_busqueda.strftime(
                            '%Y-%m-%d')
                        valor_diario.valor_fenix = float(
                            res_fenix['total__sum'])
                        valor_diario.valor_perseo_descuento = float(
                            res_perseo['descuento_de_fenix__sum'])
                        valor_diario.producido = float(
                            res_fenix['total__sum']) - float(res_perseo['descuento_de_fenix__sum'])
                        valor_diario.save()

                    fecha_busqueda = (fecha_busqueda + timedelta(days=1))

        except Exception as e:
            print(e)
        
        calculo_promedio_diario()

    return redirect('producido_diario')


def sumar_por_fecha_persona(model, fecha, instalador, total):
    resultados = model.objects.filter(
        fecha=fecha, instalador=instalador).aggregate(Sum(total))
    return resultados


def calculo_promedio_diario():
    instaladores = ProducidoDia.objects.distinct('instalador')
    for i in instaladores:
            try:
                print(i.instalador)
                
                producido = ProducidoDia.objects.filter(
                    instalador=i.instalador).aggregate(Sum('producido'))

                numero_de_dias = ProducidoDia.objects.filter(
                    instalador=i.instalador).aggregate(Count('producido'))

                adicional = float(producido['producido__sum'])-(float(numero_de_dias['producido__count'])*1000000)

                nuevo_prom = PromedioDiario()
                nuevo_prom.instalador = i.instalador
                nuevo_prom.numero_de_dias_laborados = str(numero_de_dias['producido__count'])
                nuevo_prom.valor_producido_mes = float(producido['producido__sum'])
                nuevo_prom.adicional = float(adicional)
                nuevo_prom.bonificacion_cuadrilla = float(adicional)*0.3
                nuevo_prom.bonificacion_persona = (float(adicional)*0.3)/3
                nuevo_prom.save()

            except Exception as e:
                print(e)


def reiniciar_acta_bonificaciones(request):
    Fenix.objects.all().delete()
    Perseo.objects.all().delete()

    producido = ProducidoDia.objects.all()
    return render(request, 'producido_por_dia.html', {'producido': producido})

def reiniciar_bonificaciones(request):
    PromedioDiario.objects.all().delete()
    return redirect('bonificaciones')

def producido_diario(request):
    producido = ProducidoDia.objects.all()
    total = producido.aggregate(Sum('producido'))

    return render(request, 'producido_por_dia.html', {'producido': producido, 'total': total['producido__sum']})


def bonificaciones(request):
    bonificaciones = PromedioDiario.objects.all()
    return render(request, 'bonificaciones.html', {'bonificaciones': bonificaciones})
