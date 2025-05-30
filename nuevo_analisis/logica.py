from django.db.models import Q, Sum
from django.shortcuts import render, redirect
from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad
from nuevo_analisis.models import RelacionItemRegla
from django.db.models import Sum
from decimal import Decimal
from django.db.models import Q


def total_item_requerido(registros, codigo_requerido, tipo_requerido): 

    if tipo_requerido == "suministro":
        total = sum(r.cantidad for r in registros
                    if r.suminis and r.suminis.rstrip('AP').strip() == codigo_requerido
                    )
    if tipo_requerido == "actividad":

        primer_registro = next(iter(registros), None)

        if primer_registro:
            pedido = primer_registro.pedido

            existe = Acta.objects.filter(actividad=codigo_requerido, pedido=pedido).exists()
            total = 1 if existe else 0
            
    if tipo_requerido == "obra":
        total = sum(r.cantidad for r in registros
                    if r.item_cont and r.item_cont.rstrip('AP').strip() == codigo_requerido
                     )
        
    print("item")
    print(codigo_requerido)
    print(tipo_requerido)
    print("total")
    print(total)

    return total


def cantidad_item_total(pedido, codigo_base, tipo_requerido):
    """
    Retorna la suma de cantidad para un item_cont con posibles sufijos A o P.
    """

    codigo_base = codigo_base.strip()
    
    if tipo_requerido == "suministro":
        total = Acta.objects.filter(
            Q(pedido=pedido) &
            (Q(suminis=codigo_base) |
             Q(suminis=codigo_base + 'A') |
                Q(suminis=codigo_base + 'P'))
        ).aggregate(suma=Sum('cantidad'))['suma'] or 0

    else:
        total = Acta.objects.filter(
            Q(pedido=pedido) &
            (Q(item_cont=codigo_base) |
             Q(item_cont=codigo_base + 'A') |
                Q(item_cont=codigo_base + 'P'))
        ).aggregate(suma=Sum('cantidad'))['suma'] or 0
       
    return total


def validar_reglas(request):

    reglas = RelacionItemRegla.objects.all()
    for reg in reglas:
        cantidad_regla = reg.cantidad
        codigo_requerido = reg.item_requerido.nombre.strip()
        tipo_requerido = reg.tipo_requerido

        if reg.factor == "unico":
            if reg.item.tipo == "actividad":

                pedidos = Acta.objects.filter(actividad=reg.item.nombre).values_list(
                    'pedido', flat=True).distinct()

                for p in pedidos:

                    registros = Acta.objects.filter(pedido=p)
                    total = total_item_requerido(
                        registros, codigo_requerido, tipo_requerido)

                    if reg.comparador == "igual_a":  # OK LOGICA
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total != cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "mayor_igual_a":  # OK LOGICA
                                                      
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total == 0 or total < cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "mayor_que":  # OK LOGICA                      
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total == 0 or total < cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "menor_igual_a": #OK LOGICA
                        
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total > cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "menor_que":  #OK LOGICA                        
    
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total >= cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "diferente_de":  
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)
                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total == cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

            if reg.item.tipo == "suministro":
                base_codigo = reg.item.nombre.strip()

                pedidos = Acta.objects.filter(
                    Q(suminis=base_codigo) |
                    Q(suminis=base_codigo + 'A') |
                    Q(suminis=base_codigo + 'P')
                ).values_list('pedido', flat=True).distinct()

                for p in pedidos:
                    cantidad_regla = reg.cantidad
                    codigo_requerido = reg.item_requerido.nombre.strip()
                    registros = Acta.objects.filter(pedido=p)

                    # cantidad total del item asociado
                    total = total_item_requerido(
                        registros, codigo_requerido, tipo_requerido)

                    if reg.comparador == "igual_a":  # OK LOGICA

                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total != cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "mayor_igual_a": # OK LOGICA
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total == 0 or total < cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "mayor_que":  # OK LOGICA
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total == 0 or total < cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "menor_igual_a": #OK LOGICA
                        
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total > cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)


                    if reg.comparador == "menor_que":  #OK LOGICA                        
    
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total > cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "diferente_de": # OK LOGICA

                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)
                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total == cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)
                    
            if reg.item.tipo == "obra":
                pedidos = Acta.objects.filter(item_cont=reg.item.nombre).values_list(
                    'pedido', flat=True).distinct()

                for p in pedidos:
                    cantidad_regla = reg.cantidad
                    codigo_requerido = reg.item_requerido.nombre.strip()
                    registros = Acta.objects.filter(pedido=p)
                    total = total_item_requerido(
                        registros, codigo_requerido, tipo_requerido)

                    if reg.comparador == "igual_a": # OK LOGICA
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)
                        print(cantidad_item)
                        print(total)
                        print(cantidad_regla)
                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total != cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "mayor_igual_a": # OK LOGICA
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total == 0 or total < cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "mayor_que":  # OK LOGICA
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total == 0 or total < cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "menor_igual_a": #OK LOGICA
                        
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total > cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "menor_que":  #OK LOGICA                        
    
                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total >= cantidad_regla:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

                    if reg.comparador == "diferente_de": # OK LOGICA

                        registro_actividad = Acta.objects.filter(
                            pedido=p).first()
                        cantidad_item = cantidad_item_total(
                            p, reg.item.nombre, reg.item.tipo)

                        if (reg.cantidad_requerida == 1) or (reg.cantidad_requerida > 1 and reg.cantidad_requerida == cantidad_item):
                            if total == cantidad_regla or total == 0:
                                nov = f"{reg.item.nombre} = {cantidad_regla}, {reg.item_requerido.nombre} = {total}"
                                if registro_actividad:
                                    crear_novedad(registro_actividad, nov)

    return redirect('novedades_acta')


def eliminar_regla(request, id):
    RelacionItemRegla.objects.get(id=id).delete()
    return redirect('listado_relaciones')
