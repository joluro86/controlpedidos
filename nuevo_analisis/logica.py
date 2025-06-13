from django.shortcuts import redirect
from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad
from nuevo_analisis.models import RelacionItemRegla


def analisis_reglas(request):

    for regla in RelacionItemRegla.objects.all():
        
        tipo_objeto_regla = regla.objeto.tipo
        
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
              
        filtro = crear_filtro_busqueda(regla, pedido,  campo_busqueda, regla.Item_busqueda, regla.cantidad)    
           
        if not Acta.objects.filter(**filtro).exists() and not regla.requiere_cantidad:
            
            if regla.comparador=="igual_a":
                novedad= f"{regla.objeto.nombre} {regla.Item_busqueda} cobro diferente de {regla.cantidad}"
            
            if regla.comparador=="mayor_a":
                novedad= f"{regla.objeto.nombre} {regla.Item_busqueda} menor igual a {regla.cantidad}"
                
            if regla.comparador=="menor_a":
                novedad= f"{regla.objeto.nombre} {regla.Item_busqueda} mayor igual a {regla.cantidad}"
                    
            pedi = Acta.objects.filter(pedido=pedido.get('pedido')).first()
            crear_novedad(pedi, novedad)
        
        if regla.requiere_cantidad:
             
            if regla.objeto.tipo=="actividad":
                campo_busqueda ="actividad"
            if regla.objeto.tipo=="suministro":
                campo_busqueda ="suminis"
            if regla.objeto.tipo=="obra":
                campo_busqueda ="item_cont" 
                          
            filtro2 = crear_filtro_busqueda(regla, pedido, campo_busqueda, regla.objeto.nombre, regla.cantidad_condicion)

            if Acta.objects.filter(**filtro2).exists():
                pedi = Acta.objects.filter(pedido=pedido.get('pedido')).first()
                cont+=1
                print(regla.comparador)
                print(cont)
                print("requiere")
                print(f"ped: {pedi}: {regla.cantidad_condicion} de {regla.objeto.nombre}" )
                
                if tipo_item_busqueda=="actividad":
                    campo_busqueda ="actividad"
                if tipo_item_busqueda=="suministro":
                    campo_busqueda ="suminis"
                if tipo_item_busqueda=="obra":
                    campo_busqueda ="item_cont"
                    
                filtro3 = crear_filtro_busqueda(regla, pedido,  campo_busqueda, regla.Item_busqueda, regla.cantidad)
                
                if not Acta.objects.filter(**filtro3).exists():
                    
                    if regla.comparador=="igual_a":
                        novedad= f"{regla.objeto.nombre} {regla.Item_busqueda} cobro diferente de {regla.cantidad}"
                    
                    if regla.comparador=="mayor_a":
                        novedad= f"{regla.objeto.nombre} {regla.Item_busqueda} menor igual a {regla.cantidad}"
                        
                    if regla.comparador=="menor_a":
                        novedad= f"{regla.objeto.nombre} {regla.Item_busqueda} mayor igual a {regla.cantidad}"
                            
                    pedi = Acta.objects.filter(pedido=pedido.get('pedido')).first()
                    crear_novedad(pedi, novedad)
        #else:  
         #   print("no requiere")

def crear_filtro_busqueda(regla, pedido, campo_busqueda, item_busqueda, cantidad):
    
        if regla.comparador=="igual_a":
            filtro = {
                "pedido": pedido.get('pedido'),
                campo_busqueda: item_busqueda,
                'cantidad': cantidad
            }            
            
        if regla.comparador=="mayor_a":
            
            filtro = {
                "pedido": pedido.get('pedido'),
                campo_busqueda: item_busqueda,
                "cantidad__gt": cantidad
            }
            
        if regla.comparador=="menor_a":
            
            filtro = {
                "pedido": pedido.get('pedido'),
                campo_busqueda: item_busqueda,
                "cantidad__lt": cantidad  
            }
            
        return filtro
 