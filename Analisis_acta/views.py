from asyncio.windows_events import NULL
from datetime import datetime
from email.policy import HTTP
from django.shortcuts import redirect, render
from material_oficiales.models import Material_utilizado_perseo
from Analisis_acta.models import *


def calculo_novedades_acta(request):
    pedidos = Acta.objects.all()
    cont = 0
    for pedido in pedidos:

        cod = pedido.item_cont
        primera_letra = cod[0]
        if primera_letra == 'A':

            if pedido.item_cont == 'A 04':
                if int(pedido.cantidad) > 2:
                    nov = "Actividad: " + \
                        str(pedido.item_cont) + \
                        " con cantidad= " + str(pedido.cantidad)
                    crear_novedad(pedido, nov)
            elif int(pedido.cantidad) > 1 and pedido.item_cont != 'A 46':
                nov = "Actividad: " + \
                    str(pedido.item_cont) + \
                    " con cantidad= " + str(pedido.cantidad)
                crear_novedad(pedido, nov)

        if primera_letra == 'C' or primera_letra == 'D' or primera_letra == 'R':
            if int(pedido.cantidad) > 1:
                nov = "Actividad: " + \
                    str(pedido.item_cont) + \
                    " con cantidad= " + str(pedido.cantidad)
                crear_novedad(pedido, nov)

        if primera_letra == 'B':
            if pedido.item_cont == 'B 03':

                if int(pedido.cantidad) > 60:
                    nov = "Actividad: " + \
                        str(pedido.item_cont) + \
                        " con cantidad= " + str(pedido.cantidad)
                    crear_novedad(pedido, nov)

            if pedido.item_cont == 'B 04':
                if int(pedido.cantidad) > 12:
                    nov = "Actividad: " + \
                        str(pedido.item_cont) + \
                        " con cantidad= " + str(pedido.cantidad)
                    crear_novedad(pedido, nov)

            if pedido.item_cont == 'B 06' or pedido.item_cont == 'B 07' or pedido.item_cont == 'B 08':
                if int(pedido.cantidad) > 4:
                    nov = "Actividad: " + \
                        str(pedido.item_cont) + \
                        " con cantidad= " + str(pedido.cantidad)
                    crear_novedad(pedido, nov)

        if pedido.item_cont == '0':
            pedido.item_cont = pedido.suminis
            pedido.save()

        try:
            codigo = pedido.item_cont
            codigo_ultima_letra = codigo[-1]
            if codigo_ultima_letra == 'A' or codigo_ultima_letra == 'P':
                pedido.item_cont = str(codigo[:-1])
                pedido.save()

        except:
            pass

        pagina = pedido.pagina

        if (pagina[6:9] != '100' and pedido.urbrur == 'U') or (pagina[6:9] != '200' and pedido.urbrur == 'R'):
            try:
                busquedad_tipo_pagina = Novedad_acta.objects.filter(
                    pedido=pedido.pedido).filter(novedad='Tipo página').count()
                if busquedad_tipo_pagina == 0:
                    novedad = "Tipo página"
                    crear_novedad(pedido, novedad)

            except:
                pass

        if pedido.actividad == 'AEJDO':
            if pedido.item_cont == 'A 01':

                try:
                    busquedad_a04 = Acta.objects.filter(
                        pedido=pedido.pedido).filter(item_cont='A 04').count()

                    if busquedad_a04 == 0:
                        novedad = "A 01=1, A 04=0"
                        crear_novedad(pedido, novedad)
                except:
                    pass

                try:
                    busquedad_A23 = Acta.objects.filter(
                        pedido=pedido.pedido).filter(item_cont='A 23').count()
                    if busquedad_A23 == 0:
                        novedad = "A 01=1, A 23=0"
                        crear_novedad(pedido, novedad)
                except:
                    pass

                nov = "A 01=1,"
                busqueda_item(pedido, '200410', '200411', nov)
                busqueda_item(pedido, '211829', 0, nov)
                busqueda_item(pedido, '200092', '200093', nov)
                busqueda_item(pedido, '200316', 0, nov)
                busqueda_item(pedido, '211357', 0, nov)
                busqueda_item(pedido, '213333', 0, nov)
                busqueda_item(pedido, '219404', 0, nov)
                calculo_incompatible_A01(pedido, nov)

        if pedido.tipre == 'ENESUB' and (pedido.item_cont == 'A 27' or pedido.item_cont == 'A 03' or pedido.item_cont == 'A 28' or pedido.item_cont == 'A 29'):
            print("error enesub")
            nov = 'ENESUB con item ' + str(pedido.item_cont)
            crear_novedad(pedido, nov)

        if pedido.tipre == 'ENEPRE' and pedido.item_cont == 'A 44':
            print("error ENEPRE")
            nov = 'ENEPRE con item ' + str(pedido.item_cont)
            crear_novedad(pedido, nov)

        if pedido.actividad == 'DSPRE':
            if pedido.tipre == 'ENEPRE':
                calculo_enepre(pedido)

            if pedido.tipre == 'ENESUB':
                calculo_enepre(pedido)

        if pedido.tipre == 'ENESUB' and (pedido.item_cont == 'A 27' or pedido.item_cont == 'A 03' or pedido.item_cont == 'A 28' or pedido.item_cont == 'A 29'):
            print("error enesub")

        if pedido.item_cont == 'A 02':
            nov = "A 02=1,"
            busqueda_item(pedido, '211829', 0, nov)

        if pedido.item_cont == 'A 10' or pedido.item_cont == 'A 11':
            busqueda_item(pedido, '200410', 0, pedido.item_cont)
            busqueda_item(pedido, '211829', 0, pedido.item_cont)

        if pedido.item_cont == '211829':
            insumo = "211829"
            busqueda_insumo(pedido, insumo)

        if pedido.item_cont == 'A 04':
            nov = "A 04=1,"
            busqueda_item(pedido, '210948', '210949', nov)

        if pedido.item_cont == '210948' or pedido.item_cont == '210949':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)

        if pedido.item_cont == 'A 06':
            nov = "A 06=1,"
            busqueda_item(pedido, '200410', '200411', nov)

        if pedido.item_cont == '200410' or pedido.item_cont == '200411':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)

        if pedido.item_cont == 'A 23':
            nov = "A 23=1,"
            busqueda_item(pedido, '211673', '210947', nov)

        if pedido.item_cont == '211673':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)

        if pedido.item_cont == 'A 24':
            nov = "A 24=1,"
            busqueda_item(pedido, '211357', 0, nov)

        if pedido.item_cont == '211357':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)

        if pedido.item_cont == 'A 25':
            nov = "A 25=1,"
            busqueda_item(pedido, '213333', 0, nov)

        if pedido.item_cont == '213333':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)

        if pedido.item_cont == 'A 34':
            nov = "A 34=1,"
            busqueda_item(pedido, '211686', 0, nov)

        if pedido.item_cont == '211686':
            insumo = str(pedido.item_cont)
            busqueda_insumo_por_item(pedido, insumo, 'A 34')

        if pedido.item_cont == 'A 39':
            nov = "A 39=1,"
            busqueda_item(pedido, '200410', '200411', nov)
            busquedad_200410 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont='200410')
            busquedad_200411 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont='200411')

            for b in busquedad_200410:
                if len(busquedad_200410) > 0:
                    if float(b.cantidad) < 8:
                        crear_novedad(
                            pedido, 'Cantidad de cable 200410 ó 200411 menor a 8')

            for b in busquedad_200411:
                if len(busquedad_200411) > 0:
                    if float(b.cantidad) < 8:
                        crear_novedad(
                            pedido, 'Cantidad de cable 200410 ó 200411 menor a 8')

        if pedido.item_cont == 'A 42':
            nov = "A 42=1,"
            busqueda_item(pedido, '200410', '200411', nov)

        if pedido.item_cont == '200092' or pedido.item_cont == '200093' or pedido.item_cont == '200098':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)

        if pedido.cantidad == '0' or pedido.cantidad == "":
            crear_novedad(pedido, str(pedido.item_cont) +
                          ". Cantidad igual a cero.")

        if pedido.suminis == '200092' or pedido.suminis == '200098':
            verificar_cable_acta(pedido.pedido, '200411',
                                 '200410', pedido.suminis)

        if pedido.suminis == '200093':
            verificar_cable_acta(pedido, '200410', '200411', pedido.suminis)

        if pedido.item_cont == 'A 40' or pedido.item_cont == 'A 41':
            if pedido.item_cont == 'A 40':
                calculo_otros_incompatibles(pedido, 'A 41', pedido.item_cont)
            if pedido.item_cont == 'A 41':
                calculo_otros_incompatibles(pedido, 'A 40', pedido.item_cont)

        if pedido.item_cont == 'A 10' or pedido.item_cont == 'A 11':
            if pedido.item_cont == 'A 10':
                calculo_otros_incompatibles(pedido, 'A 11', pedido.item_cont)
            if pedido.item_cont == 'A 11':
                calculo_otros_incompatibles(pedido, 'A 10', pedido.item_cont)

    novedades = Novedad_acta.objects.all()

    return render(request, "analisis.html", {'novedades': novedades})


def busqueda_insumo_por_item(pedido, insumo, item):
    try:
        pedidos = Acta.objects.filter(pedido=pedido)

        encontreinsumo = 0
        for p in pedidos:
            letra = p.item_cont[0]
            if letra == 'A':

                if p.item_cont == item:
                    encontreinsumo = 1

        if encontreinsumo == 0:
            nov = insumo + ', insumo sin actividad'
            crear_novedad(pedido, nov)

    except:
        pass


def busqueda_insumo(pedido, insumo):
    try:
        pedidos = Acta.objects.filter(pedido=pedido)

        if insumo == '200092' or insumo == '200093' or insumo == '200098':
            encontreinsumo = 0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra == 'A':

                    if p.item_cont == 'A 03' or p.item_cont == 'A 44' or p.item_cont == 'A 01' or p.item_cont == 'A 27':
                        encontreinsumo = 1

            if encontreinsumo == 0:
                nov = insumo + ', insumo sin actividad'
                crear_novedad(pedido, nov)

        if insumo == '211357':
            encontreinsumo = 0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra == 'A':

                    if p.item_cont == 'A 24' or p.item_cont == 'A 01':
                        encontreinsumo = 1

            if encontreinsumo == 0:
                nov = insumo + ', insumo sin actividad'
                crear_novedad(pedido, nov)

        if insumo == '213333':
            encontreinsumo = 0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra == 'A':

                    if p.item_cont == 'A 25' or p.item_cont == 'A 01':
                        encontreinsumo = 1

            if encontreinsumo == 0:
                nov = insumo + ', insumo sin actividad'
                crear_novedad(pedido, nov)

        if insumo == '211673':
            encontreinsumo = 0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra == 'A':

                    if p.item_cont == 'A 23':
                        encontreinsumo = 1

            if encontreinsumo == 0:
                nov = insumo + ', insumo sin actividad'
                crear_novedad(pedido, nov)

        if insumo == '200410' or insumo == '200411':
            encontreinsumo = 0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra == 'A':

                    if p.item_cont == 'A 06' or p.item_cont == 'A 01' or p.item_cont == 'A 39' or p.item_cont == 'A 41' or p.item_cont == 'A 42':
                        encontreinsumo = 1

            if encontreinsumo == 0:
                nov = insumo + ', insumo sin actividad'
                crear_novedad(pedido, nov)

        if insumo == '211829':
            encontreinsumo = 0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra == 'A':

                    if p.item_cont == 'A 02' or p.item_cont == 'A 27' or p.item_cont == 'A 01':
                        encontreinsumo = 1

            if encontreinsumo == 0:
                nov = insumo + ', insumo sin actividad'
                crear_novedad(pedido, nov)

        if insumo == '210948' or insumo == '210949':

            encontreinsumo = 0

            for p in pedidos:
                letra = p.item_cont[0]
                if letra == 'C':
                    encontreinsumo = 1
                if letra == 'A':

                    if p.item_cont == 'A 04' or p.item_cont == 'A 01' or p.actividad == 'ALEGA' or p.actividad == 'ALECA' or p.actividad == 'ALEGN' or p.actividad == 'ACAMN':
                        encontreinsumo = 1

            if encontreinsumo == 0:
                nov = insumo + ', insumo sin actividad'
                crear_novedad(pedido, nov)

    except:
        pass


def busqueda_item(pedido, item, item2, novedad):

    if item == '210948':
        try:
            busquedad_210949 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont=item).count()
            busquedad_210948 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont='210949').count()

            if busquedad_210949 == 0 and busquedad_210948 == 0:
                novedad = novedad+" "+str(item)+"=0, 210949=0"
                crear_novedad(pedido, novedad)
        except:
            pass
    elif pedido.item_cont == 'A 42':
        try:
            busquedad_200410 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont=item).count()
            busquedad_200411 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont='200411').count()
            busquedad_200316 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont='200316').count()

            if busquedad_200410 == 0 and busquedad_200411 == 0 and busquedad_200316 == 0:
                novedad = novedad+" "+str(item)+"=0, 200411=0, 200316=0 "
                crear_novedad(pedido, novedad)
        except:
            pass

    elif (pedido.item_cont == 'A 10' or pedido.item_cont == 'A 11') and item == '200410':
        try:
            busquedad_200410 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont=item).count()
            busquedad_200411 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont='200411').count()

            busquedad_a03 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont='A 03').count()
            busquedad_a28 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont='A 28').count()
            busquedad_a29 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont='A 29').count()

            if busquedad_a03 != 0 and busquedad_a28 != 0 and busquedad_a29 != 0:

                if busquedad_200410 == 0 and busquedad_200411 == 0:
                    novedad = novedad + " 200410=0, 200411=0."
                    crear_novedad(pedido, novedad)
        except:
            pass

    elif item2 != 0:

        try:
            busquedad_1 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont=item).count()
            busquedad_2 = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont=item2).count()

            if busquedad_1 == 0 and busquedad_2 == 0:
                novedad = novedad+" "+str(item)+"=0, " + str(item2)+"=0, "
                crear_novedad(pedido, novedad)
        except:
            pass

    else:
        try:
            busquedad = Acta.objects.filter(
                pedido=pedido.pedido).filter(item_cont=item).count()
            if busquedad == 0:
                novedad = novedad+" "+str(item)+"=0"
                crear_novedad(pedido, novedad)
        except:
            pass


def calculo_incompatible_A01(pedido, novedad):
    try:
        pedidos = Acta.objects.filter(pedido=pedido.pedido)
        cont = 1
        for p in pedidos:
            letra = p.item_cont[0]
            if letra == 'A':
                if p.item_cont != 'A 01' and p.item_cont != 'A 04' and p.item_cont != 'A 23':
                    nov = 'A 01=1, ' + p.item_cont + ">0. Incompatibles."
                    crear_novedad(p, nov)
    except:
        pass


def calculo_incompatible_A27(pedido, novedad):
    try:
        pedidos = Acta.objects.filter(pedido=pedido.pedido)
        cont = 1
        for p in pedidos:
            letra = p.item_cont[0]
            if letra == 'A':
                if p.item_cont == 'A 02' or p.item_cont == 'A 44' or p.item_cont == 'A 03':
                    nov = 'A 27=1, ' + p.item_cont + ">0. Incompatibles."
                    crear_novedad(p, nov)
    except:
        pass


def calculo_incompatible_A44(pedido, novedad):
    try:
        pedidos = Acta.objects.filter(pedido=pedido.pedido)
        cont = 1
        for p in pedidos:
            letra = p.item_cont[0]
            if letra == 'A':
                if p.item_cont == 'A 27' or p.item_cont == 'A 03':
                    nov = 'A 44=1, ' + p.item_cont + ">0. Incompatibles."
                    crear_novedad(p, nov)
    except:
        pass


def calculo_incompatible_A03(pedido, novedad):
    try:
        pedidos = Acta.objects.filter(pedido=pedido.pedido)
        cont = 1
        for p in pedidos:
            letra = p.item_cont[0]
            if letra == 'A':
                if p.item_cont == 'A 27' or p.item_cont == 'A 44':
                    nov = 'A 03=1, ' + p.item_cont + ">0. Incompatibles."
                    crear_novedad(p, nov)
    except:
        pass


def calculo_otros_incompatibles(pedido, item_comparar, comparado):
    try:
        pedidos = Acta.objects.filter(pedido=pedido.pedido)
        for p in pedidos:
            if p.item_cont == item_comparar:
                nov = str(comparado) + ' incompatible con ' + item_comparar
                crear_novedad(p, nov)
    except:
        pass


def crear_novedad(pedido, nov):
    novedad = Novedad_acta()
    novedad.pedido = pedido.pedido
    novedad.actividad = pedido.actividad
    novedad.municipio = pedido.municipio
    novedad.tipre = pedido.tipre
    novedad.pagina = pedido.pagina
    novedad.item = pedido.item_cont
    novedad.novedad = nov
    novedad.save()


def limpiar_novedades(request):
    Novedad_acta.objects.all().delete()
    Material_utilizado_perseo.objects.all().delete()
    return redirect('novedades_acta')


def limpiar_acta(request):
    Acta.objects.all().delete()
    return redirect('home')


def calculo_enepre(pedido):
    if pedido.item_cont == 'A 03':
        try:
            novedad = "A 03=1, "
            busqueda_item(pedido, 'A 28', 0, novedad)
            busqueda_item(pedido, 'A 29', 0, novedad)
            busqueda_item(pedido, '219404', 0, novedad)
            busqueda_item(pedido, '220683',  0, novedad)
            calculo_incompatible_A03(pedido, novedad)
        except:
            pass

    if pedido.item_cont == 'A 27':
        try:
            novedad = "A 27=1, "
            busqueda_item(pedido, 'A 41', 0, novedad)
            busqueda_item(pedido, '219404', 0, novedad)
            busqueda_item(pedido, 'A 10', 'A 11', novedad)
            calculo_incompatible_A27(pedido, novedad)
        except:
            pass

    if pedido.item_cont == 'A 44':
        try:
            novedad = "A 44=1, "
            busqueda_item(pedido, 'A 39', 0, novedad)
            busqueda_item(pedido, 'A 40', 'A 41', novedad)
            busqueda_item(pedido, '219404', 0, novedad)
            calculo_incompatible_A44(pedido, novedad)

            pedidos = Acta.objects.filter(pedido=pedido.pedido)

            encontre_A40 = 0
            encontre_A10 = 0
            encontre_A11 = 0
            encontre_riel = 0

            for p in pedidos:
                if p.item_cont == 'A 40':
                    encontre_A40 = 1
                if p.item_cont == 'A 10':
                    encontre_A10 = 1
                if p.item_cont == 'A 11':
                    encontre_A11 = 1
                if p.item_cont == '220683':
                    encontre_riel = 1

            if encontre_A40 == 0 and encontre_A10 == 0 and encontre_A11 == 0:
                novedad = novedad+"A 10=0, A 11=0"
                crear_novedad(pedido, novedad)
            if encontre_A40 == 1:
                if encontre_A10 == 1 or encontre_A11 == 1:
                    novedad = novedad+"A 40 incompatible con A 10 y A 11"
                    crear_novedad(pedido, novedad)
                if encontre_riel == 1:
                    nov = "A 40 excluye riel (220683)."
                    crear_novedad(pedido, nov)

        except:
            pass


def novedades_acta(request):
    novedades = {}
    try:
        novedades = Novedad_acta.objects.all()
    except:
        pass
    return render(request, "analisis.html", {'novedades': novedades})


def verificar_cable_acta(pedido, cable1, cable2, medidor):

    pedido1 = Acta.objects.filter(pedido=pedido).filter(item_cont=cable1)

    if len(pedido1) > 0:
        for p in pedido1:
            if float(p.cantidad) > 1:
                novedad = "Medidor: " + \
                    str(medidor)+" con cable " + \
                    str(p.suminis) + " : " + str(p.cantidad)

                pedido2 = Acta.objects.filter(
                    pedido=p).filter(item_cont=cable2)

                if len(pedido2) > 0:
                    for p in pedido2:
                        if float(p.cantidad) > 0:
                            novedad += " - " + \
                                str(p.suminis) + " : " + str(p.cantidad)

                crear_novedad(p, novedad)
