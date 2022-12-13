from django.shortcuts import render, redirect
from bonificaciones.models import *
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.db.models import Sum, Avg, Count


def gestion_fenix(request):
    
    pedidos_fenix = Fenix.objects.all()
    pedidos_modificados = []
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

        pedidos_modificados.append(pf.pedido)
        try:
            pedido = Perseo.objects.filter(pedido=pf.pedido).first()
            pf.instalador = pedido.instalador
            pf.fecha = pedido.fecha[:10]
            pf.save()

        except Exception as e:
            pass

    pedidos_perseo = Perseo.objects.all()
    for pp in pedidos_perseo:
        try:
            pp.calculo_descuento_fenix()
        except Exception as e:
            print(e)


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
        fecha_inicial = request.POST['fecha_inicial']
        fecha_final_str = request.POST['fecha_final']

        instaladores = Perseo.objects.all().only('instalador').order_by('instalador')
        instaladores_calCulados = []

        for inst in instaladores:

            fecha_busqueda = datetime.strptime(fecha_inicial, '%Y-%m-%d')
            fecha_final = datetime.strptime(fecha_final_str, '%Y-%m-%d')

            if inst.instalador not in instaladores_calCulados:
                while fecha_busqueda <= fecha_final:
                    try:
                        res_perseo = sumar_por_fecha_persona(Perseo, fecha_busqueda.strftime(
                            '%Y-%m-%d'), inst.instalador, 'descuento_de_fenix')
                        res_fenix = sumar_por_fecha_persona(
                            Fenix, fecha_busqueda.strftime('%Y-%m-%d'), inst.instalador, 'total')

                        if (res_fenix['total__sum']) is not None:
                            if (res_perseo['descuento_de_fenix__sum']) is None:
                                res_perseo = 0
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
                instaladores_calCulados.append(inst.instalador)

        calculo_promedio_diario()

    else:
        # aquí puedes mostrar el formulario para que el usuario ingrese las fechas
        pass

    return redirect('producido_diario')

def sumar_por_fecha_persona(model, fecha, instalador, total):
    resultados = model.objects.filter(
        fecha=fecha, instalador=instalador).aggregate(Sum(total))
    return resultados


def calculo_promedio_diario():
    instaladores = ProducidoDia.objects.all().only('instalador')
    procesados = []
    for i in instaladores:
        if i.instalador not in procesados:
            try:
                print(i.instalador)
                promedio = ProducidoDia.objects.filter(
                    instalador=i.instalador).aggregate(Avg('producido'))
                producido = ProducidoDia.objects.filter(
                    instalador=i.instalador).aggregate(Sum('producido'))
                numero_de_dias = ProducidoDia.objects.filter(
                    instalador=i.instalador).aggregate(Count('producido'))
                print("Promedio " + str(i.instalador) + ": " + str(promedio))
                print(str(numero_de_dias['producido__count']))
                nuevo_prom = PromedioDiario()
                nuevo_prom.instalador = i.instalador
                nuevo_prom.numero_de_dias_laborados = str(
                    numero_de_dias['producido__count'])
                nuevo_prom.valor_producido_mes = float(
                    producido['producido__sum'])
                nuevo_prom.promedio = promedio['producido__avg']
                nuevo_prom.calculo_bonificacion()
                nuevo_prom.save()

                procesados.append(i.instalador)
            except Exception as e:
                print(e)


def reiniciar_acta_bonificaciones(request):
    Fenix.objects.all().delete()
    Perseo.objects.all().delete()
    ProducidoDia.objects.all().delete()

    producido = ProducidoDia.objects.all()
    return render(request, 'producido_por_dia.html', {'producido': producido})

def producido_diario(request):
    producido = ProducidoDia.objects.all()
    total = producido.aggregate(Sum('producido'))
    
    return render(request, 'producido_por_dia.html', {'producido': producido, 'total':total['producido__sum']})

def bonificaciones(request):
    bonificaciones = PromedioDiario.objects.all()
    return render(request, 'bonificaciones.html', {'bonificaciones':bonificaciones})