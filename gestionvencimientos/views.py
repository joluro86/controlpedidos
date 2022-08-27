from asyncio.windows_events import NULL
from datetime import date, datetime, timedelta
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import holidays_co
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User, auth
from controlpedidos import settings
from gestionvencimientos.models import Acta, Actividad, Actividad_epm, Ans, Encargado, Guia, Inicio, Liquidacion_acta_epm, Material_utilizado_perseo, Municipio, Novedad_acta, NumeroActa, Oficial, Vencido, faltanteperseo, matfenix, matperseo

@login_required
def index(request):
    return render(request,  "index.html")

def calculo_dia_actutal():

    fecha_actual = datetime.now()
    dia = 0

    if fecha_actual.weekday() == 1:
        dia = 1

    if fecha_actual.weekday() == 2:
        dia = 2

    if fecha_actual.weekday() == 3:
        dia = 3

    if fecha_actual.weekday() == 4:
        dia = 4
    
    if fecha_actual.weekday() == 5:
        dia = 5
    
    if fecha_actual.weekday() == 6:
        dia = 6

    return dia

def calculo_dia_semana_2():
    
    fecha_actual = datetime.now()
    lunes = datetime.now()

    if fecha_actual.weekday() == 0:
        lunes = datetime.now()

    if fecha_actual.weekday() == 1:
        lunes = datetime.now()-timedelta(days=1)

    if fecha_actual.weekday() == 2:
        lunes = datetime.now()-timedelta(days=2)

    if fecha_actual.weekday() == 3:
        lunes = datetime.now()-timedelta(days=3)

    if fecha_actual.weekday() == 4:
        lunes = datetime.now()-timedelta(days=4)
    
    if fecha_actual.weekday() == 5:
        lunes = datetime.now()+timedelta(days=2)
    
    if fecha_actual.weekday() == 6:
        lunes = datetime.now()+timedelta(days=1)

    return lunes

def menu_pendientes(self):
    id_dia = calculo_dia_actutal()+1
    
    return redirect('pendientes', id_dia)

def limpiar_base(request):
    lista_ans = []
    aneses = Ans.objects.all().only('Subzona', 'Actividad')

    for ans in aneses:
        if ans.Subzona != "Uraba":
            ans.delete()

        elif ans.Actividad != "ACREV" and ans.Actividad != "AEJDO" and ans.Actividad != "ARTER" and ans.Actividad != "DIPRE" and ans.Actividad != "INPRE" and ans.Actividad != "REEQU" and ans.Actividad != "APLIN" and ans.Actividad != "ALEGA" and ans.Actividad != "ALEGN" and ans.Actividad != "ALECA" and ans.Actividad != "ACAMN" and ans.Actividad != "AMRTR":
            ans.delete()

    return redirect("gestionbd")

def calculo_pendientes(request, id_dia):

    lunes = calculo_dia_semana_2()
    encargados = Encargado.objects.all()

    if id_dia == 1:

        list_ans = busqueda_pendientes(lunes.strftime('%Y-%m-%d'))

        return render(request, "pendientes_lunes.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': lunes.strftime('%Y-%m-%d')})

    if id_dia == 2:

        list_ans = busqueda_pendientes((lunes+timedelta(days=1)).strftime('%Y-%m-%d'))

        return render(request, "pendientes_lunes.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=1)).strftime('%Y-%m-%d')})

    if id_dia == 3:

        list_ans = busqueda_pendientes(
            (lunes+timedelta(days=2)).strftime('%Y-%m-%d'))

        return render(request, "pendientes_lunes.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=2)).strftime('%Y-%m-%d')})

    if id_dia == 4:

        list_ans = busqueda_pendientes(
            (lunes+timedelta(days=3)).strftime('%Y-%m-%d'))

        return render(request, "pendientes_lunes.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=3)).strftime('%Y-%m-%d')})

    if id_dia == 5:

        list_ans = busqueda_pendientes(
            (lunes+timedelta(days=4)).strftime('%Y-%m-%d'))

        return render(request, "pendientes_lunes.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=4)).strftime('%Y-%m-%d')})
    
    if id_dia == 6 or id_dia == 7:
    
        list_ans = busqueda_pendientes(
            (lunes).strftime('%Y-%m-%d'))

        return render(request, "pendientes_lunes.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes).strftime('%Y-%m-%d')})

def busqueda_vencidos(request):
    aneses = Ans.objects.filter(Estado="PENDI")
    list_ans = []
    for ans in aneses:
        if ans.Estado == "PENDI" and ans.Concepto == "PENDI":
            continue
        if ans.Estado == "PENDI" and ans.Concepto == "592":
            continue
        if ans.Tipo_Elemento_ID == "ENEGED":
            continue
        try:
            fecha_vence_ans = datetime.strptime(ans.fecha_vencimiento, "%Y-%m-%d %H:%M:%S")
            if fecha_vence_ans < datetime.today():
                if ans.estado_cierre == 0:
                    list_ans.append(ans)
        except Exception as e: 
            print("An exception occurred in fecha vencimiento 2") 
            print(repr(e))                              

    return render(request, "vencidos-todos.html" , {"aneses": list_ans})

def busqueda_pendientes(fecha_vence_buscar):
    aneses = Ans.objects.filter(Estado="PENDI")
    list_ans = []
    for ans in aneses:
        if ans.Estado == "PENDI" and ans.Concepto == "PENDI":
            continue
        if ans.Estado == "PENDI" and ans.Concepto == "592":
            continue
        try:
            fecha_vence_ans = datetime.strptime(ans.fecha_vencimiento, "%Y-%m-%d %H:%M:%S")
            if fecha_vence_ans.strftime('%Y-%m-%d') == fecha_vence_buscar:
                if ans.estado_cierre == 0:
                    list_ans.append(ans) 
        except Exception as e: 
            print("An exception occurred in busqueda pendientes") 
            print(repr(e)) 

    list_ans = cambiar_formato_fecha(list_ans) 
    
    return list_ans

def cambiar_formato_fecha(fecha_a_cambiar):
    for l in fecha_a_cambiar:
        if l.fecha_vencimiento==None or l.fecha_vencimiento=='0' :
            pass
        else:
            fecha = l.fecha_vencimiento.replace('-','/')
            fecha_vencimiento   = datetime.strptime(fecha, "%Y/%m/%d %H:%M:%S")
            l.fecha_vencimiento = fecha_vencimiento.strftime("%d/%m/%Y %H:%M:%S")
    
    return fecha_a_cambiar

def cambiar_formato_fecha_epm(fecha_a_cambiar):
    for l in fecha_a_cambiar:
        if l.fecha_vencimiento==None or l.fecha_vencimiento=='0' :
            pass
        else:
            fecha = l.fecha_vencimiento.replace('-','/')
            fecha_vencimiento   = datetime.strptime(fecha, "%Y/%m/%d %H:%M:%S")
            l.fecha_vencimiento = fecha_vencimiento.strftime("%d/%m/%Y %H:%M:%S")

            fecha2 = l.fecha_vence_epm.replace('-','/')
            fecha_vencimiento_epm   = datetime.strptime(fecha2, "%Y/%m/%d %H:%M:%S")
            l.fecha_vence_epm = fecha_vencimiento_epm.strftime("%d/%m/%Y %H:%M:%S")

            l.fecha_vence_sin_hora = fecha_vencimiento_epm.strftime("%d/%m/%Y")
    
    return fecha_a_cambiar

def eliminar_bd(request):
    Ans.objects.all().delete()

    return redirect('home')

def fechas(fecha_inic, dias):

    fecha_vencimiento = datetime. strptime(fecha_inic, '%Y-%m-%d %H:%M:%S')
    cont = 0

    while cont < dias:

        fecha_vencimiento = fecha_vencimiento+timedelta(days=1)

        if es_festivo_o_fin_de_semana(fecha_vencimiento):
            continue
        else:
            cont = cont+1

    return fecha_vencimiento

def es_festivo_o_fin_de_semana(fecha):
    if holidays_co.is_holiday_date(fecha):
        return True
    if fecha.weekday() == 5 or fecha.weekday() == 6:
        return True

def gestion_bd(request): 
     
    lista_ans = []
    Ans.objects.filter(Estado ="ANULA").delete()
    Ans.objects.filter(Estado = "PENDI").filter(Concepto = "PENDI").delete()
    
    anses = Ans.objects.all()
    
    for ans in anses:
        
        if ans.Actividad != "DSPRE"  and ans.Actividad != "AEJDO" and ans.Actividad != "ACREV" and ans.Actividad != "ARTER" and ans.Actividad != "DIPRE" and ans.Actividad != "ACREV" and ans.Actividad != "INPRE" and ans.Actividad != "REEQU" and ans.Actividad != "APLIN" and ans.Actividad != "ALEGA" and ans.Actividad != "ALEGN" and ans.Actividad != "ALECA" and ans.Actividad != "ACAMN" and ans.Actividad != "AMRTR":
            ans.delete()
            
        if ans.Concepto != "406" and ans.Concepto != "414" and ans.Concepto != "430" and ans.Concepto != "495" and ans.Concepto != "PENDI" and ans.Concepto != "FSE" and ans.Concepto != "PPRG" and ans.Concepto != "PROG":
            ans.delete()

    aneses = Ans.objects.all()

    for ans in aneses:

        try:
            if ans.Instalación[7:10] == "100":
                ans.Tipo_Dirección = "Urbano"
                ans.save()
            if ans.Instalación[7:10] == "200":
                ans.Tipo_Dirección = "Rural"
                ans.save()

            if ans.Fecha_Inicio_ANS == "":
                ans.Fecha_Inicio_ANS = ans.Fecha_Concepto
                ans.save()

            actividad = Actividad.objects.get(nombre=ans.Actividad)
            actividad_epm = Actividad_epm.objects.get(nombre=ans.Actividad)
            
            if ans.Tipo_Dirección == "Urbano":
                ans.dias_vencimiento = int(actividad.dias_urbano)
                ans.dias_vencimiento_epm = int(actividad_epm.dias_urbano)
            if ans.Tipo_Dirección == "Rural":
                ans.dias_vencimiento = int(actividad.dias_rural)
                ans.dias_vencimiento_epm = int(actividad_epm.dias_rural)

            fecha = fechas(ans.Fecha_Inicio_ANS, ans.dias_vencimiento)
            ans.fecha_vencimiento = fecha
            
            fecha_epm = fechas(ans.Fecha_Inicio_ANS, ans.dias_vencimiento_epm)
            ans.fecha_vence_epm = fecha_epm
            ans.fecha_vence_sin_hora = fecha.date().strftime("%d-%m-%Y")
            
            # inicio calculo vence epm
            
            # fin calculo vence epm
    
            ans.hora_vencimiento= fecha.time()

            ans.encargado = str(actividad.encargado)

            ans.save()

        except Exception as e: 
            print("error gestion bd")
            print(e)  

    return redirect('menu_pendientes')

def cerrar_pedido(request, id_pedido):
   
    ans_cerrar = Ans.objects.get(id=id_pedido)

    ans_cerrar.estado_cierre = 1
    ans_cerrar.save()

    return redirect('menu_pendientes')

def calculo_next_week(request, id_dia):
    
    lunes = calculo_dia_semana_2()
    encargados = Encargado.objects.all()
    if id_dia == 10:

        list_ans =  list_ans = busqueda_pendientes(
            (lunes+timedelta(days=7)).strftime('%Y-%m-%d'))

        return render(request, "pendientes_next_week.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=7)).strftime('%Y-%m-%d')})

    if id_dia == 20:

        list_ans = busqueda_pendientes(
            (lunes+timedelta(days=8)).strftime('%Y-%m-%d'))

        return render(request, "pendientes_next_week.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=8)).strftime('%Y-%m-%d')})

    if id_dia == 30:

        list_ans = busqueda_pendientes(
            (lunes+timedelta(days=9)).strftime('%Y-%m-%d'))

        return render(request, "pendientes_next_week.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=9)).strftime('%Y-%m-%d')})

    if id_dia == 40:

        list_ans = busqueda_pendientes(
            (lunes+timedelta(days=10)).strftime('%Y-%m-%d'))

        return render(request, "pendientes_next_week.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=10)).strftime('%Y-%m-%d')})

    if id_dia == 50:

        list_ans = busqueda_pendientes(
            (lunes+timedelta(days=11)).strftime('%Y-%m-%d'))

        return render(request, "pendientes_next_week.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=11)).strftime('%Y-%m-%d')})

def vencidos(request):
    aeneses = Vencido.objects.all()
        
    return render(request, "vencidos.html", {"aneses":aeneses})

def vencimientos_epm(request, inicio, final):
    fecha_inicio = inicio+" "+"00:00:00"
    fecha_final = final+" "+"23:59:59"
    aeneses=[]
    ans = Ans.objects.all()
    for a in ans:
        if a.fecha_vence_epm>fecha_inicio and a.fecha_vence_epm<fecha_final:
            aeneses.append(a)
    aeneses = cambiar_formato_fecha_epm(aeneses)    
    return render(request, "pendientes_epm.html", {"aneses":aeneses})

def pedidos_week(request, id_week):
    
    lunes = calculo_dia_semana_2()
    
    encargados = Encargado.objects.all()
    
    dia=0
    
    if id_week==2:
        dia=7
        list_ans_lunes = busqueda_pendientes((lunes+timedelta(days=dia)).strftime('%Y-%m-%d'))
    else:
        list_ans_lunes = busqueda_pendientes(lunes.strftime('%Y-%m-%d'))
        
    
    list_ans_martes = busqueda_pendientes((lunes+timedelta(days=dia+1)).strftime('%Y-%m-%d'))
    list_ans_lunes.extend(list_ans_martes)
    
    list_ans_miercoles = busqueda_pendientes((lunes+timedelta(days=dia+2)).strftime('%Y-%m-%d'))
    list_ans_miercoles.extend(list_ans_lunes)
    
    list_ans_jueves = busqueda_pendientes((lunes+timedelta(days=dia+3)).strftime('%Y-%m-%d'))
    list_ans_miercoles.extend(list_ans_jueves)
    
    
    list_ans_viernes = busqueda_pendientes((lunes+timedelta(days=dia+4)).strftime('%Y-%m-%d'))
    list_ans_miercoles.extend(list_ans_viernes)
    
    if id_week==2:
        viernes = (lunes+timedelta(days=dia+4)).strftime('%d-%m-%Y')
        lunes = (lunes+timedelta(days=7)).strftime('%d-%m-%Y')
    else:
        viernes = (lunes+timedelta(days=dia+4)).strftime('%d-%m-%Y')
        lunes = lunes.strftime('%d-%m-%Y') 
    
    lista_pedidos = list_ans_miercoles

    return render(request, "pedidos_week.html", {"aneses":lista_pedidos, "lunes":lunes, "viernes":viernes})

def otros_pedidos(request, cliente, apla, pendi):
    
    if cliente == 1 and apla == 0 and pendi == 0:
          vencidos = Ans.objects.filter(Estado = "CLIEN")
          return render(request, "otros_pedidos.html", {"aneses": vencidos})
        
    if cliente == 0 and apla == 2 and pendi == 0:
        vencidos = Ans.objects.filter(Estado = "APLAZ")
        return render(request, "otros_pedidos.html", {"aneses": vencidos})
        
    if cliente == 0 and apla == 0 and pendi == 3:
        vencidos = Ans.objects.filter(Estado = "PENDI")
        return render(request, "otros_pedidos.html", {"aneses": vencidos})
            
    if cliente == 1 and apla == 2 and pendi == 0:
        vencidos = Ans.objects.filter(Q(Estado="CLIEN") | Q(Estado="APLAZ"))
        return render(request, "otros_pedidos.html", {"aneses": vencidos})
                
    if cliente == 0 and apla == 2 and pendi == 3:
        vencidos = Ans.objects.filter(Q(Estado="PENDI") | Q(Estado="APLAZ"))
        return render(request, "otros_pedidos.html", {"aneses": vencidos})
            
    if cliente == 1 and apla == 0 and pendi == 3:
        vencidos = Ans.objects.filter(Q(Estado="PENDI") | Q(Estado="CLIEN"))
        return render(request, "otros_pedidos.html", {"aneses": vencidos})
            
    if cliente == 1 and apla == 2 and pendi == 3:
        vencidos = Ans.objects.filter(Q(Estado="PENDI") | Q(Estado="CLIEN") | Q(Estado="APLAZ"))
        return render(request, "otros_pedidos.html", {"aneses": vencidos})
    
    return HttpResponse("Error en la consulta de otros pedidos")

def cierre_masivo(request, fecha_cierre, hora_cierre):
    
    fecha = fecha_cierre+ " " + hora_cierre + ":00"
    
    fecha_hora_cierre_masivo =datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
    
    aeneses_a_cerrar = busqueda_pendientes(fecha_cierre)
    
    for ans in aeneses_a_cerrar:
        try:
           ans.estado_cierre = 1
           ans.save()
        except:
            print("An exception occurred in cierre masivo")  
    
    return redirect('menu_pendientes')

def acrev(request):
    
    aeneses = Ans.objects.filter(Actividad = "ACREV").filter(Q(Estado="PENDI") | Q(Concepto="406") | Q(Concepto="414")| Q(Concepto="495")| Q(Concepto="430"))
    aeneses = cambiar_formato_fecha(aeneses)
    return render(request, "acrev.html", {"aneses": aeneses} )

def amrtr(request):
    
    aeneses = Ans.objects.filter(Actividad = "AMRTR").filter(Q(Estado="PENDI") | Q(Concepto="406") | Q(Concepto="414")| Q(Concepto="495")| Q(Concepto="430"))
    aeneses = cambiar_formato_fecha(aeneses)
    return render(request, "amrtr.html", {"aneses": aeneses} )

def lega(request):
    
    aeneses = Ans.objects.filter(Q(Actividad="ALEGA") | Q(Actividad="ALEGN") | Q(Actividad="ALECA") |Q(Actividad="ACAMN") ).filter(Q(Estado="PENDI") | Q(Concepto="406") | Q(Concepto="414")| Q(Concepto="495")| Q(Concepto="430"))
    aeneses = cambiar_formato_fecha(aeneses)
    return render(request, "lega.html", {"aneses": aeneses} )

def direccionamiento(request):
    
    aeneses = Ans.objects.filter(Q(Actividad="ACREV")).filter(Tipo_Dirección = "Urbano").filter(Concepto = "PPRG")
    
    return render(request, "direccionamiento.html", {"aneses": aeneses} )

def programador(request):
    aeneses = Ans.objects.all()
    
    return render(request, "programador.html", {"aneses": aeneses} )

def calculo_last_week(request, id_dia):
    
    lunes = calculo_dia_semana_2()
    encargados = Encargado.objects.all()
    if id_dia == 10:

        list_ans =  list_ans = busqueda_pendientes((lunes-timedelta(days=7)).strftime('%Y-%m-%d'))
        return render(request, "pendientes_last_week.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=7)).strftime('%Y-%m-%d')})

    if id_dia == 20:

        list_ans = busqueda_pendientes((lunes-timedelta(days=6)).strftime('%Y-%m-%d'))
        return render(request, "pendientes_last_week.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=8)).strftime('%Y-%m-%d')})

    if id_dia == 30:

        list_ans = busqueda_pendientes((lunes-timedelta(days=5)).strftime('%Y-%m-%d'))
        return render(request, "pendientes_last_week.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=9)).strftime('%Y-%m-%d')})

    if id_dia == 40:

        list_ans = busqueda_pendientes((lunes-timedelta(days=4)).strftime('%Y-%m-%d'))
        return render(request, "pendientes_last_week.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=10)).strftime('%Y-%m-%d')})

    if id_dia == 50:

        list_ans = busqueda_pendientes((lunes-timedelta(days=3)).strftime('%Y-%m-%d'))
        return render(request, "pendientes_last_week.html", {'id_dia':id_dia,'encargados': encargados,'aneses': list_ans, 'total': len(list_ans), 'fecha': (lunes+timedelta(days=11)).strftime('%Y-%m-%d')})

def novedades_acta(request):
    novedades={}
    try:
        novedades=Novedad_acta.objects.all()
    except:
        pass
    return render(request, "analisis.html", {'novedades':novedades})

def calculo_novedades_acta(request):
    pedidos= Acta.objects.all()
    print("tamañao: " + str(len(pedidos)))
    cont=1
    for pedido in pedidos:
        
        if pedido.item_cont=='0':
            pedido.item_cont= pedido.suminis
            pedido.save()

        try:
            codigo = pedido.item_cont
            codigo_ultima_letra=codigo[-1]
            if codigo_ultima_letra=='A' or codigo_ultima_letra=='P':
               pedido.item_cont= str(codigo[:-1])
               pedido.save()
                
        except:
            pass
        
        pagina=pedido.pagina

        if (pagina[6:9]!='100' and pedido.urbrur=='U') or (pagina[6:9]!='200' and pedido.urbrur=='R'):
            try:
                busquedad_tipo_pagina= Novedad_acta.objects.filter(pedido=pedido.pedido).filter(novedad='Tipo página').count()
                if busquedad_tipo_pagina==0:
                    novedad = "Tipo página"  
                    crear_novedad(pedido, novedad)

            except:
                pass
        
        if pedido.actividad=='AEJDO':
            if pedido.item_cont=='A 01':

                    try:
                        busquedad_a04= Acta.objects.filter(pedido=pedido.pedido).filter(item_cont='A 04').count()

                        if busquedad_a04==0:
                            novedad = "A 01=1, A 04=0"  
                            crear_novedad(pedido, novedad)        
                    except:
                        pass
                    
                    try:
                        busquedad_A23= Acta.objects.filter(pedido=pedido.pedido).filter(item_cont='A 23').count()
                        if busquedad_A23==0:
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
                    #busqueda_item(pedido, '215887', 0, nov) 
                    busqueda_item(pedido, '219404', 0, nov) 
                    calculo_incompatible_A01(pedido, nov)

        if pedido.actividad=='DSPRE':
            if pedido.tipre=='ENEPRE':
                calculo_enepre(pedido)

            if pedido.tipre=='ENESUB':
                calculo_enepre(pedido)
        
        if pedido.item_cont=='A 02':
            nov = "A 02=1,"
            busqueda_item(pedido, '211829', 0, nov)

        if pedido.item_cont=='211829':
            insumo= "211829"
            busqueda_insumo(pedido, insumo)
         

        if pedido.item_cont=='A 04':
            nov = "A 04=1,"
            busqueda_item(pedido, '210948', '210949', nov)
        
        if pedido.item_cont=='210947' or pedido.item_cont=='210948' or pedido.item_cont=='210949':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)

        if pedido.item_cont=='A 06':
            nov = "A 06=1,"
            busqueda_item(pedido, '200410', '200411', nov)  
        
        if pedido.item_cont=='200410' or pedido.item_cont=='200411':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)
                    
        if pedido.item_cont=='A 23':
            nov = "A 23=1,"
            busqueda_item(pedido, '211673', '210947', nov) 
        
        if pedido.item_cont=='211673':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)

        if pedido.item_cont=='A 24':
            nov = "A 24=1,"
            busqueda_item(pedido, '211357', 0, nov) 

        if pedido.item_cont=='211357':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)

        if pedido.item_cont=='A 25':
            nov = "A 25=1,"
            busqueda_item(pedido, '213333', 0, nov) 

        if pedido.item_cont=='213333':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)
        
        if pedido.item_cont=='A 34':
            nov = "A 34=1,"
            busqueda_item(pedido, '211686', 0, nov)
        
        if pedido.item_cont=='211686':
            insumo = str(pedido.item_cont)
            busqueda_insumo_por_item(pedido, insumo, 'A 34')

        if pedido.item_cont=='A 39':
            nov = "A 39=1,"
            busqueda_item(pedido, '200410', '200411', nov)
        
        if pedido.item_cont=='A 42':
            nov = "A 42=1,"
            busqueda_item(pedido, '200410', '200411', nov)

        if pedido.item_cont=='200092' or pedido.item_cont=='200093' or pedido.item_cont=='200098':
            insumo = str(pedido.item_cont)
            busqueda_insumo(pedido, insumo)

    novedades = Novedad_acta.objects.all()

    return render(request, "analisis.html", {'novedades':novedades})

def busqueda_insumo_por_item(pedido, insumo, item):
    try:
        pedidos = Acta.objects.filter(pedido=pedido)

        encontreinsumo=0
        for p in pedidos:
            letra = p.item_cont[0]
            if letra=='A':
                    
                if p.item_cont==item:
                    encontreinsumo=1

        if encontreinsumo==0:
            nov= insumo + ', insumo sin actividad'
            crear_novedad(pedido, nov)

                                 
    except:
        pass

def busqueda_insumo(pedido, insumo):
    try:
        pedidos = Acta.objects.filter(pedido=pedido)

        if insumo=='200092' or insumo=='200093' or insumo=='200098':
            encontreinsumo=0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra=='A':
                    
                    if p.item_cont=='A 03' or p.item_cont=='A 44' or p.item_cont=='A 01' or p.item_cont=='A 27':
                        encontreinsumo=1

            if encontreinsumo==0:
                        nov= insumo + ', insumo sin actividad'
                        crear_novedad(pedido, nov)

        if insumo=='211357':
            encontreinsumo=0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra=='A':
                    
                    if p.item_cont=='A 24' or p.item_cont=='A 01' :
                        encontreinsumo=1

            if encontreinsumo==0:
                        nov= insumo + ', insumo sin actividad'
                        crear_novedad(pedido, nov)
        
        if insumo=='213333':
            encontreinsumo=0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra=='A':
                    
                    if p.item_cont=='A 25' or p.item_cont=='A 01' :
                        encontreinsumo=1

            if encontreinsumo==0:
                        nov= insumo + ', insumo sin actividad'
                        crear_novedad(pedido, nov)

        if insumo=='211673':
            encontreinsumo=0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra=='A':
                    
                    if p.item_cont=='A 23':
                        encontreinsumo=1

            if encontreinsumo==0:
                        nov= insumo + ', insumo sin actividad'
                        crear_novedad(pedido, nov)

        if insumo=='200410' or insumo=='200411':
            encontreinsumo=0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra=='A':
                    
                    if p.item_cont=='A 06' or p.item_cont=='A 01' or p.item_cont=='A 39' or p.item_cont=='A 41' or p.item_cont=='A 42':
                        encontreinsumo=1

            if encontreinsumo==0:
                        nov= insumo + ', insumo sin actividad'
                        crear_novedad(pedido, nov)
        
        if insumo=='211829':
            encontreinsumo=0
            for p in pedidos:
                letra = p.item_cont[0]
                if letra=='A':
                    
                    if p.item_cont=='A 02' or p.item_cont=='A 27' or p.item_cont=='A 01':
                        encontreinsumo=1

            if encontreinsumo==0:
                        nov= insumo + ', insumo sin actividad'
                        crear_novedad(pedido, nov)

        if insumo=='210947':

            encontreinsumo=0

            for p in pedidos:
                letra = p.item_cont[0]

                if letra=='A':
                    if p.item_cont=='A 23':
                        encontreinsumo=1
            
            if encontreinsumo==0:
                        nov= insumo + ', insumo sin actividad'
                        crear_novedad(pedido, nov)

        if insumo=='210948' or insumo=='210949':

            encontreinsumo=0

            for p in pedidos:
                letra = p.item_cont[0]
                if letra=='C':
                    encontreinsumo=1
                if letra=='A':

                    if p.item_cont=='A 04' or p.item_cont=='A 01' or p.actividad=='ALEGA' or p.actividad=='ALECA' or p.actividad=='ALEGN' or p.actividad=='ACAMN':
                        encontreinsumo=1

            if encontreinsumo==0:
                        nov= insumo + ', insumo sin actividad'
                        crear_novedad(pedido, nov)
                                 
    except:
        pass

def busqueda_item(pedido, item, item2, novedad):

    if item=='210948':
        try:
            busquedad_210949= Acta.objects.filter(pedido=pedido.pedido).filter(item_cont=item).count()
            busquedad_210948= Acta.objects.filter(pedido=pedido.pedido).filter(item_cont='210949').count()

            if busquedad_210949==0 and busquedad_210948==0:
                novedad = novedad+" "+str(item)+"=0, 210949=0" 
                crear_novedad(pedido, novedad)
        except:
            pass
    elif pedido.item_cont=='A 42':
        try:
            busquedad_200410= Acta.objects.filter(pedido=pedido.pedido).filter(item_cont=item).count()
            busquedad_200411= Acta.objects.filter(pedido=pedido.pedido).filter(item_cont='200411').count()
            busquedad_200316= Acta.objects.filter(pedido=pedido.pedido).filter(item_cont='200316').count()

            if busquedad_200410==0 and busquedad_200411==0 and busquedad_200316==0:
                novedad = novedad+" "+str(item)+"=0, 200411=0, 200316=0 " 
                crear_novedad(pedido, novedad)
        except:
            pass

    elif item2 != 0:
        
        try:
            busquedad_1= Acta.objects.filter(pedido=pedido.pedido).filter(item_cont=item).count()
            busquedad_2= Acta.objects.filter(pedido=pedido.pedido).filter(item_cont=item2).count()

            if busquedad_1==0 and busquedad_2==0:
                novedad = novedad+" "+str(item)+"=0, " +str(item2)+"=0, " 
                crear_novedad(pedido, novedad)
        except:
            pass
    
    else:
        try:
            busquedad= Acta.objects.filter(pedido=pedido.pedido).filter(item_cont=item).count()
            if busquedad==0:
                novedad = novedad+" "+str(item)+"=0" 
                crear_novedad(pedido, novedad)
        except:
            pass

def calculo_incompatible_A01(pedido, novedad):
    try:
        pedidos =  Acta.objects.filter(pedido=pedido.pedido)
        cont=1
        for p in pedidos:
            letra = p.item_cont[0]
            if letra=='A':
                if p.item_cont!='A 01' and p.item_cont!='A 04' and p.item_cont!='A 23':
                    nov= 'A 01=1, '+ p.item_cont + ">0. Incompatibles."
                    crear_novedad(p, nov)
                
    except:
        pass

def calculo_incompatible_A27(pedido, novedad):
    try:
        pedidos =  Acta.objects.filter(pedido=pedido.pedido)
        cont=1
        for p in pedidos:
            letra = p.item_cont[0]
            if letra=='A':
                if p.item_cont=='A 02' or p.item_cont=='A 44' or p.item_cont=='A 03':
                    nov= 'A 27=1, '+ p.item_cont + ">0. Incompatibles."
                    crear_novedad(p, nov)                
    except:
        pass

def calculo_incompatible_A44(pedido, novedad):
    try:
        pedidos =  Acta.objects.filter(pedido=pedido.pedido)
        cont=1
        for p in pedidos:
            letra = p.item_cont[0]
            if letra=='A':
                if p.item_cont=='A 27' or p.item_cont=='A 03':
                    nov= 'A 44=1, '+ p.item_cont + ">0. Incompatibles."
                    crear_novedad(p, nov)                
    except:
        pass

def calculo_incompatible_A03(pedido, novedad):
    try:
        pedidos =  Acta.objects.filter(pedido=pedido.pedido)
        cont=1
        for p in pedidos:
            letra = p.item_cont[0]
            if letra=='A':
                if p.item_cont=='A 27' or p.item_cont=='A 44':
                    nov= 'A 03=1, '+ p.item_cont + ">0. Incompatibles."
                    crear_novedad(p, nov)                
    except:
        pass
        
def crear_novedad(pedido, nov):
    novedad = Novedad_acta()
    novedad.pedido = pedido.pedido
    novedad.actividad = pedido.actividad
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
    if pedido.item_cont=='A 03':
        try:
            novedad="A 03=1, "
            busqueda_item(pedido, 'A 28', 0, novedad)
            busqueda_item(pedido, 'A 29', 0, novedad)
            busqueda_item(pedido, '219404', 0, novedad) 
            busqueda_item(pedido, '220683',  0, novedad)  
            calculo_incompatible_A03(pedido, novedad)      
        except:
            pass
    
    if pedido.item_cont=='A 27':
        try:
            novedad="A 27=1, "
            busqueda_item(pedido, 'A 41', 0, novedad)
            busqueda_item(pedido, '219404', 0, novedad)    
            busqueda_item(pedido, 'A 10', 'A 11', novedad) 
            calculo_incompatible_A27(pedido, novedad)  
        except:
            pass
    
    if pedido.item_cont=='A 44':
        try:
            novedad="A 44=1, "
            busqueda_item(pedido, 'A 39', 0, novedad)    
            busqueda_item(pedido, 'A 40', 'A 41', novedad)  
            busqueda_item(pedido, '219404', 0, novedad) 
            calculo_incompatible_A44(pedido, novedad)

            pedidos =  Acta.objects.filter(pedido=pedido.pedido)

            encontre_A40=0
            encontre_A10=0
            encontre_A11=0
            encontre_riel=0

            for p in pedidos:
                if p.item_cont=='A 40':
                    encontre_A40=1
                if p.item_cont=='A 10':
                    encontre_A10=1
                if p.item_cont=='A 11':
                    encontre_A11=1
                if p.item_cont=='220683':
                    encontre_riel=1
            
            if encontre_A40==0 and encontre_A10==0 and encontre_A11==0:
                novedad= novedad+"A 10=0, A 11=0"
                crear_novedad(pedido, novedad)
            if encontre_A40==1:
                if encontre_A10==1 or encontre_A11==1:
                    novedad= novedad+"A 40 incompatible con A 10 y A 11"
                    crear_novedad(pedido, novedad)   
                if encontre_riel==1:
                    nov= "A 40 excluye riel (220683)."
                    crear_novedad(pedido, nov)                      

        except:
            pass


## aqui

def reiniciar(request):
    matfenix.objects.all().delete()
    matperseo.objects.all().delete()
    faltanteperseo.objects.all().delete()
    return redirect('novedades_acta')

def pedidos_fenix(request):
    perseo = matperseo.objects.all()
    fenix = matfenix.objects.all()
    pedidos_fenix=[]
    no=[]
    cont=0
    cont2=0
    for p in fenix:
        try:
            ped_f=matperseo.objects.get(pedido=p.pedido)
            if ped_f.pedido in pedidos_fenix:
                pass
            else:
                pedidos_fenix.append(ped_f.pedido)
                cont+=1
        except:
            if p.pedido in no:
                pass
            else:
                no.append(p.pedido)
                cont2+=1
    print("pedidos que no estan en perseo: " + str(len(no)))

    return HttpResponse("termino") #(request, 'index.html')

def concatenar(pedidos, indicador):
    con=1
    for p in pedidos:
        if indicador==1:
            try:
                nombre_cambio_codigo = Guia.objects.get(nombre_perseo=p.codigo)
                p.codigo = nombre_cambio_codigo.nombre_fenix
                p.save()

            except:
                pass
        my_str=p.codigo

        try:
            final_str=my_str[-1]
            if final_str=='A':
                p.codigo= str(my_str[:-1])
        except:
            pass       
        
        p.concatenacion = str(p.pedido + "-" + p.codigo)
        p.save()

def gestionar_bd_mat(request):
    pedidos_perseo = matperseo.objects.all()
    pedidos_fenix = matfenix.objects.all()

    concatenar(pedidos_fenix, 0)
    concatenar(pedidos_perseo, 1)

    return render(request, "index.html")

def calculo_faltantes_perseo(request):
    faltantes=[]
    pedidos_perseo = matperseo.objects.all()
    for pedido_perseo in pedidos_perseo:
        
        try:
            pedido_fenix = matfenix.objects.get(concatenacion=pedido_perseo.concatenacion)

            try:
                existe_faltante = faltanteperseo.objects.get(concatenacion = pedido_fenix.concatenacion)
                existe_faltante.cantidad= existe_faltante.cantidad + pedido_perseo.cantidad
                existe_faltante.diferencia = existe_faltante.cantidad - pedido_fenix.cantidad
                existe_faltante.save()

            except:
                if pedido_perseo.cantidad != pedido_fenix.cantidad:
                    faltante= faltanteperseo()
                    faltante.concatenacion = pedido_perseo.concatenacion
                    faltante.pedido = pedido_perseo.pedido
                    faltante.actividad = pedido_perseo.actividad
                    faltante.fecha = pedido_perseo.fecha
                    faltante.codigo = pedido_perseo.codigo
                    faltante.cantidad = pedido_perseo.cantidad
                    faltante.observacion = "Cantidad no coincide"
                    faltante.acta = pedido_perseo.acta
                    faltante.cantidad_fenix = pedido_fenix.cantidad
                    faltante.diferencia = pedido_perseo.cantidad - pedido_fenix.cantidad
                    faltante.save()        
        except:
            falt= faltanteperseo()
            falt.concatenacion = pedido_perseo.concatenacion
            falt.pedido = pedido_perseo.pedido
            falt.actividad = pedido_perseo.actividad
            falt.fecha = pedido_perseo.fecha
            falt.codigo = pedido_perseo.codigo
            falt.cantidad = pedido_perseo.cantidad
            falt.observacion = "No digitado en fenix"
            falt.acta = pedido_perseo.acta
            falt.diferencia = -9999
            falt.save()

        ped= faltanteperseo.objects.filter(diferencia=0)
        ped.delete()

    calculo_numero_acta()


    return render(request, "index.html")

def calculo_numero_acta():
    acta= NumeroActa.objects.first()
    pedidos_perseo = matperseo.objects.all()
    con=1
 
    for pedido_perseo in pedidos_perseo:
        try:
            if str(pedido_perseo.acta) != str(acta.numero):
                faltante= faltanteperseo()
                faltante.concatenacion = pedido_perseo.concatenacion
                faltante.pedido = pedido_perseo.pedido
                faltante.actividad = pedido_perseo.actividad
                faltante.fecha = pedido_perseo.fecha
                faltante.codigo = pedido_perseo.codigo
                faltante.cantidad = pedido_perseo.cantidad
                faltante.observacion = "Acta incorrecta"
                faltante.acta = pedido_perseo.acta
                faltante.diferencia = -9999
                faltante.save()                        
        except:
            print("error en el acta")



## CODIGO INVENTARIO BODEGA

def gestionar_acta_perseo_inventario(request):

        pedidos_perseo= Material_utilizado_perseo.objects.all()
        pedidos_epm=  Liquidacion_acta_epm.objects.all()

        for p in pedidos_perseo:
            try:

                codigo = p.codigo
                codigo_ultima_letra=codigo[-1]
                if codigo_ultima_letra=='A' or codigo_ultima_letra=='P':
                    p.codigo= str(codigo[:-1])  
                    p.save() 
            except:
                pass
            p.conc_pedido_codigo =  str(p.pedido)+"-"+str(p.codigo)
            p.save()
        cont=1
        for p in pedidos_epm:
            print("voy en epm: "+str(cont))
            cont+=1
            try:
                nombre_cambio_codigo = Guia.objects.get(nombre_fenix=p.item_cont)
                p.item_cont= nombre_cambio_codigo.nombre_perseo
                p.save()
               
            except:
                pass
            try:
                codigo = p.item_cont
                codigo_ultima_letra=codigo[-1]
                if codigo_ultima_letra=='A' or codigo_ultima_letra=='P':
                    p.item_cont= str(codigo[:-1])
                    p.save()
            except:
                pass
            p.conc_pedido_codigo =  str(p.pedido)+"-"+str(p.item_cont)          
            p.save()

            pedido_a_modificar = Material_utilizado_perseo.objects.filter(pedido = p)

            for ped in pedido_a_modificar:
                p.encargado= ped.instalador
                p.save()
                break 

        return render(request,  "index.html")

def calculo_inventario_por_oficial(request):

    try:
        
        for oficial in Oficial.objects.all()[:1]:
            inicio = 0
            despachado = 0
            epm = 0

            cantidad_inicial_inicio = Inicio.objects.filter(encargado= oficial)
           
            for cant_inicio in cantidad_inicial_inicio:
                codigo = cant_inicio.codigo
                inicio = cant_inicio.cantidad

                try:

                    cantidad_epm = Liquidacion_acta_epm.objects.filter(encargado= oficial)

                    for cant_epm in cantidad_epm:
                        print("codigo, " + str(codigo)+", item_cont, " + str(cant_epm.item_cont))
                        
                        if codigo== cant_epm.item_cont:
                            epm=cant_epm.cantidad
                            print(cant_inicio)
                            print("epm: " + str(epm))
                            

                except:
                    print("error 2")
    
    except:
        pass
        
    

    return render(request,  "index.html")



  


