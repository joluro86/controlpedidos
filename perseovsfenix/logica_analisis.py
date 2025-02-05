from decimal import Decimal
from perseovsfenix.models import NovedadPerseoVsFenix, matfenix, matperseo
from django.db.models import Sum

from decimal import Decimal


def obtener_diferencias_entre_items_pvf(request):
    # Obtener los valores únicos de 'concatenacion' en ambos modelos
    concatenaciones_perseo = set(
        matperseo.objects.values_list('concatenacion', flat=True))
    concatenaciones_fenix = set(
        matfenix.objects.values_list('concatenacion', flat=True))

    # Encontrar los valores que están en uno pero no en el otro
    en_perseo_no_fenix = concatenaciones_perseo - concatenaciones_fenix
    en_fenix_no_perseo = concatenaciones_fenix - concatenaciones_perseo

    # Obtener todos los registros de cada modelo
    registros_perseo = list(matperseo.objects.all())
    registros_fenix = list(matfenix.objects.all())

    # Obtener los valores únicos de 'pedido' en ambos modelos
    pedidos_perseo = {registro.pedido for registro in registros_perseo}
    pedidos_fenix = {registro.pedido for registro in registros_fenix}

    # Variable almacenar pedido cero registros
    pedidos_con_novedad = set()
    # Pedidos que no están en Fenix
    pedidos_no_en_fenix = pedidos_perseo - pedidos_fenix
    for pedido in pedidos_no_en_fenix:
        # Buscar un registro representativo en Perseo para extraer sus datos
        registro_base = next(
            (r for r in registros_perseo if r.pedido == pedido), None)
        if registro_base:
            NovedadPerseoVsFenix.objects.create(
                concatenacion="N/A",
                pedido=registro_base.pedido,
                actividad=registro_base.actividad,
                fecha="N/A",
                codigo=registro_base.codigo,
                cantidad=Decimal(0),
                acta="N/A",
                observacion="Pedido cero registros en Fenix",
                cantidad_fenix=Decimal(0),
                diferencia=Decimal(0)
            )
            pedidos_con_novedad.add(pedido)

    # Pedidos que no están en Perseo
    pedidos_no_en_perseo = pedidos_fenix - pedidos_perseo
    for pedido in pedidos_no_en_perseo:
        # Buscar un registro representativo en Fenix para extraer sus datos
        registro_base = next(
            (r for r in registros_fenix if r.pedido == pedido), None)
        if registro_base:
            NovedadPerseoVsFenix.objects.create(
                concatenacion="N/A",
                pedido=registro_base.pedido,
                actividad=registro_base.actividad,
                fecha="N/A",
                codigo=registro_base.codigo,
                cantidad=Decimal(0),  # No hay cantidad en Perseo
                acta="N/A",
                observacion="Pedido cero registros en Perseo",
                cantidad_fenix=Decimal(0),
                diferencia=Decimal(0)
            )
            pedidos_con_novedad.add(pedido)

    # Filtrar los registros de Perseo y Fenix por los pedidos comunes
    registros_perseo = matperseo.objects.filter(
        concatenacion__in=en_perseo_no_fenix)
    registros_fenix = matfenix.objects.filter(
        concatenacion__in=en_fenix_no_perseo)

    # Crear novedades para los registros en Perseo pero no en Fenix
    for registro in registros_perseo:
        
        # Evita crear novedad si ya tiene cero registros
        if registro.pedido in pedidos_con_novedad:
            continue
        
        if registro.codigo[0] != "2" and registro.codigo[0] != "B":
            continue
        else:
            NovedadPerseoVsFenix.objects.create(
                concatenacion=registro.concatenacion,
                pedido=registro.pedido,
                actividad=registro.actividad,
                fecha=registro.fecha,
                codigo=registro.codigo,
                cantidad=Decimal(registro.cantidad),
                acta=registro.acta,
                observacion="Item en Perseo pero no en Fenix",
                cantidad_fenix=Decimal(0),
                diferencia=Decimal(registro.cantidad)
            )

    # Crear novedades para los registros en Fenix pero no en Perseo
    for registro in registros_fenix:
        
        # Evita crear novedad si ya tiene cero registros
        if registro.pedido in pedidos_con_novedad:
            continue
        
        if registro.codigo[0] != "2" and registro.codigo[0] != "B":
            continue
        else:
            NovedadPerseoVsFenix.objects.create(
                concatenacion=registro.concatenacion,
                pedido=registro.pedido,
                actividad=registro.actividad,
                fecha=registro.fecha,
                codigo=registro.codigo,
                cantidad=Decimal(0),
                acta="0",
                observacion="Item en Fenix pero no en Perseo",
                cantidad_fenix=Decimal(registro.cantidad),
                diferencia=Decimal(-registro.cantidad)
            )


def comparar_cantidades_concatenacion():
    # Obtener las concatenaciones comunes en ambos modelos
    concatenaciones_perseo = set(matperseo.objects.values_list('concatenacion', flat=True))
    concatenaciones_fenix = set(matfenix.objects.values_list('concatenacion', flat=True))
    concatenaciones_comunes = concatenaciones_perseo & concatenaciones_fenix  # Intersección
    
    print(len(concatenaciones_comunes))
    for concatenacion in concatenaciones_comunes:
        # Sumar cantidades en cada modelo
        suma_perseo = matperseo.objects.filter(concatenacion=concatenacion).aggregate(Sum('cantidad'))['cantidad__sum'] or Decimal(0)
        suma_fenix = matfenix.objects.filter(concatenacion=concatenacion).aggregate(Sum('cantidad'))['cantidad__sum'] or Decimal(0)
        print("aqui")
        print(concatenacion)
        print(suma_fenix)
        print(suma_perseo)
        # Obtener un registro representativo de cada modelo
        registro_perseo = matperseo.objects.filter(concatenacion=concatenacion).first()
        registro_fenix = matfenix.objects.filter(concatenacion=concatenacion).first()

        # Si las cantidades no coinciden, crear una novedad con los datos del primer registro encontrado
        if suma_perseo != suma_fenix:
            NovedadPerseoVsFenix.objects.create(
                concatenacion=concatenacion,
                pedido=registro_perseo.pedido if registro_perseo else registro_fenix.pedido,
                actividad=registro_perseo.actividad if registro_perseo else registro_fenix.actividad,
                fecha=registro_perseo.fecha if registro_perseo else registro_fenix.fecha,
                codigo=registro_perseo.codigo if registro_perseo else registro_fenix.codigo,
                cantidad=suma_perseo,
                acta=registro_perseo.acta if registro_perseo else registro_fenix.acta,
                observacion="Diferencia en cantidad entre Perseo y Fenix",
                cantidad_fenix=suma_fenix,
                diferencia=suma_fenix - suma_perseo
            )
