from django.contrib import admin
from django.urls import path

from bonificaciones.views import gestion_fenix, datos_por_pedido, reiniciar_acta_bonificaciones

urlpatterns = [
    path('gestion_fenix/', gestion_fenix, name="calculo_bd_fenix_perseo"),
    path('reiniciar_actas_bonificaciones/', reiniciar_acta_bonificaciones, name="reiniciar_actas_bonificaciones"),
    path('datos-por-pedido/', datos_por_pedido, name="datos_por_pedido"),
]
