from django.urls import path
from .views import ImportDataView, ValorReferenciaView,import_data_success, valor_referencia_success, reiniciar, novedades, bonificacion_prod, reiniciar_novedades, dia_dia


urlpatterns = [
   path('import-data/', ImportDataView.as_view(), name='import_data'),
   path('valor-referencia/', ValorReferenciaView.as_view(), name='valor-referencia'),
   path('import-data/success/', import_data_success, name='import_data_success'),
   path('reiniciar/', reiniciar, name='reiniciar'),
   path('reiniciar-novedades/', reiniciar_novedades, name='reiniciar'),
   path('novedades/', novedades, name='novedades'),
   path('bonificacion_prod/', bonificacion_prod, name='bonificacion_prod'),
   path('producido_por_oficial/', dia_dia, name='dia_dia'),
   path('valor_referencia_success/', valor_referencia_success, name='valor_referencia_success'),
    ]