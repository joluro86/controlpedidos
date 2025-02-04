from analisis_acta.models import ActividadLegalizacion
from django.db.models import Q
from django.shortcuts import render, redirect


def actividades_legalizacion(request):
    return ActividadLegalizacion.objects.all()

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


