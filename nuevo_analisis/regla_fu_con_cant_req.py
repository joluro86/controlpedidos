from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad
from nuevo_analisis.crear_texto_novedades import crear_texto_novedad
from nuevo_analisis.models import RelacionItemRegla


def busqueda_pedidos_factor_unico_con_cantidad_requerida():
    try:
        reglas= RelacionItemRegla.objects.filter(requiere_cantidad=True, factor="unico")
        
        if reglas.exists():           
            for regla in reglas:    
                print("cantidad condicion:")  
                print(regla.cantidad_condicion)          
                campo_busqueda=regla.objeto.tipo
                filtro = {campo_busqueda: regla.objeto.nombre, 'cantidad':regla.cantidad_condicion}
                pedidos_a_evaluar_regla = Acta.objects.filter(**filtro).values('pedido').distinct()
                print(pedidos_a_evaluar_regla)
                evaluar_pedidos_regla_factor_unico_con_cantidad_requerida(regla, pedidos_a_evaluar_regla)
        
    except Exception as e:
        print(e)
        
def evaluar_pedidos_regla_factor_unico_con_cantidad_requerida(regla, pedidos_a_evaluar):

    for pedido in pedidos_a_evaluar:

        campo_busqueda=regla.tipo_item_busqueda
        crear_novedad_bandera = verificar_cumplimiento_regla_con_cantidad_requerida(pedido.get('pedido'),campo_busqueda, regla.item_busqueda, regla.cantidad, regla.comparador, regla.tipo_item_busqueda)
       
        if crear_novedad_bandera==True:
            novedad= crear_texto_novedad(regla)        
            pedi = Acta.objects.filter(pedido=pedido.get('pedido')).first()
            crear_novedad(pedi, novedad)

def verificar_cumplimiento_regla_con_cantidad_requerida(pedido,campo_busqueda,  item_busqueda, cantidad, comparador, tipo_item_busqueda):
    
    if tipo_item_busqueda=="actividad":
        filtro = {'pedido':pedido, campo_busqueda:item_busqueda}
        if not Acta.objects.filter(**filtro).exists():
                return True

    if comparador=="igual_a":
        filtro = {'pedido':pedido, campo_busqueda:item_busqueda, 'cantidad':cantidad}
        if not Acta.objects.filter(**filtro).exists():
                print("entre")
                return True
        
    if comparador=="mayor_a":
        
        filtro = {'pedido':pedido, campo_busqueda:item_busqueda, 'cantidad__gt':cantidad}
        if not Acta.objects.filter(**filtro).exists():
                print("entre")
                return True
        
    if comparador=="menor_a":     

        filtro = {'pedido':pedido, campo_busqueda:item_busqueda, 'cantidad__lt':cantidad}
        if not Acta.objects.filter(**filtro).exists():
            print("entre")
            return True
  