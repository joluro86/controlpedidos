from django.shortcuts import redirect, render
from django.http import JsonResponse
from administrador.query.actividades.actividades_epm import actualizar_actividad_epm, crear_nueva_actividad_epm, eliminar_actividad_epm
from gestionvencimientos.models import Actividad_epm

def nueva_actividad_epm(request):
    if request.method == 'POST':
        response = crear_nueva_actividad_epm(request)
        return response
    return render(request, "nueva_actividad_epm.html")


def editar_actividad_epm(request, actividad_id):
    if request.method == 'POST':
        try:
            actualizar_actividad_epm(request, actividad_id)
            return JsonResponse({'success': True})
        except Actividad_epm.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Actividad no encontrada'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def eliminar_actividad_por_id_epm(request,id):
    eliminar_actividad_epm(id)
    return redirect('index_admin')
