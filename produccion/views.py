from django.shortcuts import render, redirect
from django.views import View
from .models import Perseo_produccion, NovedadProduccion, Dia_dia, Valor_referencia
from .forms import ImportDataForm, ValorReferenciaForm
import pandas as pd
from django.db.models import Sum, Q, F, Value, DecimalField
from django.db.models.functions import Coalesce
from decimal import Decimal
from django.shortcuts import render
from django.db.models.fields import DecimalField 

def dia_dia(request):
    producido = Dia_dia.objects.all()
    return render(request, 'producido.html', {'producido':producido})

def import_data_success(request):
    return render(request, 'import_data_success.html')

def reiniciar(request):
    NovedadProduccion.objects.all().delete()
    Perseo_produccion.objects.all().delete()
    Dia_dia.objects.all().delete()
    
    return render(request, 'producido.html')

def reiniciar_novedades(request):
    NovedadProduccion.objects.all().delete()
    return render(request, 'novedades.html')

def novedades(request):
    novedades = NovedadProduccion.objects.all()
    print(len(novedades))
    
    return render(request, 'novedades.html', {"novedades": novedades})   

def valor_referencia_success(request):
    return render(request, 'valor_referencia_success.html')
    
class ValorReferenciaView(View):
    template_name = 'valor_referencia.html'

    def get(self, request):
        # Obtener el primer registro o crear uno si no existe
        valor_referencia, created = Valor_referencia.objects.get_or_create(id=1, defaults={'valor': 0})
        
        form = ValorReferenciaForm(instance=valor_referencia)
        valor_actual = Valor_referencia.objects.filter(id=1).first()
        return render(request, self.template_name, {'form': form, 'valor_actual': valor_actual})

    def post(self, request):
        valor_referencia = Valor_referencia.objects.get(id=1)  # Obtener el registro con ID 1

        form = ValorReferenciaForm(request.POST, instance=valor_referencia)
        if form.is_valid():
            form.save()
            return redirect('valor_referencia_success')

        # Obtener el valor actual para mostrarlo en caso de error
        valor_actual = Valor_referencia.objects.filter(id=1).first()
        return render(request, self.template_name, {'form': form, 'valor_actual': valor_actual})
    
class ImportDataView(View):
    template_name = 'import_data.html'

    def get(self, request):
        form = ImportDataForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ImportDataForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['Archivo_de_datos']
            df = pd.read_excel(excel_file)

            # Guardar los datos del Excel en la base de datos
            for index, row in df.iterrows():
                Perseo_produccion.objects.create(
                    pedido=row['pedido'],
                    actividad=row['actividad'],
                    instalador=row['instalador'],
                    fecha=row['fecha'],
                    codigo=row['codigo'],
                    cantidad=row['cantidad'],
                    valor=row['valor'],
                    total=row['total'],
                    acta=row['acta'],
                )

            # Verificar duplicados después de haber guardado todos los datos
            check_duplicate_dates()
            pedidos_interna()
            verificar_material_con_B03()
            verificar_material_con_B04()
            verificar_material_con_B06()
            verificar_material_con_B07()
            verificar_material_con_B08()
            actualizar_dia_dia()

            return redirect('novedades')

        return render(request, self.template_name, {'form': form})

def check_duplicate_dates():
    """
    Esta función verifica si hay más de una fecha asociada al mismo pedido y, en caso afirmativo, crea una novedad.
    Además, verifica si la actividad es 'HV+INTERNA' y si tiene los códigos 'B03', 'B04', 'B06', 'B07'.
    """
    all_pedidos = Perseo_produccion.objects.values_list('pedido', flat=True).distinct()

    for pedido in all_pedidos:
        dates_for_pedido = Perseo_produccion.objects.filter(pedido=pedido).values_list('fecha', flat=True).distinct()

        if len(dates_for_pedido) > 1:
            NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad=f'Más de una fecha para el pedido {pedido}')

def pedidos_interna():
        hv_interna_records = Perseo_produccion.objects.filter(actividad='HV+INTERNA').values_list('pedido', flat=True).distinct()
        print('con interna')
        print(len(hv_interna_records))
        for hv in hv_interna_records:
            
            registros= Perseo_produccion.objects.filter(pedido=hv, codigo__startswith='B')
            
            B03= False
            B04=False
            B06=False
            B07=False
            
            total_registros = len(registros)

            for i, p in enumerate(registros):
                if p.codigo == "B-03":
                    B03 = True
                if p.codigo == "B-04":
                    B04 = True
                if p.codigo == "B-06":
                    B06 = True
                if p.codigo == "B-07":
                    B07 = True
                
                if i == total_registros - 1:   
                                     
                    if B03 == False: 
                        NovedadProduccion.objects.create(pedido=p, novedad=f'Interna sin B03')
                        
                    if B04 == False: 
                        NovedadProduccion.objects.create(pedido=p, novedad=f'Interna sin B04')
                    
                    if B06 == False: 
                        NovedadProduccion.objects.create(pedido=p, novedad=f'Interna sin B06')
                    
                    if B07 == False: 
                        NovedadProduccion.objects.create(pedido=p, novedad=f'Interna sin B07')
                
def verificar_material_con_B03():
    from django.db.models import Sum

    # Obtener todos los pedidos con el código 'B-03'
    pedidos_B03 = Perseo_produccion.objects.filter(codigo='B-03').values_list('pedido', flat=True).distinct()

    for pedido in pedidos_B03:
        # Verificar si hay registros con el código 'M2419' para el mismo pedido
        has_M2419 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M2419').exists()

        if not has_M2419:
            NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad='B03 sin M2419')
        else:
            # Verificar si la cantidad de 'M2419' no coincide con la cantidad de 'B-03'
            cantidad_B03 = Perseo_produccion.objects.filter(pedido=pedido, codigo='B-03').aggregate(total=Sum('cantidad'))['total']
            cantidad_M2419 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M2419').aggregate(total=Sum('cantidad'))['total']

            # Manejar el caso en que la suma sea None
            if cantidad_B03 is None:
                cantidad_B03 = 0

            if cantidad_M2419 is None:
                cantidad_M2419 = 0

            if cantidad_M2419 != cantidad_B03:
                NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad='Cantidad de M2419 no coincide con la de B-03')

def verificar_material_con_B04():
    from django.db.models import Sum

    # Obtener todos los pedidos con el código 'B-04'
    pedidos_B04 = Perseo_produccion.objects.filter(codigo='B-04').values_list('pedido', flat=True).distinct()

    for pedido in pedidos_B04:
        # Verificar si hay registros con los códigos 'M070', 'M071' o 'M072' para el mismo pedido
        has_M070 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M070').exists()
        has_M071 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M071').exists()
        has_M072 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M072').exists()

        if not (has_M070 or has_M071 or has_M072):
            NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad='B-04 sin M070, M071 ni M072')
        else:
            # Verificar si la cantidad de 'M070', 'M071' o 'M072' no coincide con la cantidad de 'B-04'
            cantidad_B04 = Perseo_produccion.objects.filter(pedido=pedido, codigo='B-04').aggregate(total=Sum('cantidad'))['total']
            cantidad_M070 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M070').aggregate(total=Sum('cantidad'))['total']
            cantidad_M071 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M071').aggregate(total=Sum('cantidad'))['total']
            cantidad_M072 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M072').aggregate(total=Sum('cantidad'))['total']

            # Manejar el caso en que la suma sea None
            if cantidad_B04 is None:
                cantidad_B04 = 0

            if cantidad_M070 is None:
                cantidad_M070 = 0

            if cantidad_M071 is None:
                cantidad_M071 = 0

            if cantidad_M072 is None:
                cantidad_M072 = 0

            if (cantidad_M070 + cantidad_M071 + cantidad_M072) != cantidad_B04:
                NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad='Cantidad de M070, M071 y M072 no coincide con la de B-04')

def verificar_material_con_B06():
    from django.db.models import Sum

    # Obtener todos los pedidos con el código 'B-03'
    pedidos_B06 = Perseo_produccion.objects.filter(codigo='B-06').values_list('pedido', flat=True).distinct()

    for pedido in pedidos_B06:
        # Verificar si hay registros con el código 'M2419' para el mismo pedido
        has_M385 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M385').exists()

        if not has_M385:
            NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad='B06 sin M385')
        else:
            # Verificar si la cantidad de 'M2419' no coincide con la cantidad de 'B-06'
            cantidad_B06 = Perseo_produccion.objects.filter(pedido=pedido, codigo='B-06').aggregate(total=Sum('cantidad'))['total']
            cantidad_M385 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M385').aggregate(total=Sum('cantidad'))['total']

            # Manejar el caso en que la suma sea None
            if cantidad_B06 is None:
                cantidad_B06 = 0

            if cantidad_M385 is None:
                cantidad_M385 = 0

            if cantidad_M385 != cantidad_B06:
                NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad='Cantidad de M385 no coincide con la de B-06')

def verificar_material_con_B07():
    from django.db.models import Sum

    # Obtener todos los pedidos con el código 'B-03'
    pedidos_B07 = Perseo_produccion.objects.filter(codigo='B-07').values_list('pedido', flat=True).distinct()

    for pedido in pedidos_B07:
        # Verificar si hay registros con el código 'M2419' para el mismo pedido
        has_M947 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M947').exists()

        if not has_M947:
            NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad='B07 sin M947')
        else:
            # Verificar si la cantidad de 'M2419' no coincide con la cantidad de 'B-03'
            cantidad_B07 = Perseo_produccion.objects.filter(pedido=pedido, codigo='B-07').aggregate(total=Sum('cantidad'))['total']
            cantidad_M947 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M947').aggregate(total=Sum('cantidad'))['total']

            # Manejar el caso en que la suma sea None
            if cantidad_B07 is None:
                cantidad_B07 = 0

            if cantidad_M947 is None:
                cantidad_M947 = 0

            if cantidad_M947 != cantidad_B07:
                NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad='Cantidad de M947 no coincide con la de B-07')

def verificar_material_con_B08():
    from django.db.models import Sum

    # Obtener todos los pedidos con el código 'B-03'
    pedidos_B08 = Perseo_produccion.objects.filter(codigo='B-08').values_list('pedido', flat=True).distinct()

    for pedido in pedidos_B08:
        # Verificar si hay registros con el código 'M2419' para el mismo pedido
        has_M5097 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M5097').exists()

        if not has_M5097:
            NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad='B08 sin M5097')
        else:
            # Verificar si la cantidad de 'M2419' no coincide con la cantidad de 'B-03'
            cantidad_B08 = Perseo_produccion.objects.filter(pedido=pedido, codigo='B-08').aggregate(total=Sum('cantidad'))['total']
            cantidad_M5097 = Perseo_produccion.objects.filter(pedido=pedido, codigo='M5097').aggregate(total=Sum('cantidad'))['total']

            # Manejar el caso en que la suma sea None
            if cantidad_B08 is None:
                cantidad_B08 = 0

            if cantidad_M5097 is None:
                cantidad_M5097 = 0

            if cantidad_M5097 != cantidad_B08:
                NovedadProduccion.objects.create(pedido=Perseo_produccion.objects.filter(pedido=pedido).first(), novedad='Cantidad de M5097 no coincide con la de B-08')

def actualizar_dia_dia():
    

        # Obtener todos los instaladores y fechas únicas de Perseo_produccion
        instaladores_fechas = Perseo_produccion.objects.values('instalador', 'fecha').distinct()

        for instalador_fecha in instaladores_fechas:
            instalador = instalador_fecha['instalador']
            fecha = instalador_fecha['fecha']
            treinta_porciento=0
            por_persona=0

            # Obtener las cantidades sumadas para cada instalador y fecha
            suma_mano_obra = Perseo_produccion.objects.filter(
                Q(instalador=instalador, fecha=fecha, codigo__startswith='A') |
                Q(instalador=instalador, fecha=fecha, codigo__startswith='B') |
                Q(instalador=instalador, fecha=fecha, codigo__startswith='C')
            ).aggregate(suma_mano_obra=Sum(F('total'), output_field=DecimalField()) + Value(0, output_field=DecimalField()))['suma_mano_obra']            
            
            print(Perseo_produccion._meta.get_field('total').get_internal_type())

            suma_materiales = Perseo_produccion.objects.filter(
                instalador=instalador, fecha=fecha
            ).exclude(
                Q(codigo__startswith='A') | Q(codigo__startswith='B') | Q(codigo__startswith='2') | Q(codigo__startswith='C')
            ).aggregate(suma_materiales=Sum(F('total'), output_field=DecimalField()) + Value(0, output_field=DecimalField()))['suma_materiales']
            
            # Verificar si alguno de los valores es None y asignar un valor predeterminado
            suma_mano_obra = suma_mano_obra if suma_mano_obra is not None else Decimal('0.0')
            suma_materiales = suma_materiales if suma_materiales is not None else Decimal('0.0')

            # Calcular el producido como la diferencia entre la mano de obra y los materiales
            producido = suma_mano_obra - suma_materiales            
                        
            # Valor fijo para referencia
            valor_referencia_actual = Valor_referencia.objects.first()  

            # Calcular el valor producido por persona
            if suma_mano_obra != 0:       
                            
                # Calcular el 30% del producido
                treinta_porciento = (producido - valor_referencia_actual.valor) * Decimal('0.3')
                por_persona = treinta_porciento / 3
            
            # Crear o actualizar el registro en Dia_dia
            dia_dia, created = Dia_dia.objects.get_or_create(instalador=instalador, fecha=fecha)
            dia_dia.mano_obra = suma_mano_obra
            dia_dia.materiales = suma_materiales
            dia_dia.valor_referencia = valor_referencia_actual.valor
            dia_dia.producido = producido
            dia_dia.treinta_porciento = treinta_porciento
            dia_dia.por_persona = por_persona
            dia_dia.save()  
              
     
 
def bonificacion_prod(request):
    # Obtener la lista de instaladores (oficiales)
    instaladores = Dia_dia.objects.values('instalador').distinct()

    informe_data = []

    for instalador in instaladores:
        # Obtener los registros de Dia_dia para cada instalador
        registros_instalador = Dia_dia.objects.filter(instalador=instalador['instalador'])

        # Calcular la cantidad de días laborados
        dias_laborados = registros_instalador.count()

        # Calcular la suma de la mano de obra y valor materiales
        suma_mano_obra = registros_instalador.aggregate(suma_mano_obra=Sum('mano_obra'))['suma_mano_obra'] or Decimal('0')
        suma_materiales = registros_instalador.aggregate(suma_materiales=Sum('materiales'))['suma_materiales'] or Decimal('0')

        # Obtener el valor de referencia actual (supongamos que solo hay un registro)
        valor_referencia = Valor_referencia.objects.first()
        
        # Calcular la meta
        meta = dias_laborados * valor_referencia.valor

        # Calcular la suma del producido
        suma_producido = registros_instalador.aggregate(suma_producido=Sum('producido'))['suma_producido'] or Decimal('0')

        # Calcular el 30%
        treinta_porciento = suma_producido - meta

        # Calcular Por persona
        por_persona = treinta_porciento / 3

        # Crear un diccionario con los datos para este instalador
        instalador_data = {
            'instalador': instalador['instalador'],
            'dias': dias_laborados,
            'mano_obra': suma_mano_obra,
            'materiales': suma_materiales,
            'meta': meta,
            'producido': suma_producido,
            'treinta_porciento': treinta_porciento,
            'por_persona': por_persona,
        }

        informe_data.append(instalador_data)
        
        print(informe_data)

    return render(request, 'bonificaciones_prod.html', {'bonificaciones': informe_data})