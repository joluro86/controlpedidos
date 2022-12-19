from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



from analisis.views import *
urlpatterns = [
    path('formulario_subir_acta_analisis/', formulario_subir_acta, name="formulario_subir_acta_analisis"),
    path('subir_acta_analisis/', subir_acta, name="subir_acta_analisis"),
    path('busqueda-pedidos-acta-analisis/', busqueda_pedidos_acta_analisis, name="busqueda-pedidos-acta-analisis"),
    
] +static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)


