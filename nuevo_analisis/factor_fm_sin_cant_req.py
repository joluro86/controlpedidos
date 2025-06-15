

from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad
from nuevo_analisis.crear_texto_novedades import crear_texto_novedad
from nuevo_analisis.models import RelacionItemRegla


def busqueda_pedidos_factor_multiple_sin_cantidad_requerida():
    
    try:
        reglas= RelacionItemRegla.objects.filter(requiere_cantidad=False, factor="multiple")
        
        if reglas.exists():           
            for regla in reglas:              
                campo_busqueda=regla.objeto.tipo
                filtro = {campo_busqueda: regla.objeto.nombre, 'cantidad':regla.cantidad_condicion}
                pedidos_a_evaluar_regla = Acta.objects.filter(**filtro).values('pedido').distinct()
                print(len(pedidos_a_evaluar_regla))
                evaluar_pedidos_regla_factor_multiple_sin_cantidad_requerida(regla, pedidos_a_evaluar_regla, 0)
        
    except Exception as e:
        print(e)

def evaluar_pedidos_regla_factor_multiple_sin_cantidad_requerida(regla, pedidos_a_evaluar, cantidad_requeridad):
    texto = regla.item_busqueda
    elementos = texto.split(',')

    cont=0   
    for pedido in pedidos_a_evaluar:
        resultado = evaluar_item_por_separado(pedido, elementos, regla.tipo_item_busqueda)
        if regla.conjuncion=="todos":
            if any(not item['item_res'] for item in resultado):
                cont+=1
                print(cont)
                novedad= crear_texto_novedad(regla) 
                print(novedad)       
                pedi = Acta.objects.filter(pedido=pedido.get('pedido')).first()
                crear_novedad(pedi, novedad)
        if regla.conjuncion=="uno":
            if all(not item['item_res'] for item in resultado):
                cont += 1
                print(cont)
                novedad = crear_texto_novedad(regla)
                print(novedad)
                pedi = Acta.objects.filter(pedido=pedido.get('pedido')).first()
                crear_novedad(pedi, novedad)


def evaluar_item_por_separado(pedido, elementos, campo_busqueda):
    cont=0
    resultado = []
    
    for item in elementos:
        filtro = {'pedido':pedido.get('pedido'), campo_busqueda:item}
                       
        resultado.append(
            {
                'id':cont,
               'item_res': Acta.objects.filter(**filtro).exists()
            }
            )

    return resultado


    
   
            
