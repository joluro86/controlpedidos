from django.contrib import admin
from django.urls import path

from perseovsfenix.views import *

urlpatterns = [
    path('subir_pvf_matfenix/', subir_pvf_matfenix, name="subir_pvf_matfenix"),
    path('subir_pvf_matperseo/', subir_pvf_matperseo, name="subir_pvf_matperseo"),
    path('reiniciar/', reiniciar_bd_materiales, name="reiniciar_bd_materiales"),
    path('calculo_novedades_perseo_vs_fenix/', calculo_novedades_perseo_vs_fenix, name="calculo_novedades_perseo_vs_fenix"),
    path('novedades-perseo-fenix/', novedades_perseo_vs_fenix, name="novedades_perseo_fenix"),
    path('reiniciar-novedades-perseo-fenix/', reiniciar_novedades_perseo_vs_fenix, name="reiniciar_novedades"),
]
