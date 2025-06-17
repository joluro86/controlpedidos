from django.db.models import Count
from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad

def verificar_registros_duplicadas():
    # Buscar combinaciones de pedido + item_cont que se repiten más de una vez
    duplicados = (
        Acta.objects
        .values('pedido', 'item_cont')
        .annotate(veces=Count('id'))
        .filter(veces__gt=1)
    )
    
    novedades_creadas = set()

    for dup in duplicados:
        pedido_id = dup['pedido']
        item = dup['item_cont']
        clave = f"{pedido_id}-{item}"

        if clave not in novedades_creadas:
            acta = Acta.objects.filter(pedido=pedido_id, item_cont=item).first()
            if acta:
                mensaje = f"{item} Línea duplicada"
                crear_novedad(acta, mensaje)
                novedades_creadas.add(clave)
