from django.urls import path
from . import views

urlpatterns = [
    path('formulario-subir-material-mejia/', views.formulario_subir_pedido, name='formulario_subir_perseo'),
    path('subir-material-mejia/', views.subir_material_mejia, name='subir_material_mejia'),    
    path('ver-material-mejia/', views.ver_material_mejia, name='ver_material_mejia'),
    path('reiniciar-actas/', views.reiniciar_actas, name='reiniciar_actas'),
    path('formulario-subir-material-acta/', views.formulario_subir_acta, name='formulario_subir_acta'),
    path('subir-material-acta/', views.subir_material_acta, name='subir_material_acta'),
    path('ver-material-acta/', views.ver_material_acta, name='ver_material_acta'),
    path('comparar-pedidos/', views.comparar_pedidos, name='comparar_pedidos'),
    path('lista-comparaciones/', views.lista_comparaciones, name='lista_comparaciones'),
]
