from django.shortcuts import render
from django.db.models import Sum
from perseovsfenix.models import *


def reiniciar_bd_materiales(request):
    matfenix.objects.all().delete()
    matperseo.objects.all().delete()
    NovedadPerseoVsFenix.objects.all().delete()
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def concatenar(pedidos, indicador):
    calculados_existencia = []
    for p in pedidos:

        if indicador == 1:

            if p.pedido not in calculados_existencia:
                numero_pedidos_perseo_en_fenix = matfenix.objects.filter(
                    pedido=p.pedido).count()
                if numero_pedidos_perseo_en_fenix < 1:
                    faltante = NovedadPerseoVsFenix()
                    faltante.concatenacion = p.concatenacion
                    faltante.pedido = p.pedido
                    faltante.actividad = p.actividad
                    faltante.fecha = p.fecha
                    faltante.codigo = p.codigo
                    faltante.cantidad = '0'
                    faltante.observacion = "Pedido con cero registros en Fénix."
                    faltante.acta = p.acta
                    faltante.cantidad_fenix = '0'
                    faltante.diferencia = '0'
                    faltante.save()

                calculados_existencia.append(p.pedido)

            try:
                nombre_cambio_codigo = Guia.objects.get(nombre_perseo=p.codigo)
                p.codigo = nombre_cambio_codigo.nombre_fenix
                p.save()
            except:
                pass
        codigo = p.codigo

        if indicador == 0:

            if p.pedido not in calculados_existencia:
                numero_pedidos_perseo_en_perseo = matperseo.objects.filter(
                    pedido=p.pedido).count()
                if numero_pedidos_perseo_en_perseo < 1:
                    faltante = NovedadPerseoVsFenix()
                    faltante.concatenacion = p.concatenacion
                    faltante.pedido = p.pedido
                    faltante.actividad = p.actividad
                    faltante.fecha = p.fecha
                    faltante.codigo = p.codigo
                    faltante.cantidad = '0'
                    faltante.observacion = "Pedido con cero registros en Perseo."
                    faltante.cantidad_fenix = '0'
                    faltante.diferencia = '0'
                    faltante.save()

                calculados_existencia.append(p.pedido)

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
            if not NovedadPerseoVsFenix.objects.filter(pedido=pedido_perseo.pedido).filter(observacion="Pedido con cero registros en Fénix.").exists():

                if pedido_perseo.codigo[:1] == "M" or pedido_perseo.codigo[:1] == "G":
                    pass
                else:
                    try:
                        cantidad_en_fenix = matfenix.objects.filter(
                            concatenacion=pedido_perseo.concatenacion).aggregate(Sum('cantidad'))
                        cantidad_en_perseo = matperseo.objects.filter(
                            concatenacion=pedido_perseo.concatenacion).aggregate(Sum('cantidad'))
                        # print(cantidad_en_fenix)
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
                            faltante.cantidad_fenix = '0'
                            faltante.diferencia = '0'
                            faltante.save()

                    except Exception as e:
                        pass

        ped = NovedadPerseoVsFenix.objects.filter(diferencia=0)
        ped.delete()

    calculo_numero_acta()

    # Llamar a la función para realizar la actualización
    actualizar_novedades()
    novedades = NovedadPerseoVsFenix.objects.all()
    return render(request, 'novedades_perseo_fenix.html', {'novedades': novedades})

def actualizar_novedades():
    # Obtener todas las concatenaciones en Matperseo
    concatenaciones_matperseo = matperseo.objects.values_list('concatenacion', flat=True)
    
    # Filtrar registros en Matfenix que no están en Matperseo
    registros_faltantes_matfenix = matfenix.objects.exclude(concatenacion__in=concatenaciones_matperseo)
    
     # Crear instancias de NovedadPerseoVsFenix a partir de los registros faltantes en Matfenix
    nuevas_novedades = [
        NovedadPerseoVsFenix(
            concatenacion=registro.concatenacion,
            pedido=registro.pedido,
            actividad=registro.actividad,
            fecha=registro.fecha,
            codigo=registro.codigo,
            cantidad=0,
            acta="0",  # Valor predeterminado
            observacion="Item en fenix y no en perseo",  # Valor predeterminado
            cantidad_fenix=registro.cantidad,  # Valor predeterminado
            diferencia=0  # Valor predeterminado
        )
        for registro in registros_faltantes_matfenix
    ]
    
    # Insertar las nuevas instancias de NovedadPerseoVsFenix en la base de datos
    NovedadPerseoVsFenix.objects.bulk_create(nuevas_novedades)


def registros_faltantes_en_perseo_y_estan_en_fenix():
    # Obtener todas las concatenaciones en Matperseo
    concatenaciones_matperseo = matperseo.objects.values_list(
        'concatenacion', flat=True)

    # Filtrar registros en Matfenix que no están en Matperseo
    registros_faltantes_matfenix = matfenix.objects.exclude(
        concatenacion__in=concatenaciones_matperseo)

    for faltantes_en_perseo in registros_faltantes_matfenix:
        faltante = NovedadPerseoVsFenix()
        faltante.concatenacion = faltantes_en_perseo.concatenacion
        faltante.pedido = faltantes_en_perseo.pedido
        faltante.actividad = faltantes_en_perseo.actividad
        faltante.fecha = faltantes_en_perseo.fecha
        faltante.codigo = faltantes_en_perseo.codigo
        faltante.cantidad = '0'
        faltante.observacion = "Item no registrado en Perseo y esta en Fénix."
        faltante.acta = '0'
        faltante.cantidad_fenix = float(
            faltantes_en_perseo.cantidad)
        faltante.diferencia = '0'
        faltante.save()


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
                faltante.diferencia = 0
                faltante.save()
        except:
            print("error en el acta")


def analisis_fecha_perseo(request):

    pedidos_perseo = matperseo.objects.all()

    pedidos_calculados = []
    for pedido_perseo in pedidos_perseo:

        if pedido_perseo.pedido in pedidos_calculados:
            pass

        else:
            pedidos_calculados.append(pedido_perseo.pedido)

            pedidos = matperseo.objects.filter(
                pedido=pedido_perseo.pedido).only('fecha')

            calculados_fecha = []
            for p in pedidos:
                if p.fecha[:10] in calculados_fecha:
                    pass
                else:
                    calculados_fecha.append(p.fecha[:10])

            if len(calculados_fecha) > 1:
                pedido_novedad = NovedadPerseoVsFenix()
                pedido_novedad.concatenacion = pedido_perseo.concatenacion
                pedido_novedad.pedido = pedido_perseo.pedido
                pedido_novedad.actividad = pedido_perseo.actividad
                pedido_novedad.fecha = pedido_perseo.fecha
                pedido_novedad.codigo = pedido_perseo.codigo
                pedido_novedad.observacion = "Pedido con mas de una fecha."
                pedido_novedad.acta = pedido_perseo.acta
                pedido_novedad.cantidad_fenix = '0'
                pedido_novedad.diferencia = '0'
                pedido_novedad.save()

    novedades = NovedadPerseoVsFenix.objects.all()
    return render(request, 'novedades_perseo_fenix.html', {'novedades': novedades})


def reiniciar_novedades_perseo_vs_fenix(request):
    NovedadPerseoVsFenix.objects.all().delete()
    return render(request, 'novedades_perseo_fenix.html', {'novedades': ['']})


def novedades_perseo_vs_fenix(request):
    novedades = NovedadPerseoVsFenix.objects.all()
    return render(request, 'novedades_perseo_fenix.html', {'novedades': novedades})
