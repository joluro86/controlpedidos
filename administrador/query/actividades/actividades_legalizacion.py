from django.http import JsonResponse
from analisis_acta.models import ActividadLegalizacion
from django.db.models import Q
from django.shortcuts import get_object_or_404

from gestionvencimientos.models import Actividad_epm


def actividades_legalizacion(request):
    return ActividadLegalizacion.objects.all().order_by('nombre')

def crear_nueva_actividad_legalizacion(request):
    nombre_actividad = request.POST.get('nombre')
    
    if verificar_nombre_legalizacion(nombre_actividad):
        return JsonResponse({'success': False, 'error': 'Actividad ya existe en la base de datos.'})
    actividad = ActividadLegalizacion(
            nombre=nombre_actividad,
        )
    actividad.save()
    return JsonResponse({'success': True})

def actividad_por_id(id):
    return ActividadLegalizacion.objects.get(id=id)
    
def actualizar_legalizacion(request, actividad_id):
    
    if request.method == "POST":
        actividad = get_object_or_404(ActividadLegalizacion, id=actividad_id)
    
        nombre_actividad = request.POST.get('nombre')

        if verificar_nombre_legalizacion(nombre_actividad):
            return JsonResponse({'success': False, 'error': 'Actividad ya existe en la base de datos.'})
        
        actividad.nombre = request.POST.get('nombre', actividad.nombre)         
        actividad.save() 
    
        return JsonResponse({'success': True})

def eliminar_actividad_legalizacion(id):
    actividad_lega = get_object_or_404(ActividadLegalizacion, id=id)
    actividad_lega.delete()

def verificar_nombre_legalizacion(nombre):
    print(ActividadLegalizacion.objects.filter(nombre=nombre).exists())
    return ActividadLegalizacion.objects.filter(nombre=nombre).exists()
