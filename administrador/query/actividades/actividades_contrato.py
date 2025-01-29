from django.shortcuts import get_object_or_404
from analisis_acta.models import Materiales
from gestionvencimientos.models import Actividad, Actividad_epm, Encargado
from django.contrib import messages

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
    return Actividad.objects.all().order_by('nombre')

def actividad_por_id(id):
       return Actividad.objects.get(id=id)

def encargados(request):
    return Encargado.objects.all().order_by('nombre')

def crear_nuevo_encargado(request):
    if request.method == "POST":
        print("enca")
        
        # Obtener el valor de 'nombre' del formulario
        nombre = request.POST.get('nombre', None)

        if nombre:  # Verificar si se recibió un nombre válido
            encargado = Encargado()  # Crear una nueva instancia del modelo
            encargado.nombre = nombre  # Asignar el valor al atributo del modelo
            
            encargado.save()  # Guardar en la base de datos
            print(f"Encargado '{encargado.nombre}' guardado exitosamente.")
        else:
            print("Error: No se proporcionó un nombre válido.")
    else:
        print("Error: La solicitud no es de tipo POST.")

def actividades_epm(request):
    return Actividad_epm.objects.all().order_by('nombre')

def encargado_por_id(id):
       return Encargado.objects.get(id=id)

def actualizar_encargado(request, encargado_id):
    if request.method == "POST":
        encargado = get_object_or_404(Encargado, id=encargado_id)
        
        # Obtener el nombre del POST, si no se envía se mantiene el valor actual
        encargado.nombre = request.POST.get('nombre', encargado.nombre)
        
        encargado.save()
        print(f"Encargado con ID {encargado_id} actualizado correctamente.")

def eliminar_encargado_query(id):
    encargado = get_object_or_404(Encargado, id=id)
    encargado.delete()
    
    
def materiales(request):
    return Materiales.objects.all()

from django.http import JsonResponse

def crear_nuevo_material(request):
    if request.method == 'POST':
        mat = request.POST.get('material', None)

        if not mat:
            return JsonResponse({'success': False, 'message': "Error: No se proporcionó un nombre válido."})

        if Materiales.objects.filter(material=mat).exists():
            return JsonResponse({'success': False, 'message': f"El material '{mat}' ya existe."})

        try:
            material = Materiales(material=mat)
            material.save()
            return JsonResponse({'success': True, 'message': f"Material '{mat}' guardado exitosamente."})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f"Error al guardar: {str(e)}"})

    return JsonResponse({'success': False, 'message': "Método no permitido."})