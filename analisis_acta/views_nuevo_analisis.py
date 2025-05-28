from django.shortcuts import redirect, render
from django.contrib import messages
from analisis_acta.models import Acta, CantidadItem, Novedad_acta, VariableAnalisis
from analisis_acta.views import crear_novedad
import pandas as pd

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


def subir_cantidad_items(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']

        try:
            df = pd.read_excel(file)  # Leer el archivo Excel
            
            # Validar que las columnas requeridas estén en el archivo
            columnas_requeridas = {'item', 'cantidad_cobro', 'tipo_restriccion', 'max_cantidad'}
            if not columnas_requeridas.issubset(df.columns):
                messages.error(request, "El archivo debe contener las columnas: item, cantidad_cobro, tipo_restriccion, max_cantidad")
                return redirect('subir_cantidad_items')

            # Recorrer cada fila y guardar los datos en la base de datos
            for _, row in df.iterrows():
                CantidadItem.objects.create(
                    item=row['item'],
                    cantidad_cobro=row['cantidad_cobro'],
                    tipo_restriccion=row.get('tipo_restriccion', 'EXACTO'),
                    max_cantidad=row.get('max_cantidad', None)
                )

            messages.success(request, "Datos cargados exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al procesar el archivo: {str(e)}")

    return render(request, 'subir_cantidad_items.html')

def eliminar_cantidad_items(request, id):
    item = CantidadItem.objects.filter(id=id)
    if item.exists():
        item.delete()
        messages.success(request, "El ítem ha sido eliminado correctamente.")
    else:
        messages.warning(request, "El ítem no existe o ya ha sido eliminado.")
    
    return redirect('index_admin')


    
    
