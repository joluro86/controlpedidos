from django.contrib import admin
from django.urls import path

from bonificaciones.views import bonificaciones, calcalulo_bonificaciones, reiniciar_acta_bonificaciones

urlpatterns = [
    path('calculo-bonificaciones/', calcalulo_bonificaciones, name="calculo_bonificaciones"),
    path('reiniciar_actas_bonificaciones/', reiniciar_acta_bonificaciones, name="reiniciar_actas_bonificaciones"),
    path('bonificaciones/', bonificaciones, name="bonificaciones"),
]
