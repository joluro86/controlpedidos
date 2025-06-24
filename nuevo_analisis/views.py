# your_app_name/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages # Import the messages framework
from django.db.models import F # Useful for more complex ordering, though not strictly needed for basic __ notation
from .models import ItemRegla, RelacionIncompatibilidad, RelacionItemRegla, RelacionLimiteItem, RelacionUltimoCaracter
from nuevo_analisis.form import ItemReglaForm, RelacionIncompatibilidadForm, RelacionItemReglaForm, RelacionLimiteItemForm, RelacionUltimoCaracterForm
from django.http import HttpResponse, Http404
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    ItemRegla, RelacionItemRegla, RelacionIncompatibilidad,
    RelacionUltimoCaracter, RelacionLimiteItem
)

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


def carga_masiva_item_regla(request):
    if request.method == 'POST':
        excel = request.FILES.get('archivo')
        if not excel:
            messages.error(request, 'Debe seleccionar un archivo.')
            return redirect('listado_todas_las_relaciones')

        try:
            df = pd.read_excel(excel)
            for _, row in df.iterrows():
                ItemRegla.objects.get_or_create(
                    nombre=row['nombre'],
                    tipo=row['tipo']
                )
            messages.success(request, 'Ítems de regla cargados correctamente.')
        except Exception as e:
            messages.error(request, f'Error al procesar el archivo: {e}')
        return redirect('listado_todas_las_relaciones')
    return render(request, 'carga_masiva.html', {'titulo': 'Carga Masiva - Ítems de Regla',  'modelo': 'item_regla'})

def carga_masiva_relacion_item(request):
    if request.method == 'POST':
        excel = request.FILES.get('archivo')
        if not excel:
            messages.error(request, 'Debe seleccionar un archivo.')
            return redirect('listado_todas_las_relaciones')

        try:
            df = pd.read_excel(excel)
            for _, row in df.iterrows():
                obj = ItemRegla.objects.get(nombre=row['objeto'])
                RelacionItemRegla.objects.create(
                    objeto=obj,
                    requiere_cantidad=row['requiere_cantidad'],
                    cantidad_condicion=row['cantidad_condicion'],
                    factor=row['factor'],
                    item_busqueda=row['item_busqueda'],
                    tipo_item_busqueda=row['tipo_item_busqueda'],
                    conjuncion=row['conjuncion'],
                    comparador=row['comparador'],
                    cantidad=row['cantidad'],
                    verificar_cantidad_items=row['verificar_cantidad_items']
                )
            messages.success(request, 'Relaciones de ítems cargadas correctamente.')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('listado_todas_las_relaciones')
    return render(request, 'carga_masiva.html', {'titulo': 'Carga Masiva - Relaciones Ítems',  'modelo': 'relacion_item'})

def carga_masiva_incompatibilidad(request):
    if request.method == 'POST':
        excel = request.FILES.get('archivo')
        if not excel:
            messages.error(request, 'Debe seleccionar un archivo.')
            return redirect('listado_todas_las_relaciones')

        try:
            df = pd.read_excel(excel)
            for _, row in df.iterrows():
                obj = ItemRegla.objects.get(nombre=row['objeto'])
                RelacionIncompatibilidad.objects.create(
                    objeto=obj,
                    item_incompatibilidad=row['item_incompatibilidad'],
                    tipo_item_incompatibilidad=row['tipo_item_incompatibilidad']
                )
            messages.success(request, 'Incompatibilidades cargadas correctamente.')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('listado_todas_las_relaciones')
    return render(request, 'carga_masiva.html', {'titulo': 'Carga Masiva - Incompatibilidades',  'modelo': 'incompatibilidad'})

def carga_masiva_caracter(request):
    if request.method == 'POST':
        excel = request.FILES.get('archivo')
        if not excel:
            messages.error(request, 'Debe seleccionar un archivo.')
            return redirect('listado_todas_las_relaciones')

        try:
            df = pd.read_excel(excel)
            for _, row in df.iterrows():
                obj = ItemRegla.objects.get(nombre=row['objeto'])
                RelacionUltimoCaracter.objects.create(
                    objeto=obj,
                    caracter=row['caracter'],
                    aplica=row['aplica'],
                    item_caracter=row.get('item_caracter'),
                    tipo_item=row['tipo_item'],
                    todos_los_registros=row['todos_los_registros']
                )
            messages.success(request, 'Reglas de carácter cargadas correctamente.')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('listado_todas_las_relaciones')
    return render(request, 'carga_masiva.html', {'titulo': 'Carga Masiva - Carácter Final',  'modelo': 'caracter'})

def carga_masiva_cantidad(request):
    if request.method == 'POST':
        excel = request.FILES.get('archivo')
        if not excel:
            messages.error(request, 'Debe seleccionar un archivo.')
            return redirect('listado_todas_las_relaciones')

        try:
            df = pd.read_excel(excel)
            for _, row in df.iterrows():
                RelacionLimiteItem.objects.create(
                    tipo_item=row['tipo_item'],
                    items=row.get('items'),
                    comparador=row['comparador'],
                    cantidad=row['cantidad']
                )
            messages.success(request, 'Reglas de cantidad cargadas correctamente.')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('listado_todas_las_relaciones')
    return render(request, 'carga_masiva.html', {'titulo': 'Carga Masiva - Límite de Cantidad', 'modelo': 'cantidad'})



def descargar_plantilla_modelo(request, modelo):
    # Diccionario con encabezados y ejemplos para cada modelo
    plantillas = {
        'relacion_item': {
            'columnas': [
                'objeto', 'requiere_cantidad', 'cantidad_condicion', 'factor',
                'item_busqueda', 'tipo_item_busqueda', 'conjuncion',
                'comparador', 'cantidad', 'verificar_cantidad_items'
            ],
            'ejemplo': [
                'ITEM-001', True, 2, 'unico',
                '200410,200411', 'suminis', 'todos',
                'mayor_a', 1, True
            ]
        },
        'incompatibilidad': {
            'columnas': ['objeto', 'item_incompatibilidad', 'tipo_item_incompatibilidad'],
            'ejemplo': ['ITEM-002', '200420,200421', 'actividad']
        },
        'caracter': {
            'columnas': ['objeto', 'caracter', 'aplica', 'item_caracter', 'tipo_item', 'todos_los_registros'],
            'ejemplo': ['ITEM-003', 'A', True, '200450', 'item_cont', False]
        },
        'cantidad': {
            'columnas': ['tipo_item', 'items', 'comparador', 'cantidad'],
            'ejemplo': ['suminis', '200460,200461', 'igual_a', 5]
        },
        'item_regla': {
            'columnas': ['nombre', 'tipo'],
            'ejemplo': ['ITEM-004', 'actividad']
        }
    }

    if modelo not in plantillas:
        raise Http404("Modelo no válido.")

    data = plantillas[modelo]
    df = pd.DataFrame(columns=data['columnas'])
    df.loc[0] = data['ejemplo']

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=plantilla_{modelo}.xlsx'
    df.to_excel(response, index=False)
    return response
