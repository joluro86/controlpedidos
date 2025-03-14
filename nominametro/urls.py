from django.contrib import admin
from django.urls import path

from nominametro.views import export_excel, get_progress, subirnominametro, reiniciar_prenomina, gestionar_prenomina, definir_fechas, informe

urlpatterns = [
    path('subir_nomina_metro/', subirnominametro, name="subirnominametro"),
    path('get_progress/', get_progress, name="get_progress"),
    path('reiniciar_nomina_metro/', reiniciar_prenomina, name="reiniciar_prenomina"),    
    path('definir_fechas_nomina_metro/', definir_fechas, name="definir_fechas"),
    path('gestionar_nomina_metro/', gestionar_prenomina, name="gestionar_prenomina"),
    path('informe/', informe, name="informe"),  
    path('export_excel/', export_excel, name="export_excel"),
    ]

