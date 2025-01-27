
from django.http import JsonResponse
from django.shortcuts import render, redirect

from administrador.query.actividades.actividades_contrato import encargados, crear_nuevo_encargado, actualizar_encargado, eliminar_encargado_query
from gestionvencimientos.models import Encargado

def nuevo_encargado(request):
    if request.method == 'POST':
        try:
            crear_nuevo_encargado(request)
            return redirect('index_admin')
        except:
            return JsonResponse({'success': False, 'error': 'Encargado no guardado'})
    return render(request, "nuevo_encargado.html", {'encargados':encargados(request)})

def editar_encargado(request, encargado_id):
    if request.method == 'POST':
        try:
            actualizar_encargado(request, encargado_id)
            return JsonResponse({'success': True})
        except Encargado.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Encargado no encontrado'})
        
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def eliminar_encargado(request,id):
    eliminar_encargado_query(id)
    return redirect('index_admin')