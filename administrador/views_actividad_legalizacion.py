from django.shortcuts import redirect, render
from administrador.query.actividades.actividades_legalizacion import crear_nueva_actividad_legalizacion

def crear_actividad_legalizacion(request):
    if request.method == 'POST':
        try:
            crear_nueva_actividad_legalizacion(request)
            return redirect('index_admin')
        except Exception as e:
            return e

    return render(request, "nueva_actividad_legalizacion.html")
