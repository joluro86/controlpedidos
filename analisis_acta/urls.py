from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from analisis_acta.views import subir_acta_revision, calculo_novedades_acta, limpiar_novedades, limpiar_acta, novedades_acta
from analisis_acta.views_nuevo_analisis import analisis_revision_acta_nuevo, subir_cantidad_items, eliminar_cantidad_items

urlpatterns = [
    path('subir_acta_revision/', subir_acta_revision, name="subir_acta_revision"),
    path('calculo_novedades/', calculo_novedades_acta, name="calculo_novedades"),
    path('revision_acta/', analisis_revision_acta_nuevo, name="analisis_acta"),
        
    path('limpiar_novedades/', limpiar_novedades, name="limpiarnov"),
    path('limpiar_acta/', limpiar_acta, name="limpiaracta"),
   
    path('novedades-acta/', novedades_acta, name="novedades_acta"),
    
    path('subir-cantidad-items/', subir_cantidad_items, name='subir_cantidad_items'),
    path('eliminar-cantidad-items/<int:id>/', eliminar_cantidad_items, name='eliminar_cantidad_items'),
            
] +static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)


