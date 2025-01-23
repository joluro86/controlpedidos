from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from administrador.query.actividades.actividades import actividades_contrato
from administrador.templates.forms.forms_actividad import ActividadForm
from gestionvencimientos.models import Actividad, Encargado


def index(request):
    act_cont = actividades_contrato(request)
    encargados = Encargado.objects.all()
    print("hola")
    print(encargados)
    return render(request, "admin.html", {'actividades_contrato':act_cont, 'encargados':encargados})

def actividades_view(request):
    actividades = Actividad.objects.all()
    encargados = Encargado.objects.all()
    print("hola")
    print(encargados)
    return render(request, 'administrador/actividades_list.html', {
        'actividades_contrato': actividades, 'encargados': encargados,
    })

def editar_actividad(request, actividad_id):
    if request.method == 'POST':
        try:
            actividad = Actividad.objects.get(id=actividad_id)
            actividad.nombre = request.POST.get('nombre', actividad.nombre)
            actividad.dias_urbano = request.POST.get('dias_urbano', actividad.dias_urbano)
            actividad.dias_rural = request.POST.get('dias_rural', actividad.dias_rural)
            
            # Asignar el encargado que viene en el formulario
            actividad.encargado = Encargado.objects.get(id=request.POST.get('encargado'))
            
            actividad.save()
            return JsonResponse({'success': True})
        except Actividad.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Actividad no encontrada'})
        except Encargado.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Encargado no encontrado'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})
