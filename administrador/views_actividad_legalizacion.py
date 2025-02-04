from django.shortcuts import redirect, render
from administrador.query.actividades.actividades_legalizacion import crear_nueva_actividad_legalizacion
from django.contrib import messages


def crear_actividad_legalizacion(request):
    if request.method == 'POST':
        if crear_nueva_actividad_legalizacion(request):
            messages.error(
                request,
                "Actividad creada con exito."
            )
            return redirect('nueva_actividad_legalizacion_form')
        else:
            messages.error(
                request,
                "Actividad ya existe, ingrese otra."
            )
            return redirect('nueva_actividad_legalizacion_form')            

    return render(request, "nueva_actividad_legalizacion.html")
