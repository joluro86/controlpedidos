from django.shortcuts import render, redirect
from django.http import HttpResponse
from openpyxl import load_workbook
from django.db.models import Sum

from nominametro.models import Novedad_nomina, plantilla, prenomina, Concepto


def subirnominametro(request):
    try:
        if request.method == 'POST':
            file = request.FILES['file']
            process_excel(file)
            return render(request, 'fecha_inicial_final.html')
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

            nomina_empleado. centro_de_costos = row[0].value
            nomina_empleado. nombre_del_centro_de_costos = row[1].value
            nomina_empleado. empleado = row[2].value
            nomina_empleado. nombre_del_empleado = row[3].value
            nomina_empleado. turno = row[4].value
            nomina_empleado. descripción_del_turno = row[5].value

            nomina_empleado. concepto = row[6].value

            try:
                nomina_empleado.conversor = buscar_conversor(row[6].value)
                tipo_ingreso = Concepto.objects.filter(
                    concepto=row[6].value).first()
                nomina_empleado. tipo = tipo_ingreso.tipo
                nomina_empleado. factor = tipo_ingreso.factor

            except Exception as e:
                novedad = Novedad_nomina()
                novedad.empleado = nomina_empleado.empleado
                novedad.novedad = str(e)
                novedad.save()

            nomina_empleado. nombre_del_concepto = row[7].value
            nomina_empleado. vinculación = row[8].value
            nomina_empleado. préstamo = row[9].value
            nomina_empleado. salario_básico_hora = row[10].value
            nomina_empleado. tiempo = row[11].value
            nomina_empleado. valor = row[12].value

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

        empleados = prenomina.objects.values_list('empleado').distinct()

        cont = 1

        valorhoras = 0
        for e in empleados.order_by('empleado'):
            cont += 1

            empleado = prenomina.objects.filter(empleado=e[0]).first()

            emplea = e[0]

            nomina_empleado = plantilla()
            nomina_empleado.cedula = empleado.empleado
            nomina_empleado.nombre = empleado.nombre_del_empleado
            nomina_empleado.apellido = empleado.nombre_del_empleado
            nomina_empleado.periodo_fecha_inicial = fecha_inicial
            nomina_empleado.periodo_fecha_final = fecha_final
            nomina_empleado.valor_hora_ordin = empleado.salario_básico_hora

            horas_ordinarias = calculo_horas(emplea, 100)
            nomina_empleado.horas_ordinarias = horas_ordinarias

            on_0_35 = calculo_horas(emplea, 200)
            nomina_empleado.on_0_35 = on_0_35

            ed_1_25 = calculo_horas(emplea, 300)
            nomina_empleado.ed_1_25 = ed_1_25

            en_1_75 = calculo_horas(emplea, 400)
            nomina_empleado.en_1_75 = en_1_75

            fd_0_75 = calculo_horas(emplea, 500)
            nomina_empleado.fd_0_75 = fd_0_75

            fn_1_1 = calculo_horas(emplea, 600)
            nomina_empleado.fn_1_1 = fn_1_1

            efd_2 = calculo_horas(emplea, 700)
            nomina_empleado.efd_2 = efd_2

            efn_2_5 = calculo_horas(emplea, 800)
            nomina_empleado.efn_2_5 = efn_2_5

            d_o_f_d_1_75 = calculo_horas(emplea, 900)
            nomina_empleado.d_o_f_d_1_75 = d_o_f_d_1_75

            d_o_f_n_2_1 = calculo_horas(emplea, 1000)
            nomina_empleado.d_o_f_n_2_1 = d_o_f_n_2_1

            ausencias_remuneradas_hora = calculo_horas(emplea, 1100)
            nomina_empleado.ausencias_remuneradas_hora = ausencias_remuneradas_hora

            ausencias_no_remuneradas_hora = calculo_horas(emplea, 1200)
            nomina_empleado.ausencias_no_remuneradas_hora = ausencias_no_remuneradas_hora

            incapacidad_por_enfermedad_general_horas = calculo_horas(
                emplea, 1300)
            nomina_empleado.incapacidad_por_enfermedad_general_horas = incapacidad_por_enfermedad_general_horas

            vr_auxilio_transporte_o_auxilio_de_conectividad = calculo_valor(
                emplea, 1400)
            nomina_empleado.vr_auxilio_transporte_o_auxilio_de_conectividad = vr_auxilio_transporte_o_auxilio_de_conectividad

            otros_ingresos_no_prestacionales = calculo_valor(emplea, 1500)
            nomina_empleado.otros_ingresos_no_prestacionales = otros_ingresos_no_prestacionales

            otros_ingresos_prestacionales = calculo_valor(emplea, 1900)
            nomina_empleado.otros_ingresos_prestacionales = otros_ingresos_prestacionales

            nomina_empleado.total_devengado = calculo_devengado(empleado)

            nomina_empleado.deducción_retención_en_la_fuente = calculo_valor(
                empleado, 1600)

            nomina_empleado.otras_deducciones = calculo_valor(emplea, 1700)

            nomina_empleado.deducciones_sgss = calculo_valor(emplea, 1800)

            nomina_empleado.neto_a_pagar = calculo_neto_a_pagar(emplea)

            nomina_empleado.save()

    return redirect('informe')


def reiniciar_prenomina(request):
    prenomina.objects.all().delete()
    plantilla.objects.all().delete()
    Novedad_nomina.objects.all().delete()
    return redirect('informe')


def calculo_horas(empleado, conversor):

    horas = prenomina.objects.filter(empleado=empleado).filter(
        conversor=conversor).aggregate(suma=Sum('tiempo'))

    if horas['suma'] is None:
        horas = 0
    else:
        horas = horas['suma']

    return horas


def calculo_valor(empleado, conversor):

    valor = prenomina.objects.filter(empleado=empleado).filter(
        conversor=conversor).aggregate(suma=Sum('valor'))

    if valor['suma'] is None:
        valor = 0
    else:
        valor = valor['suma']

    return valor


def calculo_devengado(empleado):
    valor = prenomina.objects.filter(empleado=empleado)\
        .filter(tipo='devengado').aggregate(devengado=Sum('valor'))
    devengado = valor['devengado']

    return devengado


def calculo_neto_a_pagar(empleado):
    valor = prenomina.objects.filter(empleado=empleado)\
        .filter(tipo='devengado').aggregate(devengado=Sum('valor'))

    deduccion = prenomina.objects.filter(empleado=empleado)\
                                 .filter(tipo='deduccion').aggregate(deduccion=Sum('valor'))

    if deduccion['deduccion'] is None:
        deduccion['deduccion'] = 0
    if valor['devengado'] is None:
        valor['devengado'] = 0

    neto_a_pagar = float(valor['devengado'])-float(deduccion['deduccion'])

    return neto_a_pagar


def informe(request):
    informe = plantilla.objects.all()
    return render(request, 'informe.html', {'informe':informe})
