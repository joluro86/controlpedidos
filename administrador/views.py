from django.shortcuts import redirect, render
from django.http import JsonResponse
from administrador.query.actividades.actividades_contrato import actualizar_actividad,actividades_contrato, encargados, crear_nueva_actividad, eliminar_actividad, actividades_epm, materiales
from gestionvencimientos.models import Actividad, Encargado

def index(request):
    
    context = {
        'actividades_contrato': actividades_contrato(request),
        'actividades_epm': actividades_epm(request),
        'encargados': encargados(request),
        'materiales_permitidos': materiales(request), 
    }
    
    return render(request, "admin.html", context)

def actividades_view(request): 
    context = {
    'encargados':encargados(request),
    'actividades_contrato': actividades_contrato(request),
    }
    return render(request, 'administrador/actividades_list.html', context)

def nueva_actividad(request):
    if request.method == 'POST':
        try:
            crear_nueva_actividad(request)
            return redirect('index_admin')
        except Encargado.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Encargado no encontrado'})
    context = {
    'encargados':encargados(request),
     }
    return render(request, "nueva_actividad.html", context)


def editar_actividad(request, actividad_id):
    if request.method == 'POST':
        try:
            actualizar_actividad(request, actividad_id)
            return JsonResponse({'success': True})
        except Actividad.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Actividad no encontrada'})
        except Encargado.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Encargado no encontrado'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def eliminar_actividad_por_id(request,id):
    eliminar_actividad(id)
    return redirect('index_admin')
