
from django.http import JsonResponse
from django.shortcuts import render, redirect
from administrador.query.actividades.actividades_contrato import encargados, crear_nuevo_encargado, actualizar_encargado, eliminar_encargado_query
from gestionvencimientos.models import Encargado


def nuevo_encargado(request):
    if request.method == 'POST':
        response = crear_nuevo_encargado(request)
        return response
    context = {
        'encargados': encargados(request),
    }
    return render(request, "nuevo_encargado.html", context)


def editar_encargado(request, encargado_id):
    if request.method == 'POST':
        try:
            return actualizar_encargado(request, encargado_id)
        except Encargado.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Encargado no encontrado'})


def eliminar_encargado(request, id):
    eliminar_encargado_query(id)
    return redirect('index_admin')
