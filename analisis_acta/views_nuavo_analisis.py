from django.shortcuts import redirect, render
from django.contrib import messages
from analisis_acta.models import Acta, CantidadItem, Novedad_acta, VariableAnalisis
from analisis_acta.views import crear_novedad

def analisis_revision_acta_nuevo(request):
    variable_region = VariableAnalisis.objects.first()  # Obtener la primera variable
    
    if variable_region:
        Acta.objects.exclude(subz=variable_region.region).delete()
    else:
        messages.warning(request, "No existen Variables de contrato registradas.")
        return redirect("index_admin")
    
    # Obtener todos los ítems de CantidadItem
    items_cantidad = CantidadItem.objects.values_list('item', flat=True)

    # Filtrar las actas que tienen un item_cont que existe en items_cantidad
    actas_items = Acta.objects.filter(item_cont__in=items_cantidad)
    
    for acta in actas_items:
        cantidad_item = CantidadItem.objects.filter(item=acta.item_cont).first()
        if cantidad_item:
            mensaje_error = cantidad_item.verificar_cantidad(acta.pedido, cantidad_item.cantidad_cobro)
            if mensaje_error:
                # Registrar una novedad con el mensaje específico
                crear_novedad(acta, mensaje_error)
    
    # Recuperar las novedades para la vista
    novedades = Novedad_acta.objects.all()
    return render(request, "analisis.html", {'novedades': novedades})

