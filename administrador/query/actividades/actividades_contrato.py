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
    return Actividad_epm.objects.all()

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