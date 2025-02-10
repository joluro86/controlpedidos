from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from sellos.views_acta import generar_informe, subir_acta, reiniciar_extracciones,novedades_sellos, ver_informe_sellos

urlpatterns = [
    
    path('subir_acta_sellos/<str:archivo>/', subir_acta, name="subir_acta_sellos"),
    path('generar-informe-sellos', generar_informe, name="generar_informe_sellos"),
    path('reiniciar-extracciones-sellos', reiniciar_extracciones, name="reiniciar_extracciones_sellos"),
    path('ver-informe-sellos', ver_informe_sellos, name="ver_informe_sellos"),
    path('ver-novedades-sellos', novedades_sellos, name="ver_novedades_sellos")                  
] +static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)