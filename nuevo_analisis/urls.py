from django.urls import path
from nuevo_analisis import views
from nuevo_analisis.logica import analisis_reglas

urlpatterns = [
    # Análisis de reglas
    path('analisis_reglas/', analisis_reglas, name="analisis_reglas"),

    # Ítems de regla
    path('items/', views.lista_item_regla, name='listado_items_regla'),
    path('items/nuevo/', views.crear_editar_item_regla, name='crear_item_regla'),
    path('items/editar/<int:pk>/', views.crear_editar_item_regla, name='editar_item_regla'),
    path('items/eliminar/<int:pk>/', views.eliminar_item_regla, name='eliminar_item_regla'),

    # Relaciones de ítems (actividad/suministro)
    path('relaciones/', views.lista_relacion_item_regla, name='listado_relaciones'),
    path('relaciones/nueva/', views.crear_editar_relacion_item_regla, name='crear_relacion_item'),
    path('relaciones/editar/<int:pk>/', views.crear_editar_relacion_item_regla, name='editar_relacion_item_regla'),
    path('relaciones/eliminar/<int:pk>/', views.eliminar_relacion_item_regla, name='eliminar_relacion_item_regla'),

    # Relaciones de incompatibilidad (separadas para evitar conflicto de ruta)
    path('incompatibilidades/', views.lista_relaciones_incompatibilidad, name='lista_relaciones_incompatibilidad'),
    path('incompatibilidades/nueva/', views.crear_relacion_incompatibilidad, name='crear_relacion_incompatibilidad'),
    path('incompatibilidades/editar/<int:pk>/', views.editar_relacion_incompatibilidad, name='editar_relacion_incompatibilidad'),
    path('incompatibilidades/eliminar/<int:pk>/', views.eliminar_relacion_incompatibilidad, name='eliminar_relacion_incompatibilidad'),

    # Relaciones por carácter final
    path('caracteres/', views.lista_relaciones_caracter, name='lista_relaciones_caracter'),
    path('caracteres/nueva/', views.crear_relacion_caracter, name='crear_relacion_caracter'),
    path('caracteres/editar/<int:pk>/', views.editar_relacion_caracter, name='editar_relacion_caracter'),
    path('caracteres/eliminar/<int:pk>/', views.eliminar_relacion_caracter, name='eliminar_relacion_caracter'),

        # Relaciones por cantidad (limites)
    path('cantidades/', views.lista_relaciones_cantidad, name='lista_relaciones_cantidad'),
    path('cantidades/nueva/', views.crear_relacion_cantidad, name='crear_relacion_cantidad'),
    path('cantidades/editar/<int:pk>/', views.editar_relacion_cantidad, name='editar_relacion_cantidad'),
    path('cantidades/eliminar/<int:pk>/', views.eliminar_relacion_cantidad, name='eliminar_relacion_cantidad'),

]

