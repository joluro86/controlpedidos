from perseovsfenix.models import Guia
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

def guia_interna_list(request):
    return Guia.objects.all().order_by('nombre_perseo')

def existencia_equivalencia(nombre_per, nombre_fen):
    return Guia.objects.filter(nombre_perseo=nombre_per, nombre_fenix=nombre_fen).exists()

def actualizar_guia_id(request, id):
    
    if existencia_equivalencia(request.POST.get('nombre_perseo'), request.POST.get('nombre_fenix')):
        return False
    else:
        guia = Guia.objects.get(id=id)
        guia.nombre_perseo = request.POST.get('nombre_perseo', guia.nombre_perseo)
        guia.nombre_fenix = request.POST.get('nombre_fenix', guia.nombre_fenix)           
        guia.save() 
        return True

def eliminar_guia_id(id):    
    equivalencia = get_object_or_404(Guia, id=id)
    equivalencia.delete()
        