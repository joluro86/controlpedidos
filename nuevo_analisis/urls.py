from django.urls import path
from nuevo_analisis import views 
from nuevo_analisis.logica import analisis_reglas

urlpatterns = [
    # URLs para ItemRegla
    path('analisis_reglas/', analisis_reglas, name="analisis_reglas"),
    #path('eliminar/<int:id>/', eliminar_regla, name="eliminar_regla"),
    
    path('items/', views.lista_item_regla, name='listado_items_regla'),
    path('items/nuevo/', views.crear_editar_item_regla, name='crear_item_regla'),
    path('items/editar/<int:pk>/', views.crear_editar_item_regla, name='editar_item_regla'),
    path('items/eliminar/<int:pk>/', views.eliminar_item_regla, name='eliminar_item_regla'), # Considera usar POST para eliminar

    # URLs para RelacionItemRegla
    path('relaciones/', views.lista_relacion_item_regla, name='listado_relaciones'),
    path('relaciones/nueva/', views.crear_editar_relacion_item_regla, name='crear_relacion_item'), # Cambié 'crear_relacion_item' a 'crear_relacion_item_regla'
    path('relaciones/editar/<int:pk>/', views.crear_editar_relacion_item_regla, name='editar_relacion_item_regla'),
    path('relaciones/eliminar/<int:pk>/', views.eliminar_relacion_item_regla, name='eliminar_relacion_item_regla'),
]
