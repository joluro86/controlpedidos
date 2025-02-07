from django.shortcuts import get_object_or_404
from analisis_acta.models import Materiales
from gestionvencimientos.models import Actividad, Actividad_epm, Encargado
from django.http import JsonResponse

def crear_nueva_actividad(request):
    if request.method == "POST":
        nombre_nueva_actividad = request.POST.get('nombre')

        # Validar si la actividad ya existe
        if verificar_actividad_existente(nombre_nueva_actividad):
            return JsonResponse({'success': False, 'error': 'La actividad ya existe en la base de datos.'})

        # Crear nueva actividad
        actividad = Actividad(
            nombre=nombre_nueva_actividad,
            dias_urbano=request.POST.get('dias_urbano', 0),
            dias_rural=request.POST.get('dias_rural', 0),
            encargado=get_object_or_404(Encargado, id=request.POST.get('encargado'))
        )
        actividad.save()
        return JsonResponse({'success': True})

def actualizar_actividad(request, actividad_id):
    if request.method == "POST":
        actividad = get_object_or_404(Actividad, id=actividad_id)

        # No permitir cambiar el nombre
        if 'nombre' in request.POST and request.POST.get('nombre') != actividad.nombre:
            return JsonResponse({'success': False, 'error': 'No está permitido cambiar el nombre de la actividad.'})

        # Actualizar solo los campos permitidos
        actividad.dias_urbano = request.POST.get('dias_urbano', actividad.dias_urbano)
        actividad.dias_rural = request.POST.get('dias_rural', actividad.dias_rural)

        # Verificar si el encargado existe antes de asignarlo
        encargado_id = request.POST.get('encargado')
        if encargado_id:
            actividad.encargado = get_object_or_404(Encargado, id=encargado_id)
        
        actividad.save()
        return JsonResponse({'success': True})


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
    return Materiales.objects.all().order_by("material")


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


def eliminar_material(id):
    material = get_object_or_404(Materiales, id=id)
    material.delete()


def actualizar_material(request, material_id):
    if request.method == "POST":
        material = get_object_or_404(Materiales, id=material_id)

        nuevo_nombre = request.POST.get('material', material.material)

        # Verificar si el nuevo nombre ya existe en otro registro
        if verificar_material_existente(nuevo_nombre):
            return JsonResponse({'success': False, 'error': 'El material ya existe en la base de datos.'})

        # Actualizar solo si el nombre no existe en otro registro
        material.material = nuevo_nombre
        material.save()
        return JsonResponse({'success': True, 'message': 'Material actualizado correctamente.'})

    return JsonResponse({'success': False, 'error': 'Método no permitido'})


def verificar_material_existente(nombre):
    """
    Verifica si ya existe un material con el mismo nombre en la base de datos.
    Retorna True si existe, False si no.
    """
    return Materiales.objects.filter(material=nombre).exists()


def verificar_actividad_existente(nombre_actividad):
    """
    Verifica si ya existe la actividad con el mismo nombre en la base de datos.
    Retorna True si existe, False si no.
    """
    return Actividad.objects.filter(nombre=nombre_actividad).exists()
