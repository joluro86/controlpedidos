from django.db.models import Q
from decimal import Decimal
from perseovsfenix.models import NovedadPerseoVsFenix, matfenix, matperseo


from decimal import Decimal

def obtener_diferencias_entre_items_pvf(request):
    # Obtener los valores únicos de 'concatenacion' en ambos modelos
    concatenaciones_perseo = set(matperseo.objects.values_list('concatenacion', flat=True))
    concatenaciones_fenix = set(matfenix.objects.values_list('concatenacion', flat=True))
    
    # Encontrar los valores que están en uno pero no en el otro
    en_perseo_no_fenix = concatenaciones_perseo - concatenaciones_fenix
    en_fenix_no_perseo = concatenaciones_fenix - concatenaciones_perseo
    
    # Validación de pedidos antes de procesar
    pedidos_perseo = set(matperseo.objects.values_list('pedido', flat=True))
    pedidos_fenix = set(matfenix.objects.values_list('pedido', flat=True))
    
    # Pedidos que están en ambos modelos
    pedidos_comunes = pedidos_perseo & pedidos_fenix
    
    # Filtrar los registros de Perseo y Fenix por los pedidos comunes
    registros_perseo = matperseo.objects.filter(concatenacion__in=en_perseo_no_fenix, pedido__in=pedidos_comunes)
    registros_fenix = matfenix.objects.filter(concatenacion__in=en_fenix_no_perseo, pedido__in=pedidos_comunes)

    # Crear novedades para los registros en Perseo pero no en Fenix
    for registro in registros_perseo:
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
                observacion="Existe en Perseo pero no en Fenix",
                cantidad_fenix=Decimal(0),
                diferencia=Decimal(registro.cantidad)
            )
    
    # Crear novedades para los registros en Fenix pero no en Perseo
    for registro in registros_fenix:
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
                observacion="Existe en Fenix pero no en Perseo",
                cantidad_fenix=Decimal(registro.cantidad),
                diferencia=Decimal(-registro.cantidad)
            )
    
    # Si un pedido no está presente en uno de los modelos, crear la novedad correspondiente
    pedidos_no_en_fenix = pedidos_perseo - pedidos_fenix
    for pedido in pedidos_no_en_fenix:
        NovedadPerseoVsFenix.objects.create(
            concatenacion="N/A",  # No hay concatenación asociada
            pedido=pedido,
            actividad="N/A",  # No hay actividad asociada
            fecha="N/A",  # No hay fecha asociada
            codigo="N/A",  # No hay código asociado
            cantidad=Decimal(0),
            acta="N/A",  # No hay acta asociada
            observacion="Pedido existe en Perseo pero no en Fenix",
            cantidad_fenix=Decimal(0),
            diferencia=Decimal(0)
        )

    pedidos_no_en_perseo = pedidos_fenix - pedidos_perseo
    for pedido in pedidos_no_en_perseo:
        NovedadPerseoVsFenix.objects.create(
            concatenacion="N/A",  # No hay concatenación asociada
            pedido=pedido,
            actividad="N/A",  # No hay actividad asociada
            fecha="N/A",  # No hay fecha asociada
            codigo="N/A",  # No hay código asociado
            cantidad=Decimal(0),
            acta="N/A",  # No hay acta asociada
            observacion="Pedido existe en Fenix pero no en Perseo",
            cantidad_fenix=Decimal(0),
            diferencia=Decimal(0)
        )
