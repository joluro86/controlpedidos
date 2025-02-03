from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from administrador.query.actividades.actividades_contrato import actualizar_actividad,actividades_contrato, encargados, crear_nueva_actividad, eliminar_actividad, actividades_epm, materiales
from administrador.query.actividades.actividades_legalizacion import actividades_legalizacion
from gestionvencimientos.models import Actividad, Encargado
from administrador.query.actividades.variables_contrato import variables_contrato

@login_required
def index(request):
    
    context = {
        'actividades_contrato': actividades_contrato(request),
        'actividades_epm': actividades_epm(request),
        'encargados': encargados(request),
        'materiales_permitidos': materiales(request), 
        'variables_contrato': variables_contrato(request),
        'actividades_legalizacion': actividades_legalizacion(request),
    }
    
    return render(request, "admin.html", context)

@login_required
def actividades_view(request): 
    context = {
    'encargados':encargados(request),
    'actividades_contrato': actividades_contrato(request),
    }
    return render(request, 'administrador/actividades_list.html', context)

@login_required
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

@login_required
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

@login_required
def eliminar_actividad_por_id(request,id):
    eliminar_actividad(id)
    return redirect('index_admin')
