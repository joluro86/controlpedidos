from django.shortcuts import render, get_object_or_404, redirect
from administrador.query.actividades.actividades import actividades_contrato
from .models import Actividad
from .forms import ActividadForm

def index(request):
    act_cont = actividades_contrato(request)
    return render(request, "admin.html", {'actividades_contrato':act_cont})

def editar_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_tu_vista_principal')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'editar_actividad.html', {'form': form})

