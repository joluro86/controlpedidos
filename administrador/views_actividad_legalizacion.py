from django.shortcuts import redirect, render
from administrador.query.actividades.actividades_legalizacion import crear_nueva_actividad_legalizacion, actualizar_legalizacion, eliminar_actividad_legalizacion
from django.contrib import messages
from django.http import JsonResponse
from analisis_acta.models import ActividadLegalizacion


def crear_actividad_legalizacion(request):
    
    if request.method == 'POST':
        response = crear_nueva_actividad_legalizacion(request)
        return response
    
    return render(request, "nueva_actividad_legalizacion.html")

def editar_actividad_legalizacion(request, actividad_id):
    if request.method == 'POST':
        try:
            actualizar_legalizacion(request, actividad_id)
        except ActividadLegalizacion.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Actividad no encontrada'})

def eliminar_actividad_legalizacion_id(request,id):
    eliminar_actividad_legalizacion(id)
    return redirect('index_admin')