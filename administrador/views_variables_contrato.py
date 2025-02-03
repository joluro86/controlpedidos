# views.py
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from analisis_acta.models import VariableAnalisis
from .forms import VariableContratoForm
from administrador.query.actividades.variables_contrato import actualizar_variable, crear_variable_contrato


def agregar_variable_contrato(request):
    # Si ya existen registros en VariableAnalisis:
    if VariableAnalisis.objects.exists():
        messages.error(
            request,
            "Ya hay registros de variables de contrato, puede actualizarlas si desea."
        )
        return redirect('index_admin')
    else:
        if request.method == 'POST':
            form = VariableContratoForm(request.POST)
            if form.is_valid():
                crear_variable_contrato(form.cleaned_data)
            return redirect('index_admin')
        else:
            form = VariableContratoForm()
            return render(request, "nueva_variable_contrato.html", {'form': form})

def editar_variable(request, variable_id):
    if request.method == 'POST':
        try:
            actualizar_variable(request, variable_id)
            return JsonResponse({'success': True})
        except VariableAnalisis.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Variable no encontrada'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})