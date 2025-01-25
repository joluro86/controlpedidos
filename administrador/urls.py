from django.contrib import admin
from django.urls import path
from administrador.views import index, editar_actividad, nueva_actividad, eliminar_actividad_por_id
from administrador.views_epm import nueva_actividad_epm, editar_actividad_epm, eliminar_actividad_por_id_epm
from administrador.views_encargado import nuevo_encargado
urlpatterns = [
    path('new_admin/', index, name="index_admin"),
    path('editar-actividad/<int:actividad_id>/', editar_actividad, name='editar_actividad'), 
    path('nueva_actividad_contrato/', nueva_actividad, name='nueva_actividad_form'),
    path('eliminar-actividad/<int:id>/', eliminar_actividad_por_id, name='eliminar_actividad'),

    path('nueva_actividad_epm/', nueva_actividad_epm, name='nueva_actividad_epm_form'),
    path('editar-actividad-epm/<int:actividad_id>/', editar_actividad_epm, name='editar_actividad_epm'),
    path('eliminar-actividad-epm/<int:id>/', eliminar_actividad_por_id_epm, name='eliminar_actividad_epm'),
    
    path('nuevo_encargado/', nuevo_encargado, name='nueva_encargado_form'),
    ]

