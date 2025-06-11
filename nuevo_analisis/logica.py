from django.shortcuts import redirect
from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad
from nuevo_analisis.models import RelacionItemRegla


def analisis_reglas(request):

    for regla in RelacionItemRegla.objects.all():
        
        tipo_objeto_regla = regla.objeto.tipo
        item_busqueda = regla.Item_busqueda
        print(f"objeto {regla.objeto.nombre}")
        #print(item_busqueda)
        
        if tipo_objeto_regla=="actividad":
            campo_busqueda ="actividad"
        if tipo_objeto_regla=="suministro":
            campo_busqueda ="suminis"
        if tipo_objeto_regla=="obra":
            campo_busqueda ="item_cont"
        
        filtro = {campo_busqueda: regla.objeto.nombre}
        pedidos_a_evaluar_regla = Acta.objects.filter(**filtro)
        
            
        if regla.factor=="unico":
            evaluacion_factor_unico(pedidos_a_evaluar_regla, regla.requiere_cantidad, regla.cantidad_condicion, regla.Item_busqueda, regla.comparador, regla.cantidad, campo_busqueda, regla.objeto.nombre)
        
        cont=0
        
        for ped in pedidos_a_evaluar_regla:
            
            cont+=1
        print(cont)
        
        
    return redirect('listado_relaciones')

def evaluacion_factor_unico(pedidos, requiere_cantidad, cantidad_requerida_condicion, item_busqueda, comparador, cantidad_comparar, campo_busqueda, objeto):
    cont=0
    for pedido in pedidos:
        
        filtro = {
            "pedido": pedido,
            campo_busqueda: item_busqueda
        }
        
        if not Acta.objects.filter(**filtro).exists():
            cont+=1
            print(pedido)
            print(campo_busqueda)
            print(item_busqueda)
            print(comparador)
            print(cantidad_comparar)
            print(f"contador {cont}")
            crear_novedad(pedido, f"{objeto} sin {item_busqueda}")
        elif requiere_cantidad:
            print("requiere")
        else: 
            print("no requiere")
        