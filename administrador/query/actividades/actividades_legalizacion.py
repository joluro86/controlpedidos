from analisis_acta.models import ActividadLegalizacion
from django.db.models import Q
from django.shortcuts import get_object_or_404


def actividades_legalizacion(request):
    return ActividadLegalizacion.objects.all().order_by('nombre')

def crear_nueva_actividad_legalizacion(request):
    nombre_actividad = request.POST.get('nombre', '')
    
    # Verificamos si ya existe un registro con la misma región o contrato
    if ActividadLegalizacion.objects.filter(Q(nombre=nombre_actividad)).exists():
        # Si ya existe, no guardamos nada y podemos retornar None o un mensaje.
        return False

    # Si no existe, creamos y guardamos la nueva variable.
    nueva_actividad = ActividadLegalizacion(nombre=nombre_actividad)
    nueva_actividad.save()
    
    return True

def actividad_por_id(id):
    return ActividadLegalizacion.objects.get(id=id)
    
def actualizar_legalizacion(request, actividad_id):
            actividad = actividad_por_id(actividad_id)
            actividad.nombre = request.POST.get('nombre', actividad.nombre)         
            actividad.save() 

def eliminar_actividad_legalizacion(id):
    actividad_lega = get_object_or_404(ActividadLegalizacion, id=id)
    actividad_lega.delete()


