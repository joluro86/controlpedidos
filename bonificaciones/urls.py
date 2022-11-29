from django.contrib import admin
from django.urls import path

from bonificaciones.views import gestion_bd_fenix_perseo, datos_por_pedido, calcalulo_bonificaciones, reiniciar_acta_bonificaciones

urlpatterns = [
    path('gestion-bd-fenix-perseo/', gestion_bd_fenix_perseo, name="calculo_bd_fenix_perseo"),
    path('calculo-bonificaciones/', calcalulo_bonificaciones, name="calculo_bonificaciones"),
    path('reiniciar_actas_bonificaciones/', reiniciar_acta_bonificaciones, name="reiniciar_actas_bonificaciones"),
    path('datos-por-pedido/', datos_por_pedido, name="datos_por_pedido"),
]
