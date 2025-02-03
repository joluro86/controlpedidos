from analisis_acta.models import VariableAnalisis
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def variables_contrato(request):
    return VariableAnalisis.objects.all()


def crear_variable_contrato(data):
    region = data.get('region', '')
    contrato = data.get('contrato', '')
    
    # Verificamos si ya existe un registro con la misma región o contrato
    if VariableAnalisis.objects.filter(Q(region=region) | Q(contrato=contrato)).exists():
        # Si ya existe, no guardamos nada y podemos retornar None o un mensaje.
        return None

    # Si no existe, creamos y guardamos la nueva variable.
    nueva_variable = VariableAnalisis(region=region, contrato=contrato)
    nueva_variable.save()
    
def actualizar_variable(request, variable_id):
    if request.method == "POST":
        variable = get_object_or_404(VariableAnalisis, id=variable_id)    

        # Actualizar solo si la variable no existe en otro registro
        variable.region = request.POST.get('region', variable.region)
        variable.contrato = request.POST.get('contrato', variable.contrato)
        variable.save()
        return JsonResponse({'success': True, 'message': 'Variables actualizadas correctamente.'})

    return JsonResponse({'success': False, 'error': 'Método no permitido'})


