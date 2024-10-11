from django.shortcuts import render, redirect
from django.contrib import messages
import openpyxl
from .models import Pedido, ActaB, MaterialSeleccionado


def formulario_subir_pedido(request):
    return render(request, 'formulario_subir_perseo.html')  # Asegúrate de usar el nombre correcto del template

def formulario_subir_acta(request):
    return render(request, 'formulario_subir_acta.html')  # Asegúrate de usar el nombre correcto del template


def subir_material_mejia(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        
        if not file:
            messages.error(request, 'Por favor selecciona un archivo.')
            return redirect('ver_material_mejia')

        # Verificar que el archivo sea de tipo Excel
        if not file.name.endswith('.xlsx'):
            messages.error(request, 'El archivo debe ser un archivo Excel (.xlsx).')
            return redirect('ver_material_mejia')

        try:
            wb = openpyxl.load_workbook(file)
            sheet = wb.active  # Seleccionar la hoja activa del archivo Excel

            # Obtener todos los códigos que están en el modelo MaterialSeleccionado
            codigos_seleccionados = MaterialSeleccionado.objects.values_list('codigo', flat=True)

            # Empezar desde la segunda fila (ignorar el encabezado)
            for row in sheet.iter_rows(min_row=2, values_only=True):
                codigo = row[18]  # Columna S (índice 18)
                
                 # Convertir el código a string en caso de que sea numérico
                codigo = str(codigo)
                
                # Verificar si el código está en MaterialSeleccionado
                if codigo in codigos_seleccionados:
                    pedido = row[3]   # Columna D (índice 3)
                    actividad = row[11]  # Columna L (índice 11)
                    instalador = row[12]  # Columna M (índice 12)
                    cantidad = row[20]  # Columna U (índice 20)
                    fecha = row[25]  # Columna Z (índice 25)
                    acta = row[26]  # Columna AA (índice 26)

                    # Crear la instancia del modelo Pedido y guardarla
                    Pedido.objects.create(
                        pedido=pedido,
                        actividad=actividad,
                        instalador=instalador,
                        codigo=codigo,
                        cantidad=cantidad,
                        fecha=fecha,
                        acta=acta
                    )
            
            messages.success(request, 'Archivo subido y procesado correctamente.')
            return redirect('ver_material_mejia')

        except Exception as e:
            messages.error(request, f'Error al procesar el archivo: {str(e)}')
            print(e)
            return redirect('ver_material_mejia')

    return redirect('ver_material_mejia')


def ver_material_mejia(request):
    pedidos = Pedido.objects.all()  # Obtén todos los pedidos desde la base de datos
    return render(request, 'material_mejia.html', {'pedidos': pedidos}) 

def ver_material_acta(request):
    pedidos = ActaB.objects.all()  # Obtén todos los pedidos desde la base de datos
    return render(request, 'material_acta.html', {'actas': pedidos}) 

from django.shortcuts import render, redirect
from django.contrib import messages
import openpyxl
from .models import ActaB, MaterialSeleccionado

def subir_material_acta(request):
    if request.method == 'POST':
        file = request.FILES.get('file')

        if not file:
            messages.error(request, 'Por favor selecciona un archivo.')
            return redirect('ver_material_acta')

        # Verificar que el archivo sea de tipo Excel
        if not file.name.endswith('.xlsx'):
            messages.error(request, 'El archivo debe ser un archivo Excel (.xlsx).')
            return redirect('ver_material_acta')
        
        try:
            wb = openpyxl.load_workbook(file)
            sheet = wb.active  # Seleccionar la hoja activa del archivo Excel
            
            # Obtener todos los valores del campo 'guia' del modelo MaterialSeleccionado
            guias_seleccionadas = MaterialSeleccionado.objects.values_list('guia', flat=True)

            # Empezar desde la segunda fila (ignorar el encabezado)
            for row in sheet.iter_rows(min_row=2, values_only=True):
                
                
                pedido = row[0]  # Columna A (índice 0)

                actividad = row[7]  # Columna H (índice 7)
                
                # Columna S (índice 18) o R (índice 17) si S está vacía
                codigo = row[18] if row[18] else row[17]

                # Convertir el código a string en caso de que sea numérico
                codigo = str(codigo)
                
                # Si el código termina en 'A' o 'P', eliminar el último carácter
                if codigo and codigo[-1] in ['A', 'P']:
                    codigo = codigo[:-1]

                cantidad = row[20]  # Columna U (índice 20)

                # Verificar si el código está en el campo 'guia' del modelo MaterialSeleccionado                
                if codigo in guias_seleccionadas:
                    # Crear la instancia del modelo Acta y guardarla
                    ActaB.objects.create(
                        pedido=pedido,
                        actividad=actividad,
                        codigo=codigo,
                        cantidad=float(cantidad)
                    )

            messages.success(request, 'Archivo subido y procesado correctamente.')
            return redirect('ver_material_acta')

        except Exception as e:
            messages.error(request, f'Error al procesar el archivo: {str(e)}')
            print(str(e))
            return redirect('ver_material_acta')

    return redirect('ver_material_acta')


def reiniciar_actas(request):
    Pedido.objects.all().delete()
    ActaB.objects.all().delete()
    ComparacionPedido.objects.all().delete()
    return render(request, 'material_mejia.html') 

from django.db.models import Sum
from .models import Pedido, ActaB, ComparacionPedido

from django.db.models import Sum
from .models import Pedido, ActaB, ComparacionPedido

from django.db.models import Sum
from .models import Pedido, ActaB, ComparacionPedido, MaterialSeleccionado

from django.shortcuts import render, redirect
from .models import Pedido, ActaB, ComparacionPedido, MaterialSeleccionado
from django.db.models import Sum

def comparar_pedidos(request):
    # Obtener las sumas de materiales del modelo Pedido, incluyendo todos los campos necesarios
    pedidos = Pedido.objects.values(
        'pedido', 'codigo', 'fecha', 'actividad', 'instalador'
    ).annotate(suma_pedido=Sum('cantidad'))

    # Obtener la relación de códigos y guías del modelo MaterialSeleccionado
    seleccionados = MaterialSeleccionado.objects.values('codigo', 'guia')

    # Crear un diccionario de 'guia' a 'codigo' para asociar código en Pedido con guía en ActaB
    guia_to_codigo = {s['guia']: s['codigo'] for s in seleccionados}

    # Obtener las sumas de materiales del modelo ActaB, usando 'guia' en lugar de 'codigo'
    actas = ActaB.objects.values('pedido', 'codigo').annotate(suma_acta=Sum('cantidad'))

    for pedido in pedidos:
        # Encontrar la guía correspondiente al código del pedido en MaterialSeleccionado
        guia_correspondiente = next((g for g, c in guia_to_codigo.items() if c == pedido['codigo']), None)

        if guia_correspondiente:
            # Buscar la suma correspondiente en ActaB con el código relacionado (la guía)
            acta = next((a for a in actas if a['pedido'] == pedido['pedido'] and a['codigo'] == guia_correspondiente), None)

            suma_material_acta = acta['suma_acta'] if acta else 0
            suma_material_pedido = pedido['suma_pedido']

            # Solo guardamos los registros donde las sumas no coinciden
            if suma_material_acta != suma_material_pedido:
                # Asegúrate de que 'fecha' y demás campos existen en el diccionario 'pedido'
                fecha = pedido.get('fecha', None)
                actividad = pedido.get('actividad', '')
                instalador = pedido.get('instalador', '')

                # Establecer la observación si las cantidades no coinciden
                observacion = 'Cantidad no coincide' if suma_material_acta != suma_material_pedido else ''

                # Crear una instancia del modelo ComparacionPedido
                ComparacionPedido.objects.create(
                    pedido=pedido['pedido'],
                    codigo=pedido['codigo'],
                    suma_material_pedido=suma_material_pedido,
                    suma_material_acta=suma_material_acta,
                    diferencia=suma_material_acta - suma_material_pedido,
                    actividad=actividad,
                    fecha=fecha,
                    instalador=instalador,
                    observacion=observacion
                )
    verificar_codigos_actab_sin_pedido(request)

    return redirect('lista_comparaciones')

from .models import Pedido, ActaB, ComparacionPedido

from .models import Pedido, ActaB, ComparacionPedido, MaterialSeleccionado
from django.db.models import Sum

def verificar_codigos_actab_sin_pedido(request):
    # Obtener todos los códigos y pedidos del modelo Pedido
    pedidos = Pedido.objects.values('pedido', 'codigo')

    # Convertir los pedidos y códigos en un conjunto para facilitar la búsqueda
    pedidos_codigos = set((p['pedido'], p['codigo']) for p in pedidos)

    # Obtener las guías del modelo MaterialSeleccionado que vinculan los códigos de Pedido y ActaB
    material_seleccionado = MaterialSeleccionado.objects.values('codigo', 'guia')

    # Crear un diccionario de 'guia' a 'codigo' para asociar código en Pedido con la guía en ActaB
    guia_to_codigo = {ms['guia']: ms['codigo'] for ms in material_seleccionado}

    # Obtener todos los códigos y pedidos del modelo ActaB
    actas = ActaB.objects.values('pedido', 'codigo', 'cantidad')

    # Iterar sobre los códigos de ActaB
    for acta in actas:
        # Verificar si el código en ActaB (que corresponde a la 'guía') no está asociado a un código en Pedido
        codigo_pedido = guia_to_codigo.get(acta['codigo'], None)

        # Si no hay un código en Pedido asociado a la guía (código en ActaB), creamos el registro en ComparacionPedido
        if not codigo_pedido or (acta['pedido'], codigo_pedido) not in pedidos_codigos:
            # Si el código no está en Pedido, creamos un registro en ComparacionPedido
            ComparacionPedido.objects.create(
                pedido=acta['pedido'],
                codigo=acta['codigo'],  # Mostramos la guía (código en ActaB)
                suma_material_pedido=0,  # No hay datos en Pedido, así que la suma es 0
                suma_material_acta=acta['cantidad'],  # Usar el valor de ActaB
                diferencia=acta['cantidad'],  # Diferencia será igual a la suma de ActaB
                actividad='',  # Si necesitas copiar datos adicionales, puedes hacerlo aquí
                fecha=None,  # Usar None si no hay una fecha correspondiente
                instalador='',  # Usar valores por defecto o buscar una manera de obtener estos datos
                observacion=f'Código {acta["codigo"]} no aparece en Perseo'
            )

    messages.success(request, 'Verificación completada. Registros creados para códigos que no aparecen en Perseo.')
    return redirect('lista_comparaciones')


from django.shortcuts import render
from .models import ComparacionPedido, MaterialSeleccionado

def lista_comparaciones(request):
    # Obtener todas las comparaciones guardadas en la base de datos
    comparaciones = ComparacionPedido.objects.all()

    # Crear una lista para almacenar los datos con la 'guía' de MaterialSeleccionado
    comparaciones_con_guia = []

    # Obtener la relación 'codigo' y 'guia' de MaterialSeleccionado
    seleccionados = MaterialSeleccionado.objects.values('codigo', 'guia')

    # Crear un diccionario de 'codigo' a 'guia'
    codigo_to_guia = {s['codigo']: s['guia'] for s in seleccionados}

    # Iterar sobre las comparaciones y buscar la 'guia' correspondiente al 'codigo'
    for comparacion in comparaciones:
        guia = codigo_to_guia.get(comparacion.codigo, comparacion.codigo)  # Si no hay guía, usar el código como fallback
        comparaciones_con_guia.append({
            'pedido': comparacion.pedido,
            'actividad': comparacion.actividad,
            'codigo': guia,  # Mostrar la guía en lugar del código
            'suma_material_pedido': comparacion.suma_material_pedido,
            'suma_material_acta': comparacion.suma_material_acta,
            'diferencia': comparacion.diferencia,
            'instalador': comparacion.instalador,
            'observacion': comparacion.observacion,
            'fecha': comparacion.fecha,
        })

    return render(request, 'lista_comparaciones.html', {'comparaciones': comparaciones_con_guia})
