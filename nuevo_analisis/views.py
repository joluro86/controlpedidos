from django.shortcuts import render, redirect
from nuevo_analisis.form import RelacionItemReglaForm, ItemReglaForm

def crear_relacion_item(request):
    form = RelacionItemReglaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listado_relaciones')  # Ajusta esto al nombre de tu vista/listado

    return render(request, 'crear_relacion_item.html', {
        'form': form
    })

def crear_item_regla(request):
    form = ItemReglaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listado_items_regla')  # Asegúrate de tener esta vista/listado

    return render(request, 'crear_item_regla.html', {
        'form': form
    })

from django.shortcuts import render, get_object_or_404, redirect
from nuevo_analisis.models import ItemRegla

def listado_items_regla(request):
    items = ItemRegla.objects.all().order_by('nombre')
    return render(request, 'listado_items_regla.html', {'items': items})

def editar_item_regla(request, pk):
    item = get_object_or_404(ItemRegla, pk=pk)
    form = ItemReglaForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('listado_items_regla')

    return render(request, 'crear_item_regla.html', {'form': form})
def eliminar_item_regla(request, pk):
    item = get_object_or_404(ItemRegla, pk=pk)
    item.delete()
    return redirect('listado_items_regla')

from django.shortcuts import render
from .models import RelacionItemRegla

def listado_relaciones(request):
    relaciones = RelacionItemRegla.objects.select_related('item', 'item_requerido').all().order_by('item__tipo', 'item__nombre')
    
    return render(request, 'listado_relaciones.html', {
        'relaciones': relaciones
    })


# views.py
from django.shortcuts import get_object_or_404, render, redirect
from nuevo_analisis.models import RelacionItemRegla
from nuevo_analisis.form import RelacionItemReglaForm
from django.contrib import messages

def editar_regla(request, pk):
    regla = get_object_or_404(RelacionItemRegla, pk=pk)
    initial = {'item_requerido_nombre': regla.item_requerido.nombre}

    if request.method == 'POST':
        form = RelacionItemReglaForm(request.POST, instance=regla)
        if form.is_valid():
            form.save()
            messages.success(request, "Regla actualizada correctamente.")
            return redirect('listado_relaciones')  # Cambia esta ruta si es diferente
        else:
            messages.error(request, "Revisa los errores en el formulario.")
    else:
        form = RelacionItemReglaForm(instance=regla, initial=initial)

    return render(request, 'editar_regla.html', {
        'form': form,
        'regla': regla,
        'breadcrumb_items': [('Relaciones', 'Editar regla')],
    })
