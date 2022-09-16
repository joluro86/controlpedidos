from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static



from Analisis_acta.views import *
urlpatterns = [
    path('limpiar_novedades/', limpiar_novedades, name="limpiarnov"),
    path('limpiar_acta/', limpiar_acta, name="limpiaracta"),
    path('calculo_novedades/', calculo_novedades_acta, name="calculo_novedades"),
    path('novedades-acta/', novedades_acta, name="novedades_acta"),
    
] +static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)


