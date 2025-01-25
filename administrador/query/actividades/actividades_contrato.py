from django.shortcuts import get_object_or_404
from gestionvencimientos.models import Actividad, Actividad_epm, Encargado

def crear_nueva_actividad(request):
            actividad = Actividad()
            actividad.nombre = request.POST.get('nombre', actividad.nombre)
            actividad.dias_urbano = request.POST.get('dias_urbano', actividad.dias_urbano)
            actividad.dias_rural = request.POST.get('dias_rural', actividad.dias_rural)
            actividad.encargado = Encargado.objects.get(id=request.POST.get('encargado'))
            
            actividad.save()

def actualizar_actividad(request, actividad_id):
            actividad = actividad_por_id(actividad_id)
            actividad.nombre = request.POST.get('nombre', actividad.nombre)
            actividad.dias_urbano = request.POST.get('dias_urbano', actividad.dias_urbano)
            actividad.dias_rural = request.POST.get('dias_rural', actividad.dias_rural)
            
            # Asignar el encargado que viene en el formulario
            actividad.encargado = Encargado.objects.get(id=request.POST.get('encargado'))            
            actividad.save() 

def eliminar_actividad(id):
    actividad = get_object_or_404(Actividad, id=id)
    actividad.delete()

def actividades_contrato(request):
    return Actividad.objects.all()

def actividad_por_id(id):
       return Actividad.objects.get(id=id)

def encargados(request):
    return Encargado.objects.all()

def crear_nuevo_encargado(request):
            encargado= Encargado()
            encargado= request.POST.get('nombre', encargado.nombre)
            encargado.save()

def actividades_epm(request):
    return Actividad_epm.objects.all()

