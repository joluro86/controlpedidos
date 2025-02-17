
from analisis_acta.models import CantidadItem
from analisis_acta.views import crear_novedad

def analisis_cantidades_items():
    
    lista_items = CantidadItem.objects.all()
    
    for item in lista_items:
        if item.verificar_cantidad:
            crear_novedad(item.item.pedido, "Cantidad cobro item no permitida")