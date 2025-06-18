# your_app_name/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages # Import the messages framework
from django.db.models import F # Useful for more complex ordering, though not strictly needed for basic __ notation

from .models import ItemRegla, RelacionIncompatibilidad, RelacionItemRegla, RelacionLimiteItem, RelacionUltimoCaracter
from nuevo_analisis.form import ItemReglaForm, RelacionIncompatibilidadForm, RelacionItemReglaForm, RelacionLimiteItemForm, RelacionUltimoCaracterForm

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
            saved_item = form.save()
            if pk:
                messages.success(request, f'Ítem "{saved_item.nombre}" actualizado exitosamente.')
            else:
                messages.success(request, f'Ítem "{saved_item.nombre}" creado exitosamente.')
            
            # Logic for "Guardar y Crear Otro" button
            if 'save_and_add_another' in request.POST:
                return redirect('crear_item_regla') # Redirect back to the empty create form
            else:
                return redirect('listado_todas_las_relaciones') # Default redirect
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ItemReglaForm(instance=item)

    context = {
        'form': form,
        'is_editing': pk is not None
    }
    return render(request, 'crear_item_regla.html', context)

def eliminar_item_regla(request, pk):
    """
    Vista para eliminar un ItemRegla.
    """
    item = get_object_or_404(ItemRegla, pk=pk)
    if request.method == 'POST': # Ensure it's a POST request for deletion (from SweetAlert2)
        item_nombre = item.nombre # Get name before deleting
        item.delete()
        messages.success(request, f'Ítem "{item_nombre}" eliminado exitosamente.')
    return redirect('listado_todas_las_relaciones')
    # The render for 'confirmar_eliminacion.html' here is usually for GET request confirmation pages.
    # With SweetAlert2, you often redirect directly after POST.

# --- Vistas para RelacionItemRegla ---

def lista_relacion_item_regla(request):
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
            saved_relacion = form.save()
            if pk:
                messages.success(request, f'Relación de Ítem "{saved_relacion}" actualizada exitosamente.')
            else:
                messages.success(request, f'Relación de Ítem "{saved_relacion}" creada exitosamente.')
            
            # Logic for "Guardar y Crear Otro" button (if added to this template)
            if 'save_and_add_another' in request.POST:
                return redirect('crear_relacion_item')
            else:
                return redirect('listado_todas_las_relaciones')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = RelacionItemReglaForm(instance=relacion)

    context = {
        'form': form,
        'is_editing': pk is not None
    }
    return render(request, 'crear_relacion_item.html', context)

def eliminar_relacion_item_regla(request, pk):
    if request.method == 'POST':
        relacion = get_object_or_404(RelacionItemRegla, pk=pk)
        relacion_str = str(relacion) # Get string representation before deleting
        relacion.delete()
        messages.success(request, f'Relación de Ítem "{relacion_str}" eliminada exitosamente.')
    return redirect('listado_todas_las_relaciones')

# --- Vistas para RelacionIncompatibilidad ---
def lista_relaciones_incompatibilidad(request):
    relaciones = RelacionIncompatibilidad.objects.all()
    return render(request, 'relaciones_incompatibilidad/lista.html', {'relaciones': relaciones})

def crear_relacion_incompatibilidad(request):
    if request.method == 'POST':
        form = RelacionIncompatibilidadForm(request.POST)
        if form.is_valid():
            saved_relacion = form.save()
            messages.success(request, f'Relación de incompatibilidad "{saved_relacion.objeto.nombre}" creada exitosamente.')
            
            # Logic for "Guardar y Crear Otro" button (if added to this template)
            if 'save_and_add_another' in request.POST:
                return redirect('crear_relacion_incompatibilidad')
            else:
                return redirect('listado_todas_las_relaciones')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = RelacionIncompatibilidadForm()
    return render(request, 'relaciones_incompatibilidad/formulario.html', {'form': form, 'titulo': 'Crear relación'})

def editar_relacion_incompatibilidad(request, pk):
    relacion = get_object_or_404(RelacionIncompatibilidad, pk=pk)
    if request.method == 'POST':
        form = RelacionIncompatibilidadForm(request.POST, instance=relacion)
        if form.is_valid():
            saved_relacion = form.save()
            messages.success(request, f'Relación de incompatibilidad "{saved_relacion.objeto.nombre}" actualizada exitosamente.')
            return redirect('listado_todas_las_relaciones')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = RelacionIncompatibilidadForm(instance=relacion)
    return render(request, 'relaciones_incompatibilidad/formulario.html', {'form': form, 'titulo': 'Editar relación'})

def eliminar_relacion_incompatibilidad(request, pk):
    relacion = get_object_or_404(RelacionIncompatibilidad, pk=pk)
    if request.method == 'POST':
        relacion_nombre = f"{relacion.objeto.nombre} incompatible con {relacion.item_incompatibilidad}"
        relacion.delete()
        messages.success(request, f'Relación de incompatibilidad "{relacion_nombre}" eliminada exitosamente.')
    return redirect('listado_todas_las_relaciones')

# --- Vistas para RelacionUltimoCaracter ---

def lista_relaciones_caracter(request):
    relaciones = RelacionUltimoCaracter.objects.all()
    return render(request, 'relacion_caracter/lista.html', {'relaciones': relaciones})

def crear_relacion_caracter(request):
    if request.method == 'POST':
        form = RelacionUltimoCaracterForm(request.POST)
        if form.is_valid():
            saved_relacion = form.save()
            messages.success(request, f'Regla de Carácter Final "{saved_relacion.objeto.nombre} {saved_relacion.caracter}" creada exitosamente.')
            
            # Logic for "Guardar y Crear Otro" button (if added to this template)
            if 'save_and_add_another' in request.POST:
                return redirect('crear_relacion_caracter')
            else:
                return redirect('listado_todas_las_relaciones')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = RelacionUltimoCaracterForm()
    return render(request, 'relacion_caracter/formulario.html', {'form': form})

def editar_relacion_caracter(request, pk):
    relacion = get_object_or_404(RelacionUltimoCaracter, pk=pk)
    if request.method == 'POST':
        form = RelacionUltimoCaracterForm(request.POST, instance=relacion)
        if form.is_valid():
            saved_relacion = form.save()
            messages.success(request, f'Regla de Carácter Final "{saved_relacion.objeto.nombre} {saved_relacion.caracter}" actualizada exitosamente.')
            return redirect('listado_todas_las_relaciones')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = RelacionUltimoCaracterForm(instance=relacion)
    return render(request, 'relacion_caracter/formulario.html', {'form': form})

def eliminar_relacion_caracter(request, pk):
    relacion = get_object_or_404(RelacionUltimoCaracter, pk=pk)
    if request.method == 'POST':
        relacion_nombre = f"{relacion.objeto.nombre} (Carácter: {relacion.caracter})"
        relacion.delete()
        messages.success(request, f'Regla de Carácter Final "{relacion_nombre}" eliminada exitosamente.')
    return redirect('listado_todas_las_relaciones')


# --- Vistas para RelacionLimiteItem ---

def lista_relaciones_cantidad(request):
    relaciones = RelacionLimiteItem.objects.all()
    return render(request, 'relacion_cantidad/relacion_limite_list.html', {'relaciones': relaciones})

def crear_relacion_cantidad(request):
    if request.method == 'POST':
        form = RelacionLimiteItemForm(request.POST)
        if form.is_valid():
            saved_relacion = form.save()
            items_display = saved_relacion.items if saved_relacion.items else 'un límite de cantidad'
            messages.success(request, f'Regla de Límite de Cantidad para "{items_display}" creada exitosamente.')
            
            # Logic for "Guardar y Crear Otro" button (if added to this template)
            if 'save_and_add_another' in request.POST:
                return redirect('crear_relacion_cantidad')
            else:
                return redirect('listado_todas_las_relaciones')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = RelacionLimiteItemForm()
    return render(request, 'relacion_cantidad/relacion_limite_form.html', {'form': form})

def editar_relacion_cantidad(request, pk):
    relacion = get_object_or_404(RelacionLimiteItem, pk=pk)
    if request.method == 'POST':
        form = RelacionLimiteItemForm(request.POST, instance=relacion)
        if form.is_valid():
            saved_relacion = form.save()
            items_display = saved_relacion.items if saved_relacion.items else 'un límite de cantidad'
            messages.success(request, f'Regla de Límite de Cantidad para "{items_display}" actualizada exitosamente.')
            return redirect('listado_todas_las_relaciones')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = RelacionLimiteItemForm(instance=relacion)
    return render(request, 'relacion_cantidad/relacion_limite_form.html', {'form': form, 'editar': True})

def eliminar_relacion_cantidad(request, pk):
    relacion = get_object_or_404(RelacionLimiteItem, pk=pk)
    if request.method == 'POST':
        items_display = relacion.items if relacion.items else 'este límite de cantidad'
        relacion.delete()
        messages.success(request, f'Regla de Límite de Cantidad para "{items_display}" eliminada exitosamente.')
    return redirect('listado_todas_las_relaciones')


# --- Vista General de Reglas ---
def listado_general_reglas(request):
    from .models import (
        ItemRegla,
        RelacionItemRegla,
        RelacionIncompatibilidad,
        RelacionUltimoCaracter,
        RelacionLimiteItem,
    )

    contexto = {
        'item_reglas': ItemRegla.objects.all().order_by('nombre'),
        'relaciones_item_regla': RelacionItemRegla.objects.all().order_by('objeto__nombre'),
        'relaciones_incompatibilidad': RelacionIncompatibilidad.objects.all().order_by('objeto__nombre'), # Added ordering by related object name
        'relaciones_caracter': RelacionUltimoCaracter.objects.all().order_by('objeto__nombre'), # Added ordering by related object name
        'relaciones_cantidad': RelacionLimiteItem.objects.all().order_by(F('items').asc(nulls_first=True)), # Order by items, with nulls first for clarity
    }
    return render(request, 'listado_general.html', contexto)