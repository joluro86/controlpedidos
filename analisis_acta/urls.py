from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from analisis_acta.views import *
urlpatterns = [
    path('subir_acta_revision/', subir_acta_revision, name="subir_acta_revision"),
    path('calculo_novedades/', calculo_novedades_acta, name="calculo_novedades"),
    
    path('limpiar_novedades/', limpiar_novedades, name="limpiarnov"),
    path('limpiar_acta/', limpiar_acta, name="limpiaracta"),
   
    path('novedades-acta/', novedades_acta, name="novedades_acta"),
            
] +static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)


