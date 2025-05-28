from django.shortcuts import render, redirect
from analisis_acta.models import Acta
from analisis_acta.views import crear_novedad
from nuevo_analisis.models import RelacionItemRegla
from django.db.models import Sum
from decimal import Decimal
from django.db.models import Q

def validar_reglas(request):

    reglas = RelacionItemRegla.objects.all()
    for reg in reglas:
        if reg.factor == "unico":
            if reg.item.tipo == "actividad":

                pedidos = Acta.objects.filter(actividad=reg.item.nombre).values_list(
                    'pedido', flat=True).distinct()

                for p in pedidos:
                    cantidad_regla = reg.cantidad
                    codigo_requerido = reg.item_requerido.nombre.strip()
                    registros = Acta.objects.filter(pedido=p)

                    total = sum(
                        r.cantidad for r in registros
                        if r.suminis and r.suminis.rstrip('AP').strip() == codigo_requerido
                    )

                    if reg.comparador == "igual_a":
                        if total!=cantidad_regla:
                            registro_actividad = Acta.objects.filter(
                                pedido=p).first()
                            nov = f"{reg.item.nombre}= {cantidad_regla}, {reg.item_requerido.nombre}= {total}"
                            if registro_actividad:
                                crear_novedad(registro_actividad, nov)

                    if reg.comparador == "mayor_igual_a":
                        pass
                    if reg.comparador == "mayor_que":
                        pass

                    if reg.comparador == "menor_igual_que":
                        if total > cantidad_regla or total < 1:
                            registro_actividad = Acta.objects.filter(
                                pedido=p).first()
                            nov = f"{reg.item_requerido.nombre} igual a {total}"
                            if registro_actividad:
                                crear_novedad(registro_actividad, nov)

                    if reg.comparador == "menor_que":
                        pass
                    if reg.comparador == "diferente_de":
                        pass

            if reg.item.tipo == "suministro":
                base_codigo = reg.item.nombre.strip()

                pedidos = Acta.objects.filter(
                    Q(suminis=base_codigo) |
                    Q(suminis=base_codigo + 'A') |
                    Q(suminis=base_codigo + 'P')
                ).values_list('pedido', flat=True).distinct()
                cont=1
                for p in pedidos:
                    cantidad_regla = reg.cantidad
                    codigo_requerido = reg.item_requerido.nombre.strip()
                    registros = Acta.objects.filter(pedido=p)

                    total = sum(
                        r.cantidad for r in registros
                        if r.item_cont and r.item_cont.rstrip('AP').strip() == codigo_requerido
                    )

                    if reg.comparador == "igual_a": #OK LOGICA
                        if total!=cantidad_regla:
                            registro_actividad = Acta.objects.filter(
                                pedido=p).first()
                            nov = f"{reg.item.nombre}= {cantidad_regla}, {reg.item_requerido.nombre}= {total}"
                            if registro_actividad:
                                crear_novedad(registro_actividad, nov)
                            

                    if reg.comparador == "mayor_igual_a":
                        pass
                    if reg.comparador == "mayor_que":
                        pass

                    if reg.comparador == "menor_igual_que":
                        if total > cantidad_regla or total < 1:
                            registro_actividad = Acta.objects.filter(
                                pedido=p).first()
                            nov = f"{reg.item_requerido.nombre}= {total}"
                            if registro_actividad:
                                crear_novedad(registro_actividad, nov)

                    if reg.comparador == "menor_que":
                        pass
                    if reg.comparador == "diferente_de":
                        pass
                    
                    cont+=1
                
            if reg.item.tipo == "obra":
                pedidos = Acta.objects.filter(item_cont=reg.item.nombre).values_list(
                    'pedido', flat=True).distinct()

                for p in pedidos:
                    cantidad_regla = reg.cantidad
                    codigo_requerido = reg.item_requerido.nombre.strip()
                    registros = Acta.objects.filter(pedido=p)

                    total = sum(
                        r.cantidad for r in registros
                        if r.suminis and r.suminis.rstrip('AP').strip() == codigo_requerido
                    )

                    if reg.comparador == "igual_a":
                       pass

                    if reg.comparador == "mayor_igual_a": #OK LOGICA
                        if total == 0 or total < cantidad_regla:
                            registro_actividad = Acta.objects.filter(
                                pedido=p).first()
                            nov = f"{reg.item.nombre}= {cantidad_regla}, {reg.item_requerido.nombre}= {total}"
                            if registro_actividad:
                                crear_novedad(registro_actividad, nov)

                    if reg.comparador == "mayor_que":
                        pass

                    if reg.comparador == "menor_igual_que":
                        pass

                    if reg.comparador == "menor_que":
                        pass
                    if reg.comparador == "diferente_de":
                        pass

    return redirect('novedades_acta')


def eliminar_regla(request, id):
    RelacionItemRegla.objects.get(id=id).delete()
    return redirect('novedades_acta')
    