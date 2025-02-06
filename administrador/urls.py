from django.urls import path
from administrador.views import index, editar_actividad, nueva_actividad, eliminar_actividad_por_id
from administrador.views_epm import nueva_actividad_epm, editar_actividad_epm, eliminar_actividad_por_id_epm
from administrador.views_encargado import editar_encargado, nuevo_encargado, eliminar_encargado
from administrador.views_masivo import subir_masivo_actividad_contrato, subir_masivo_actividad_epm, subir_masivo_encargados
from administrador.views_materiales import materiales_permitidos_list, nuevo_material, subir_masivo_materiales_contrato, eliminar_material_contrato, editar_material_id
from administrador.views_perfil import upload_avatar, eliminar_foto
from administrador.views_variables_contrato import agregar_variable_contrato, editar_variable
from administrador.views_actividad_legalizacion import crear_actividad_legalizacion, editar_actividad_legalizacion, eliminar_actividad_legalizacion_id
from administrador.views_guia import GuiaCreateView, GuiaListView, actualizar_guia, eliminar_guia


urlpatterns = [
    path('subir-avatar/', upload_avatar, name='upload_avatar'),
    path('eliminar-foto/', eliminar_foto, name='eliminar_foto'),

    path('new_admin/', index, name="index_admin"),
    path('editar-actividad/<int:actividad_id>/',
         editar_actividad, name='editar_actividad'),
    path('nueva_actividad_contrato/', nueva_actividad,
         name='nueva_actividad_form'),
    path('eliminar-actividad/<int:id>/',
         eliminar_actividad_por_id, name='eliminar_actividad'),

    path('nueva_actividad_epm/', nueva_actividad_epm,
         name='nueva_actividad_epm_form'),
    path('editar-actividad-epm/<int:actividad_id>/',
         editar_actividad_epm, name='editar_actividad_epm'),
    path('eliminar-actividad-epm/<int:id>/',
         eliminar_actividad_por_id_epm, name='eliminar_actividad_epm'),

    path('nuevo_encargado/', nuevo_encargado, name='nueva_encargado_form'),
    path('editar-encargado/<int:encargado_id>/',
         editar_encargado, name='editar_encargado'),
    path('eliminar-encargado/<int:id>/',
         eliminar_encargado, name='eliminar_encargado'),

    path('masivo-actividad-contrato/', subir_masivo_actividad_contrato,
         name='subir_masivo_actividad_contrato'),
    path('masivo-actividad-epm/', subir_masivo_actividad_epm,
         name='subir_masivo_actividad_epm'),
    path('masivo-actividad-encargados/', subir_masivo_encargados,
         name='subir_masivo_encargados'),

    path('materiales-revision-acta/', materiales_permitidos_list,
         name='materiales_permitidos_list'),
    path('nuevo_material/', nuevo_material, name='nueva_material_form'),
    path('masivo-materiales/', subir_masivo_materiales_contrato,
         name='subir_masivo_materiales'),
    path('eliminar-material-contrato/<int:id>/',
         eliminar_material_contrato, name='eliminar-material-contrato'),
    path('editar-material/<int:material_id>/',
         editar_material_id, name='editar_material'),

    path('agregar-variables/', agregar_variable_contrato,
         name='agregar_variable_contrato_form'),
    path('editar-variable/<int:variable_id>/',
         editar_variable, name='editar_variable'),

    path('editar-actividad-legalizacion/<int:actividad_id>/',
         editar_actividad_legalizacion, name='editar_actividad_legalizacion'),
    path('nueva_actividad_legalizacion/', crear_actividad_legalizacion,
         name='nueva_actividad_legalizacion_form'),
    path('eliminar-actividad-legalizacion/<int:id>/',
         eliminar_actividad_legalizacion_id, name='eliminar_actividad_legalizacion'),

    path('guias/', GuiaListView.as_view(), name='guia_list'),
    path('nueva_guia/', GuiaCreateView.as_view(),
         name='nueva_guia_form'),
    path('editar-equivalencia/<int:id>/', actualizar_guia, name='update_guia'),
    path('eliminar-equivalencia/<int:id>/', eliminar_guia, name='eliminar_guia'),
]
