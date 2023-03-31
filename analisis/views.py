import time
from django.shortcuts import redirect, render, HttpResponse
import pandas as pd

from analisis.queries import analisis_acta
from .forms import ActaAnalisisFileForm
from .models import Acta_analisis
from math import isnan


def formulario_subir_acta(request):
    form = ActaAnalisisFileForm()
    return render(request, 'form_subir_acta_analisis.html', {'form': form})


def subir_acta(request):
    inicio = time.time()
    if request.method == 'POST':
        form = ActaAnalisisFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['archivo']
            df = pd.read_excel(file)
            cont = 0
            for index, row in df.iterrows():
                if row['subz'] == 'URA':
                    try:
                        if isnan(row['item_cont']):
                            item_cont = row['suminis']
                    except:
                        item_cont = row['item_cont']

                    try:
                        if isnan(row['tipre']):
                            tipre = ""
                    except:
                        tipre = row['tipre']

                    Acta_analisis.objects.create(
                        pedido=row['pedido'],
                        subz=row['subz'],
                        municipio=row['municipio'],
                        actividad=row['actividad'],
                        pagina=row['pagina'],
                        urbrur=row['urbrur'],
                        tipre=tipre,
                        tipo=row['tipo'],
                        suminis=row['suminis'],
                        item_cont=item_cont,
                        cantidad=row['cantidad'],
                    )
            fin = time.time()
            total = fin-inicio
            print(total)
    else:
        form = ActaAnalisisFileForm()

    return redirect('busqueda-pedidos-acta-analisis')


def busqueda_pedidos_acta_analisis(request):

    pedidos = Acta_analisis.objects.all()
    datos = {'pedidos': pedidos}
    return render(request, 'pedidos_subidos_acta.html', datos)

def analizar_acta(request):
    analisis_acta()

    return redirect('busqueda-pedidos-acta-analisis')

def eliminar_acta(request):
    Acta_analisis.objects.all().delete()
    return redirect('busqueda-pedidos-acta-analisis')
