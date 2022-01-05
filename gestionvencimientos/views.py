from datetime import date, datetime, timedelta
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import holidays_co
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User, auth
from controlpedidos import settings
from gestionvencimientos.models import Actividad, Ans, Encargado, Municipio, Vencido


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

    return lunes

@login_required
def menu_pendientes(self):
    id_dia = calculo_dia_actutal()+1;
    
    return redirect('pendientes', id_dia)

@login_required
def limpiar_base(request):
    lista_ans = []
    aneses = Ans.objects.all()

    for ans in aneses:
        if ans.Subzona != "Uraba":
            ans.delete()
        elif ans.Area_Operativa == "NOR-ENE" and ans.Actividad == "ACREV":
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

@login_required
def busqueda_vencidos(request):
    aneses = Ans.objects.filter(Estado="PENDI")
    list_ans = []
    for ans in aneses:
        if ans.Estado == "PENDI" and ans.Concepto == "PENDI":
            continue
        if ans.Estado == "PENDI" and ans.Concepto == "592":
            continue
        try:
            fecha_vence_ans = datetime.strptime(ans.fecha_vencimiento, "%Y-%m-%d")
            if fecha_vence_ans < datetime.today():
                if ans.estado_cierre == 0:
                    list_ans.append(ans)
                    
        except:
            print("An exception occurred in fecha vencimiento 2")        

    return render(request, "vencidos-todos.html" , {"aneses": list_ans})


def busqueda_pendientes(fecha_vence_buscar):
    aneses = Ans.objects.filter(Estado="PENDI")
    cont=0
    list_ans = []
    cont = 0
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
        except:
            print("An exception occurred in fecha vencimiento 2")        

    return list_ans


def eliminar_bd(request):
    Ans.objects.all().delete()

    return redirect('home')


def fechas(fecha_inic, dias):

    fecha_vencimiento = datetime. strptime(fecha_inic, '%Y/%m/%d %H:%M:%S')
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

@login_required
def gestion_bd(request):
    
    lista_ans = []
    Ans.objects.filter(Estado ="ANULA").delete()
    BORRAR = Ans.objects.filter(Estado = "PENDI").filter(Concepto = "PENDI").delete()
    
    anses = Ans.objects.all()
        
    for ans in anses:
        if ans.Area_Operativa == "NOR-ENE" and ans.Actividad == "ACREV":
            ans.delete()

        elif ans.Actividad != "ACREV" and ans.Actividad != "AEJDO" and ans.Actividad != "ARTER" and ans.Actividad != "DIPRE" and ans.Actividad != "INPRE" and ans.Actividad != "REEQU" and ans.Actividad != "APLIN" and ans.Actividad != "ALEGA" and ans.Actividad != "ALEGN" and ans.Actividad != "ALECA" and ans.Actividad != "ACAMN" and ans.Actividad != "AMRTR":
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
            if ans.Tipo_Dirección == "Urbano":
                ans.dias_vencimiento = int(actividad.dias_urbano)
            if ans.Tipo_Dirección == "Rural":
                ans.dias_vencimiento = int(actividad.dias_rural)

            ans.fecha_vencimiento = (fechas(ans.Fecha_Inicio_ANS, ans.dias_vencimiento))
            ans.fecha_vence= ((fechas(ans.Fecha_Inicio_ANS, ans.dias_vencimiento)).date()).strftime("%d/%m/%Y")
            
            ans.hora_vencimiento = (fechas(ans.Fecha_Inicio_ANS, ans.dias_vencimiento)).time()
            
            dias_ans = ans.Días_ANS
            dias = round(float(dias_ans), 2)            
            ans.Días_ANS = str(dias)
            
            ans.encargado = str(actividad.encargado)

            ans.save()

        except:
            print("An exception occurred")

    return redirect('home')

@login_required
def cerrar_pedido(request, id_pedido, fecha_cierre, hora_cierre):
   
    fecha_hora_cierre = fecha_cierre+" "+hora_cierre+":00";
    fecha_hora_cierre_final =datetime.strptime(fecha_hora_cierre, "%Y-%m-%d %H:%M:%S")
    
    ans_cerrar = Ans.objects.get(id=id_pedido)
    
    if datetime.strptime(ans_cerrar.fecha_vencimiento, "%Y-%m-%d %H:%M:%S")<fecha_hora_cierre_final:
        try:    
            ans_vencida = Vencido(
            Pedido = ans_cerrar.Pedido,
            Instalación = ans_cerrar.Instalación,
            Actividad = ans_cerrar.Actividad,
            Observación = "Aun nada",
            fecha_vencimiento = ans_cerrar.fecha_vencimiento,
            encargado = ans_cerrar.encargado,
            fecha_cierre = fecha_hora_cierre_final            
            )
            ans_vencida.save()
        except:
            print("bien hecho")

    ans_cerrar.estado_cierre = 1
    ans_cerrar.save()

    return redirect('menu_pendientes')

@login_required
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

@login_required
def vencidos(request):
    aeneses = Vencido.objects.all()
    
    return render(request, "vencidos.html", {"aneses":aeneses})

@login_required
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

@login_required
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

@login_required
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

@login_required
def acrev(request):
    
    aeneses = Ans.objects.filter(Actividad = "ACREV").filter(Q(Estado="PENDI") | Q(Concepto="406") | Q(Concepto="414")| Q(Concepto="495"))
    
    return render(request, "acrev.html", {"aneses": aeneses} )

@login_required
def amrtr(request):
    
    aeneses = Ans.objects.filter(Actividad = "AMRTR").filter(Q(Estado="PENDI") | Q(Concepto="406") | Q(Concepto="414")| Q(Concepto="495"))
    
    return render(request, "amrtr.html", {"aneses": aeneses} )

@login_required
def lega(request):
    
    aeneses = Ans.objects.filter(Q(Actividad="ALEGA") | Q(Actividad="ALEGN") | Q(Actividad="ALECA") |Q(Actividad="ACAMN") ).filter(Q(Estado="PENDI") | Q(Concepto="406") | Q(Concepto="414")| Q(Concepto="495"))
    
    return render(request, "lega.html", {"aneses": aeneses} )

@login_required
def direccionamiento(request):
    
    aeneses = Ans.objects.filter(Q(Actividad="ACREV")).filter(Tipo_Dirección = "Urbano").filter(Concepto = "PPRG")
    
    return render(request, "direccionamiento.html", {"aneses": aeneses} )

@login_required
def jorge_wolf(request):
    ans = Ans.objects.filter(Observación_Solicitud__contains='JWOLFV')
    
    return HttpResponse(len(ans))