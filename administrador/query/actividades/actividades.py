from gestionvencimientos.models import Actividad, Actividad_epm

def actividades_contrato(request):
    return Actividad.objects.all()

def actividades_epm(request):
    return Actividad_epm.objects.all()

