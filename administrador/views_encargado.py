
from django.http import JsonResponse
from django.shortcuts import render

def nuevo_encargado(request):
    if request.method == 'POST':
        try:
            crear_nuevo_encargado(request)
            return redirect('index_admin')
        except:
            return JsonResponse({'success': False, 'error': 'Encargado no encontrado'})
    return render(request, "nueva_actividad.html", {'encargados':encargados(request)})


"""

def encargados_view(request): 
    return render(request, 'administrador/actividades_list.html', {
        'actividades_contrato': actividades_contrato(request), 'encargados': encargados(request),
    })



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
"""