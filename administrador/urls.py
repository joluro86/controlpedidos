from django.urls import path
from administrador.views import index, editar_actividad, nueva_actividad, eliminar_actividad_por_id
from administrador.views_epm import nueva_actividad_epm, editar_actividad_epm, eliminar_actividad_por_id_epm
from administrador.views_encargado import editar_encargado, nuevo_encargado, eliminar_encargado
from administrador.views_masivo import subir_masivo_actividad_contrato, subir_masivo_actividad_epm, subir_masivo_encargados
from administrador.views_materiales import materiales_permitidos_list

urlpatterns = [
    path('new_admin/', index, name="index_admin"),
    path('editar-actividad/<int:actividad_id>/', editar_actividad, name='editar_actividad'), 
    path('nueva_actividad_contrato/', nueva_actividad, name='nueva_actividad_form'),
    path('eliminar-actividad/<int:id>/', eliminar_actividad_por_id, name='eliminar_actividad'),

    path('nueva_actividad_epm/', nueva_actividad_epm, name='nueva_actividad_epm_form'),
    path('editar-actividad-epm/<int:actividad_id>/', editar_actividad_epm, name='editar_actividad_epm'),
    path('eliminar-actividad-epm/<int:id>/', eliminar_actividad_por_id_epm, name='eliminar_actividad_epm'),
    
    path('nuevo_encargado/', nuevo_encargado, name='nueva_encargado_form'),
    path('editar-encargado/<int:encargado_id>/', editar_encargado, name='editar_encargado'),
    path('eliminar-encargado/<int:id>/', eliminar_encargado, name='eliminar_encargado'),
    
    path('masivo-actividad-contrato/', subir_masivo_actividad_contrato, name='subir_masivo_actividad_contrato'),
    path('masivo-actividad-epm/', subir_masivo_actividad_epm, name='subir_masivo_actividad_epm'),
    path('masivo-actividad-encargados/', subir_masivo_encargados, name='subir_masivo_encargados'),  
    
    path('materiales-revision-acta/', materiales_permitidos_list, name='materiales_permitidos_list'),    
    ]

