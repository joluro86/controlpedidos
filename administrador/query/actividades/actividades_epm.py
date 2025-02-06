from django.shortcuts import get_object_or_404
from gestionvencimientos.models import Actividad, Actividad_epm, Encargado

def crear_nueva_actividad_epm(request):
            actividad = Actividad_epm()
            actividad.nombre = request.POST.get('nombre', actividad.nombre)
            actividad.dias_urbano = request.POST.get('dias_urbano', actividad.dias_urbano)
            actividad.dias_rural = request.POST.get('dias_rural', actividad.dias_rural)            
            actividad.save()

def actualizar_actividad_epm(request, actividad_id):
            actividad = actividad_por_id_epm(actividad_id)
            actividad.nombre = request.POST.get('nombre', actividad.nombre)
            actividad.dias_urbano = request.POST.get('dias_urbano', actividad.dias_urbano)
            actividad.dias_rural = request.POST.get('dias_rural', actividad.dias_rural)          
            actividad.save() 

def eliminar_actividad_epm(id):
    actividad = get_object_or_404(Actividad_epm, id=id)
    actividad.delete()

def actividades_epm(request):
    return Actividad_epm.objects.all()

def actividad_por_id_epm(id):
       return Actividad_epm.objects.get(id=id)


def actividades_epm(request):
    return Actividad_epm.objects.all()

