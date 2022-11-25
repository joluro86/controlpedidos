from django.shortcuts import render, redirect
from bonificaciones.models import *
import datetime


def calcalulo_bonificaciones(request):
    calculo_valor_pedidos()
    calcular_bonificacion_diaria()

    return redirect('datos_por_pedido')


def calculo_valor_pedidos():
    pedidos = PedidoBoniPerseo.objects.all().only(
        'pedido', 'instalador', 'fecha')
    cont = 0
    calculados = []
    for p in pedidos:
        if p.pedido in calculados:
            pass
        else:
            cont += 1
            # print(cont)
            valor_perseo = calculo_valor_un_solo_pedido_perseo(p)
            valor_fenix = calculo_valor_un_solo_pedido_fenix(p)
            calculados.append(p.pedido)

            crear_valor_bonificacion_por_pedido(
                p.pedido, p.instalador, p.fecha, valor_perseo, valor_fenix)


# RETORNA EL VALOR DE LOS MATERIALES QUE MEJIA PONE
def calculo_valor_un_solo_pedido_perseo(pedido):
    pedidos = PedidoBoniPerseo.objects.filter(pedido=pedido.pedido)
    valor = 0

    for p in pedidos:
        if (p.codigo[0] >= '0' and p.codigo[0] <= '9'):
            pass
        else:
            valor += float(p.total)
            print(str(p.fecha) + " " + str(p.instalador) +
                  " " + str(p.codigo) + " valor: " + str(valor))

    print("valor retornado: " + str(valor))
    return valor


# RETORNA EL VALOR QUE PAGA EPM POR PEDIDO
def calculo_valor_un_solo_pedido_fenix(pedido):

    pedidos = PedidoBoniFenix.objects.filter(pedido=pedido.pedido)
    valor = 0

    for p in pedidos:

        if str(p.urbrur) == 'R':
            valor_linea = (float(p.valor)*1.27)
        if str(p.urbrur) == 'U':
            valor_linea = (float(p.valor)*1.17)

        valor += valor_linea

        # agregro el nombre del instalador al pedido del acta fenix
        p.instalador = pedido.instalador
        p.fecha = pedido.fecha
        p.total = valor_linea
        p.save()

    return valor


# GUARDA EL VALOR DE LA BONIFICACION POR PEDIDO
def crear_valor_bonificacion_por_pedido(pedido, instalador, fecha, valor_perseo, valor_fenix):
    dato_pedido = ValorBonificacion()
    dato_pedido.pedido = pedido
    dato_pedido.instalador = instalador
    dato_pedido.fecha = str(fecha[0:10])
    dato_pedido.valor_perseo = valor_perseo
    dato_pedido.valor_fenix = valor_fenix
    dato_pedido.diferencia = float(float(valor_fenix)-float(valor_perseo))
    dato_pedido.save()


def reiniciar_acta_bonificaciones(request):
    ValorBonificacion.objects.all().delete()
    # PedidoBoniFenix.objects.all().delete()
    # PedidoBoniPerseo.objects.all().delete()
    BonificacionDia.objects.all().delete()
    return redirect('datos_por_pedido')


def datos_por_pedido(request):
    bonificaciones = ValorBonificacion.objects.all()
    return render(request, 'datos_por_pedido.html', {'pedidos': bonificaciones})


def calcular_bonificacion_diaria():
    instaladores = ValorBonificacion.objects.all().only(
        'instalador', 'fecha').order_by('fecha')
    bonificacion = 0
    instaladores_calculados = []

    for i in instaladores:
        valor_producido_mes = 0
        if i.instalador in instaladores_calculados:
            pass

        else:
            print(i.instalador)
            fecha_inicial = RangoFechas.objects.get().fecha_inicial
            fecha_final = RangoFechas.objects.get().fecha_final

            valor = 0
            cont = 0
            laborado=0            

            while fecha_inicial <= fecha_final:

                bonificaciones_dia = ValorBonificacion.objects.filter(
                    fecha=fecha_inicial).filter(instalador=i.instalador)

                if len(bonificaciones_dia) > 0:
                    
                    for b in bonificaciones_dia:
                        valor += float(b.diferencia)
                        laborado+= float(float(b.valor_fenix)-float(b.valor_perseo))

                    bonificacion = ((float(valor))-(float(DatosBon.objects.get(nombre='Monto').valor)))*(
                        float(DatosBon.objects.get(nombre='Porcentaje').valor))/100

                    if bonificacion <= 0:
                        bonificacion = 0
                    guardar_bonificacion_diaria(
                        i, valor, fecha_inicial, bonificacion)
                    cont += 1

                valor = 0
                
                fecha_a_guardar = fecha_inicial
                fecha_inicial = fecha_inicial + datetime.timedelta(days=1)

            instaladores_calculados.append(i.instalador)
            valor_producido_mes+=laborado
            print("CONTADOR: " + str(cont))
            print(laborado)
            if laborado>0:
                print(laborado/cont)
            else:
                print(0)
            print("prod mes")
            print(valor_producido_mes)

            prom_diario = PromedioDiario()
            prom_diario.instalador = i.instalador
            prom_diario.fecha = fecha_a_guardar
            prom_diario.valor_producido_mes = valor_producido_mes
            prom_diario.numero_de_dias_laborados = cont

            if cont>0:
                prom_diario.promedio = valor_producido_mes/cont
                
            prom_diario.bonificacion = bonificacion
            prom_diario.save()

def guardar_bonificacion_diaria(instalador, valor_dia, fecha, bonificacion):
    bonificacion_dia = BonificacionDia()
    bonificacion_dia.instalador = instalador.instalador
    bonificacion_dia.fecha = fecha
    bonificacion_dia.laborado = valor_dia
    bonificacion_dia.bonificacion = bonificacion
    bonificacion_dia.save()


def bonificaciones_diarias(request):
    bonificaciones = BonificacionDia.objects.all()
    return render(request, 'bonificaciones_por_dia.html', {'bonificaciones': bonificaciones})
