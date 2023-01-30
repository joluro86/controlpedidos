from django.shortcuts import render
from django.http import HttpResponse
from openpyxl import load_workbook
from django.db.models import Q, Sum

from nominametro.models import plantilla, prenomina, Concepto

# Create your views here.

def subirnominametro(request):
    try:
        if request.method == 'POST':
            file = request.FILES['file']
            process_excel(file)
            return HttpResponse("File uploaded and processed!")
    except Exception as e:
            print(e)
    return render(request, 'subirarchivo.html')

def process_excel(file):

    try:
        wb = load_workbook(file)
        ws = wb[wb.sheetnames[0]]
        
        row_count = 0
        
        for row in ws.iter_rows():
            
            if row_count == 0:
                row_count += 1
                continue
            
            nomina_empleado = prenomina()
            
            nomina_empleado. centro_de_costos =  row[0].value
            nomina_empleado. nombre_del_centro_de_costos =  row[1].value
            nomina_empleado. empleado =  row[2].value
            nomina_empleado. nombre_del_empleado =  row[3].value
            nomina_empleado. turno =  row[4].value
            nomina_empleado. descripción_del_turno =  row[5].value

            nomina_empleado. concepto =  row[6].value
            
            
            try:
                nomina_empleado.conversor = buscar_conversor(row[6].value)
                
                concepto = buscar_conversor(row[6].value)
            except Exception as e:
                print(row[6].value + " " + str(e))

            nomina_empleado. nombre_del_concepto =  row[7].value
            nomina_empleado. vinculación =  row[8].value
            nomina_empleado. préstamo =  row[9].value
            nomina_empleado. salario_básico_hora =  row[10].value
            nomina_empleado. tiempo =  row[11].value
            nomina_empleado. valor =  row[12].value
            
            nomina_empleado.save()
    except Exception as e:
            print(e)

def buscar_conversor(concepto):
    conversor = Concepto.objects.filter(concepto=concepto).first()
    conversor = conversor.conversor
    return conversor


def definir_fechas(request):
    return render(request, 'fecha_inicial_final.html')

def gestionar_prenomina(request):

    if request.method == 'POST':
        fecha_inicial = request.POST['fecha_inicial']
        fecha_final = request.POST['fecha_final']

        print(fecha_inicial)
        print(fecha_final)
    
        empleados = prenomina.objects.values_list('empleado').distinct()

        cont=1
        for e in empleados.order_by('empleado'):
            print(cont)
            cont+=1

            empleado = prenomina.objects.filter(empleado=e[0]).first()
            print(empleado.nombre_del_empleado)

            emplea=e[0]         
            
            nomina_empleado = plantilla()
            nomina_empleado.cedula = empleado.empleado
            nomina_empleado.nombre = empleado.nombre_del_empleado
            nomina_empleado.apellido = empleado.nombre_del_empleado
            nomina_empleado.periodo_fecha_inicial = fecha_inicial
            nomina_empleado.periodo_fecha_final = fecha_final
            nomina_empleado.valor_hora_ordin = empleado.salario_básico_hora            

            horas_ordinarias = calculo_horas(emplea, 100)
            if horas_ordinarias['suma'] is not None:
                nomina_empleado.horas_ordinarias = horas_ordinarias['suma']
            else: nomina_empleado.horas_ordinarias = 0

            on_0_35 = calculo_horas(emplea, 200)
            if on_0_35['suma'] is not None:
                nomina_empleado.on_0_35  = on_0_35['suma']
            else: nomina_empleado.on_0_35 = 0

            ed_1_25 = calculo_horas(emplea, 300)
            if ed_1_25['suma'] is not None:
                nomina_empleado.ed_1_25  = ed_1_25['suma']
            else: nomina_empleado.ed_1_25 = 0

            en_1_75 = calculo_horas(emplea, 400)
            if en_1_75['suma'] is not None:
                nomina_empleado.en_1_75  = en_1_75['suma']
            else: nomina_empleado.en_1_75 = 0

            fd_0_75 = calculo_horas(emplea, 500)
            if fd_0_75['suma'] is not None:
                nomina_empleado.fd_0_75  = fd_0_75['suma']
            else: nomina_empleado.fd_0_75 = 0

            fn_1_1 = calculo_horas(emplea, 600)
            if fn_1_1['suma'] is not None:
                nomina_empleado.fn_1_1  = fn_1_1['suma']
            else: nomina_empleado.fn_1_1 = 0

            efd_2 = calculo_horas(emplea, 700)
            if efd_2['suma'] is not None:
                nomina_empleado.efd_2  = efd_2['suma']
            else: nomina_empleado.efd_2 = 0

            efn_2_5 = calculo_horas(emplea, 800)
            if efn_2_5['suma'] is not None:
                nomina_empleado.efn_2_5  = efn_2_5['suma']
            else: nomina_empleado.efn_2_5 = 0

            d_o_f_d_1_75 = calculo_horas(emplea, 900)
            if d_o_f_d_1_75['suma'] is not None:
                nomina_empleado.d_o_f_d_1_75  = d_o_f_d_1_75['suma']
            else: nomina_empleado.d_o_f_d_1_75 = 0

            d_o_f_n_2_1 = calculo_horas(emplea, 1000)
            if d_o_f_n_2_1['suma'] is not None:
                nomina_empleado.d_o_f_n_2_1  = d_o_f_n_2_1['suma']
            else: nomina_empleado.d_o_f_n_2_1 = 0

            ausencias_remuneradas_hora = calculo_horas(emplea, 1100)
            if ausencias_remuneradas_hora['suma'] is not None:
                nomina_empleado.ausencias_remuneradas_hora  = ausencias_remuneradas_hora['suma']
            else: nomina_empleado.ausencias_remuneradas_hora = 0

            ausencias_no_remuneradas_hora = calculo_horas(emplea, 1200)
            if ausencias_no_remuneradas_hora['suma'] is not None:
                nomina_empleado.ausencias_no_remuneradas_hora  = ausencias_no_remuneradas_hora['suma']
            else: nomina_empleado.ausencias_no_remuneradas_hora = 0

            incapacidad_por_enfermedad_general_horas = calculo_horas(emplea, 1300)
            if incapacidad_por_enfermedad_general_horas['suma'] is not None:
                nomina_empleado.incapacidad_por_enfermedad_general_horas  = incapacidad_por_enfermedad_general_horas['suma']
            else: nomina_empleado.incapacidad_por_enfermedad_general_horas = 0

            nomina_empleado.save()

    return HttpResponse("Informe procesado!")

def reiniciar_prenomina(request):
    prenomina.objects.all().delete()
    return render(request, 'subirarchivo.html')

def calculo_horas(empleado, conversor):

    horas = prenomina.objects.filter(empleado=empleado).filter(conversor = conversor).aggregate(suma=Sum('tiempo'))

    return horas
