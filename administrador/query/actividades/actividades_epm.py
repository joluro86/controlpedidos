from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from gestionvencimientos.models import Actividad, Actividad_epm, Encargado

def crear_nueva_actividad_epm(request):
    if request.method == "POST":
        nombre_nueva_actividad_epm = request.POST.get('nombre')

        # Validar si la actividad ya existe
        if verificar_existancia_actividad_epm(nombre_nueva_actividad_epm):
            return JsonResponse({'success': False, 'error': 'La actividad ya existe en la base de datos.'})

        # Crear nueva actividad
        actividad = Actividad_epm(
            nombre=nombre_nueva_actividad_epm,
            dias_urbano=request.POST.get('dias_urbano', 0),
            dias_rural=request.POST.get('dias_rural', 0),
        )
        actividad.save()
        return JsonResponse({'success': True})


def actualizar_actividad_epm(request, actividad_id):
        if request.method == "POST":
            actividad_epm = get_object_or_404(Actividad_epm, id=actividad_id)

            # No permitir cambiar el nombre
            if 'nombre' in request.POST and request.POST.get('nombre') != actividad_epm.nombre:
                return JsonResponse({'success': False, 'error': 'No está permitido cambiar el nombre de la actividad.'})

            # Actualizar solo los campos permitidos
            actividad_epm.dias_urbano = request.POST.get('dias_urbano', actividad_epm.dias_urbano)
            actividad_epm.dias_rural = request.POST.get('dias_rural', actividad_epm.dias_rural)
          
            actividad_epm.save()
            
            return JsonResponse({'success': True})

def eliminar_actividad_epm(id):
    actividad = get_object_or_404(Actividad_epm, id=id)
    actividad.delete()

def actividades_epm(request):
    return Actividad_epm.objects.all()

def actividad_por_id_epm(id):
       return Actividad_epm.objects.get(id=id)


def actividades_epm(request):
    return Actividad_epm.objects.all()

def verificar_existancia_actividad_epm(nuevo_nombre):
    print(nuevo_nombre)
    return Actividad_epm.objects.filter(nombre=nuevo_nombre).exists()