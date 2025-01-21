from gestionvencimientos.models import Actividad, Actividad_epm

def dias_actividades_contrato(request):
    return Actividad.objects.all()

def dias_actividades_epm(request):
    return Actividad_epm.objects.all()

