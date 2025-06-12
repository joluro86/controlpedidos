from django.shortcuts import redirect
from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad
from nuevo_analisis.models import RelacionItemRegla


def analisis_reglas(request):

    for regla in RelacionItemRegla.objects.all():
        
        tipo_objeto_regla = regla.objeto.tipo
        item_busqueda = regla.Item_busqueda
        print(f"tipo objeto {tipo_objeto_regla} debe lleva {item_busqueda}")
        
        
        if tipo_objeto_regla=="actividad":
            campo_busqueda ="actividad"
        if tipo_objeto_regla=="suministro":
            campo_busqueda ="suminis"
        if tipo_objeto_regla=="obra":
            campo_busqueda ="item_cont"
        
        filtro = {campo_busqueda: regla.objeto.nombre}
        pedidos_a_evaluar_regla = Acta.objects.filter(**filtro).values('pedido').distinct()
        
            
        if regla.factor=="unico":
            evaluacion_factor_unico(pedidos_a_evaluar_regla, regla)
        
        cont=0        
        
    return redirect('listado_relaciones')

def evaluacion_factor_unico(pedidos, regla):
    cont=0
    
    tipo_item_busqueda = regla.tipo_item_busqueda
    
    if tipo_item_busqueda=="actividad":
        campo_busqueda ="actividad"
    if tipo_item_busqueda=="suministro":
        campo_busqueda ="suminis"
    if tipo_item_busqueda=="obra":
        campo_busqueda ="item_cont"

    for pedido in pedidos:
        print(f"buscar: {regla.Item_busqueda} cant: {regla.cantidad}")
        
    """
        filtro = {
            "pedido": pedido,
            campo_busqueda: tipo_item_busqueda
        }
        
        if not Acta.objects.filter(**filtro).exists():
            cont+=1
            if pedido.actividad=="ALECA":
                print(pedido)
                print(campo_busqueda)
                print(item_busqueda)
        #        crear_novedad(pedido, f"{objeto} sin {item_busqueda}")
        #elif requiere_cantidad:
         #   print("requiere")
        #else: 
         #   print("no requiere")
    """