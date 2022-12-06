from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponse
from perseovsfenix.models import *


def reiniciar_bd_materiales(request):
    matfenix.objects.all().delete()
    matperseo.objects.all().delete()
    NovedadPerseoVsFenix.objects.all().delete()
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def pedidos_fenix(request):
    perseo = matperseo.objects.all()
    fenix = matfenix.objects.all()
    pedidos_fenix = []
    no = []
    cont = 0
    cont2 = 0
    for p in fenix:
        try:
            ped_f = matperseo.objects.get(pedido=p.pedido)
            if ped_f.pedido in pedidos_fenix:
                pass
            else:
                pedidos_fenix.append(ped_f.pedido)
                cont += 1
        except:
            if p.pedido in no:
                pass
            else:
                no.append(p.pedido)
                cont2 += 1
    print("pedidos que no estan en perseo: " + str(len(no)))

    return HttpResponse("termino")  # (request, 'index.html')


def concatenar(pedidos, indicador):
    con = 1
    for p in pedidos:
        if indicador == 1:
            try:
                nombre_cambio_codigo = Guia.objects.get(nombre_perseo=p.codigo)
                p.codigo = nombre_cambio_codigo.nombre_fenix
                p.save()
            except:
                pass
        codigo = p.codigo

        try:
            ultima_letra = codigo[-1]
            if ultima_letra == 'A' or ultima_letra == 'P':
                p.codigo = str(codigo[:-1])
        except:
            pass

        p.concatenacion = str(p.pedido + "-" + p.codigo)
        p.save()


def gestionarbd():
    pedidos_perseo = matperseo.objects.all()
    pedidos_fenix = matfenix.objects.all()

    concatenar(pedidos_fenix, 0)
    concatenar(pedidos_perseo, 1)


def calculo_novedades_perseo_vs_fenix(request):
    gestionarbd()
    calculados = []
    pedidos_perseo = matperseo.objects.all()
    for pedido_perseo in pedidos_perseo:
        if pedido_perseo.concatenacion not in calculados:
            calculados.append(pedido_perseo.concatenacion)
            if pedido_perseo.codigo[:1]=="M" or pedido_perseo.codigo[:1]=="G":
                pass
            else:
                try:
                    cantidad_en_fenix = matfenix.objects.filter(
                        concatenacion=pedido_perseo.concatenacion).aggregate(Sum('cantidad'))
                    cantidad_en_perseo = matperseo.objects.filter(
                        concatenacion=pedido_perseo.concatenacion).aggregate(Sum('cantidad'))
                    print(cantidad_en_fenix)
                    if cantidad_en_fenix['cantidad__sum'] is not None:
                        if float(cantidad_en_fenix['cantidad__sum']) >= 0:
                            if float(cantidad_en_fenix['cantidad__sum']) != float(cantidad_en_perseo['cantidad__sum']):
                                print(pedido_perseo.pedido)
                                print("fenix: " +
                                    str(cantidad_en_fenix['cantidad__sum']))
                                print("perseo: " +
                                    str(cantidad_en_perseo['cantidad__sum']))

                                faltante = NovedadPerseoVsFenix()
                                faltante.concatenacion = pedido_perseo.concatenacion
                                faltante.pedido = pedido_perseo.pedido
                                faltante.actividad = pedido_perseo.actividad
                                faltante.fecha = pedido_perseo.fecha
                                faltante.codigo = pedido_perseo.codigo
                                faltante.cantidad = float(
                                    cantidad_en_perseo['cantidad__sum'])
                                faltante.observacion = "Cantidad no coincide"
                                faltante.acta = pedido_perseo.acta
                                faltante.cantidad_fenix = str(
                                    cantidad_en_fenix['cantidad__sum'])
                                faltante.diferencia = float(
                                    cantidad_en_perseo['cantidad__sum']) - float(cantidad_en_fenix['cantidad__sum'])
                                faltante.save()
                    else:
                        faltante = NovedadPerseoVsFenix()
                        faltante.concatenacion = pedido_perseo.concatenacion
                        faltante.pedido = pedido_perseo.pedido
                        faltante.actividad = pedido_perseo.actividad
                        faltante.fecha = pedido_perseo.fecha
                        faltante.codigo = pedido_perseo.codigo
                        faltante.cantidad = float(
                            cantidad_en_perseo['cantidad__sum'])
                        faltante.observacion = "Item no registrado en Fénix."
                        faltante.acta = pedido_perseo.acta
                        faltante.cantidad_fenix = '-999'
                        faltante.diferencia = '-999'
                        faltante.save()

                except Exception as e:
                    pass

        ped = NovedadPerseoVsFenix.objects.filter(diferencia=0)
        ped.delete()

    calculo_numero_acta()

    novedades = NovedadPerseoVsFenix.objects.all()
    return render(request, 'novedades_perseo_fenix.html', {'novedades': novedades})


def calculo_numero_acta():
    acta = NumeroActa.objects.first()
    pedidos_perseo = matperseo.objects.all()
    con = 1

    for pedido_perseo in pedidos_perseo:
        try:
            if str(pedido_perseo.acta) != str(acta.numero):
                faltante = NovedadPerseoVsFenix()
                faltante.concatenacion = pedido_perseo.concatenacion
                faltante.pedido = pedido_perseo.pedido
                faltante.actividad = pedido_perseo.actividad
                faltante.fecha = pedido_perseo.fecha
                faltante.codigo = pedido_perseo.codigo
                faltante.cantidad = pedido_perseo.cantidad
                faltante.observacion = "Acta incorrecta"
                faltante.acta = pedido_perseo.acta
                faltante.diferencia = -9999
                faltante.save()
        except:
            print("error en el acta")


def reiniciar_novedades_perseo_vs_fenix(request):
    NovedadPerseoVsFenix.objects.all().delete()
    return render(request, 'novedades_perseo_fenix.html', {'novedades': ['']})


def novedades_perseo_vs_fenix(request):
    novedades = NovedadPerseoVsFenix.objects.all()
    return render(request, 'novedades_perseo_fenix.html', {'novedades': novedades})
