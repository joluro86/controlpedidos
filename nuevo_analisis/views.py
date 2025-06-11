# your_app_name/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy # Para redirigir con un nombre de URL, útil en clases pero también aplicable aquí
from .models import ItemRegla, RelacionItemRegla
from nuevo_analisis.form import ItemReglaForm, RelacionItemReglaForm # Asegúrate de que estos formularios estén definidos

# --- Vistas para ItemRegla ---

def lista_item_regla(request):
    """
    Vista para listar todos los ItemRegla.
    """
    items = ItemRegla.objects.all()
    return render(request, 'listado_items_regla.html', {'items': items})

def crear_editar_item_regla(request, pk=None):
    """
    Vista para crear un nuevo ItemRegla o editar uno existente.
    """
    item = None
    if pk: # Si se proporciona una PK, estamos editando
        item = get_object_or_404(ItemRegla, pk=pk)

    if request.method == 'POST':
        form = ItemReglaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # Redirigir a la lista de ítems o a una página de éxito
            return redirect('listado_items_regla') # Asume que tienes una URL llamada 'lista_item_regla'
    else:
        form = ItemReglaForm(instance=item) # Crea el formulario vacío o precargado

    context = {
        'form': form,
        'is_editing': pk is not None # Pasa una bandera para que el template sepa si es edición
    }
    return render(request, 'crear_relacion_item.html', context)

def eliminar_item_regla(request, pk):
    """
    Vista para eliminar un ItemRegla.
    """
    item = get_object_or_404(ItemRegla, pk=pk)
    item.delete()
    return redirect('listado_items_regla')
    
# --- Vistas para RelacionItemRegla ---

def lista_relacion_item_regla(request):
    """
    Vista para listar todas las RelacionItemRegla.
    """
    relaciones = RelacionItemRegla.objects.all()
    
    return render(request, 'listado_relaciones.html', {'relaciones': relaciones})


def crear_editar_relacion_item_regla(request, pk=None):
    """
    Vista para crear una nueva RelacionItemRegla o editar una existente.
    """
    relacion = None
    if pk:
        relacion = get_object_or_404(RelacionItemRegla, pk=pk)

    if request.method == 'POST':
        form = RelacionItemReglaForm(request.POST, instance=relacion)
        if form.is_valid():
            form.save()
            # Redirigir a la lista de relaciones o a una página de éxito
            return redirect('listado_relaciones') # Asume que tienes una URL llamada 'lista_relacion_item_regla'
    else:
        form = RelacionItemReglaForm(instance=relacion)

    context = {
        'form': form,
        'is_editing': pk is not None
    }
    return render(request, 'crear_relacion_item.html', context)

def eliminar_relacion_item_regla(request, pk):
    """
    Vista para eliminar una RelacionItemRegla.
    """
    relacion = get_object_or_404(RelacionItemRegla, pk=pk)
    relacion.delete()
    return redirect('listado_relaciones')
    
