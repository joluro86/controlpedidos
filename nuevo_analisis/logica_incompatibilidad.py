from django.shortcuts import redirect

from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad
from nuevo_analisis.crear_texto_novedades import crear_texto_novedad
from nuevo_analisis.models import RelacionIncompatibilidad

def analisis_reglas_incompatibilidad():

    reglas = RelacionIncompatibilidad.objects.all()

    if reglas.exists():
        for regla in reglas:
            campo_busqueda=regla.objeto.tipo
            filtro = {campo_busqueda: regla.objeto.nombre}
            
            pedidos_a_evaluar_regla = Acta.objects.filter(**filtro).values('pedido').distinct()
            
            analizar_cumplimiento_regla(pedidos_a_evaluar_regla, regla)

    return redirect('novedades_acta')

"""
    
    

def analizar_cumplimiento_regla(pedidos_a_evaluar, regla):

    for pedido in pedidos_a_evaluar:
        campo_busqueda=regla.tipo_item_incompatibilidad
        filtro = {'pedido': pedido.get('pedido'), campo_busqueda: regla.item_incompatibilidad}
            
        busqueda = Acta.objects.filter(**filtro)

        if busqueda.exists():    
            novedad= f"{regla.objeto.nombre} incompatible con {regla.item_incompatibilidad}"        
            pedi = Acta.objects.filter(pedido=pedido.get('pedido')).first()
            crear_novedad(pedi, novedad)
"""

def analizar_cumplimiento_regla(pedidos_a_evaluar, regla):
    campo_busqueda = regla.tipo_item_incompatibilidad
    items_incompatibles = regla.item_incompatibilidad.split(',') if regla.item_incompatibilidad else []

    for pedido in pedidos_a_evaluar:
        pedido_id = pedido.get('pedido')

        for item in items_incompatibles:
            item = item.strip()
            filtro = {'pedido': pedido_id, campo_busqueda: item}

            busqueda = Acta.objects.filter(**filtro)

            if busqueda.exists():
                texto_novedad = f"{regla.objeto.nombre} incompatible con '{item}' en {campo_busqueda}"
                acta_referencia = busqueda.first()
                crear_novedad(acta_referencia, texto_novedad)
                break  # si ya hay una incompatibilidad, no se necesita revisar más

