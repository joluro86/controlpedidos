from django.contrib import admin
from django.urls import path

from bonificaciones.views import bonificaciones, calculo_diario_instalador, gestion_fenix, producido_diario, reiniciar_acta_bonificaciones

urlpatterns = [
    path('gestion_fenix/', gestion_fenix, name="calculo_bd_fenix_perseo"),
    path('calculo_diario_oficiales/', calculo_diario_instalador, name="calculo_promedio_oficiales"),
    path('reiniciar_actas_bonificaciones/', reiniciar_acta_bonificaciones, name="reiniciar_actas_bonificaciones"),
    path('producido_diario/', producido_diario, name="producido_diario"),
    path('bonificaciones/', bonificaciones, name="bonificaciones"),
]
