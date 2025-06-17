from django.shortcuts import redirect
from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad
from nuevo_analisis.models import RelacionUltimoCaracter

def analisis_reglas_caracter():

    reglas = RelacionUltimoCaracter.objects.all()

    if reglas.exists():
        for regla in reglas:
            campo_busqueda=regla.objeto.tipo
            filtro = {campo_busqueda: regla.objeto.nombre}
            
            pedidos_a_evaluar_regla = Acta.objects.filter(**filtro).values('pedido').distinct()
            
            if regla.todos_los_registros==True and regla.aplica==True:
                analizar_cumplimiento_caracter_todos(pedidos_a_evaluar_regla, regla)
            
            if regla.todos_los_registros==False and regla.aplica==True:
                analizar_cumplimiento_caracter_un_item(pedidos_a_evaluar_regla, regla)
                
            if regla.todos_los_registros==True and regla.aplica==False:
                analizar_cumplimiento_caracter_todos_no_aplica(pedidos_a_evaluar_regla, regla)
            
            if regla.todos_los_registros==False and regla.aplica==False:
                analizar_cumplimiento_caracter_no_aplica_un_item(pedidos_a_evaluar_regla, regla)
                           

    return redirect('novedades_acta')


def analizar_cumplimiento_caracter_todos(pedidos_a_evaluar, regla):
    
      
    for pedido in pedidos_a_evaluar:
        campo_busqueda = regla.tipo_item
        valor_caracter = regla.caracter
        pedido_id = pedido.get('pedido')

        registros = Acta.objects.filter(pedido=pedido_id)

        for registro in registros:
            valor = str(getattr(registro, campo_busqueda, '')).strip()

            # Saltar si está vacío, es None, "0" o "00"
            if not valor or valor in ['0', '00']:
                continue

            # Validar si no termina con el valor esperado
            if not valor.lower().endswith(valor_caracter.lower()):
                novedad = f"{regla.objeto.nombre} - El campo '{campo_busqueda}' no termina con '{valor_caracter}'"
                crear_novedad(registro, novedad)
                break

def analizar_cumplimiento_caracter_un_item(pedidos_a_evaluar, regla):
    for ped in pedidos_a_evaluar:
        campo_busqueda = regla.tipo_item
        inicio_caracter = regla.item_caracter
        fin_caracter = regla.caracter
        pedido_id = ped.get('pedido')

        # Filtrar registros cuyo campo comience con 'inicio_caracter'
        filtro = {
            'pedido': pedido_id,
            f"{campo_busqueda}__istartswith": inicio_caracter
        }

        registros = Acta.objects.filter(**filtro)
        
        for registro in registros:
            valor = str(getattr(registro, campo_busqueda, '')).strip()
            
            # Saltar si el valor es vacío, "0" o "00"
            if not valor or valor in ['0', '00']:
                continue

            # Verificar si no termina con lo requerido
            if not valor.lower().endswith(fin_caracter.lower()):
                novedad = f"{regla.objeto.nombre} - {inicio_caracter} sin '{fin_caracter}'"
                crear_novedad(registro, novedad)
                break  # Ya con uno que falle, no seguimos con este pedido


def analizar_cumplimiento_caracter_todos_no_aplica(pedidos_a_evaluar, regla):
    
      
    for pedido in pedidos_a_evaluar:
        campo_busqueda = regla.tipo_item
        valor_caracter = regla.caracter
        pedido_id = pedido.get('pedido')

        registros = Acta.objects.filter(pedido=pedido_id)

        for registro in registros:
            valor = str(getattr(registro, campo_busqueda, '')).strip()

            # Saltar si está vacío, es None, "0" o "00"
            if not valor or valor in ['0', '00']:
                continue

            # Validar si no termina con el valor esperado
            if valor.lower().endswith(valor_caracter.lower()):
                novedad = f"{regla.objeto.nombre} - El campo '{campo_busqueda}' termina con '{valor_caracter}'"
                crear_novedad(registro, novedad)
                break
            

def analizar_cumplimiento_caracter_no_aplica_un_item(pedidos_a_evaluar, regla):
    for ped in pedidos_a_evaluar:
        campo_busqueda = regla.tipo_item
        inicio_caracter = regla.item_caracter
        fin_caracter = regla.caracter
        pedido_id = ped.get('pedido')

        # Filtrar registros cuyo campo comience con 'inicio_caracter'
        filtro = {
            'pedido': pedido_id,
            f"{campo_busqueda}__istartswith": inicio_caracter
        }

        registros = Acta.objects.filter(**filtro)
        
        for registro in registros:
            valor = str(getattr(registro, campo_busqueda, '')).strip()
            
            # Saltar si el valor es vacío, "0" o "00"
            if not valor or valor in ['0', '00']:
                continue

            # Verificar si no termina con lo requerido
            if valor.lower().endswith(fin_caracter.lower()):
                novedad = f"{regla.objeto.nombre} - {inicio_caracter} con '{fin_caracter}'"
                crear_novedad(registro, novedad)
                break  # Ya con uno que falle, no seguimos con este pedido
