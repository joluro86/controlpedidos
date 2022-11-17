from django.contrib import admin
from django.urls import path

from perseovsfenix.views import *

urlpatterns = [
    path('gestionbd/', gestionarbd, name="gestionbd"),
    path('reiniciar/', reiniciar_bd_materiales, name="reiniciar_bd_materiales"),
    path('calculo_novedades_perseo_vs_fenix/', calculo_novedades_perseo_vs_fenix, name="calculo_novedades_perseo_vs_fenix"),
    path('novedades-perseo-fenix/', novedades_perseo_vs_fenix, name="novedades_perseo_fenix")
]
