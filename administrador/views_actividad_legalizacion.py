from django.shortcuts import redirect, render
from administrador.query.actividades.actividades_legalizacion import crear_nueva_actividad_legalizacion, actualizar_legalizacion, eliminar_actividad_legalizacion
from django.contrib import messages
from django.http import JsonResponse
from analisis_acta.models import ActividadLegalizacion


def crear_actividad_legalizacion(request):
    if request.method == 'POST':
        if crear_nueva_actividad_legalizacion(request):
            messages.error(
                request,
                "Actividad creada con exito."
            )
            return redirect('nueva_actividad_legalizacion_form')
        else:
            messages.error(
                request,
                "Actividad ya existe, ingrese otra."
            )
            return redirect('nueva_actividad_legalizacion_form')

    return render(request, "nueva_actividad_legalizacion.html")

def editar_actividad_legalizacion(request, actividad_id):
    if request.method == 'POST':
        try:
            actualizar_legalizacion(request, actividad_id)
            return JsonResponse({'success': True})
        except ActividadLegalizacion.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Actividad no encontrada'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def eliminar_actividad_legalizacion_id(request,id):
    eliminar_actividad_legalizacion(id)
    return redirect('index_admin')