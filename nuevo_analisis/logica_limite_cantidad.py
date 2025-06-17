from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad
from nuevo_analisis.models import RelacionLimiteItem

def analisis_reglas_limite_cantidad():

    reglas = RelacionLimiteItem.objects.all()

    if reglas.exists():
        for regla in reglas:
            analizar_cumplimiento_cantidades(regla)            


def analizar_cumplimiento_cantidades(regla):
    campo_busqueda = regla.tipo_item
    items = regla.items.split(',') if regla.items else []
    
    for item in items:
        item = item.strip()
        filtro_item = {campo_busqueda: item}
        
        pedidos = Acta.objects.filter(**filtro_item).values('pedido').distinct()

        for pedido_dict in pedidos:
            pedido_id = pedido_dict['pedido']
            registros = Acta.objects.filter(pedido=pedido_id, **filtro_item)
            suma = sum(r.cantidad for r in registros if r.cantidad is not None)

            # Comparación según regla.comparador
            cumple = (
                (regla.comparador == 'igual_a' and suma == regla.cantidad) or
                (regla.comparador == 'mayor_a' and suma > regla.cantidad) or
                (regla.comparador == 'menor_a' and suma < regla.cantidad)
            )

            if not cumple:
                texto_novedad = (
                    f"Item '{item}' - '{campo_busqueda}' "
                    f"cantidad {suma}"
                )
                crear_novedad(registros.first(), texto_novedad)

            
            

        