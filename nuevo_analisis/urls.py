from django.urls import path
from nuevo_analisis import views 
from nuevo_analisis.views import editar_regla
from nuevo_analisis.logica import validar_reglas, eliminar_regla

urlpatterns = [       
    path('relacion/nueva/', views.crear_relacion_item, name='crear_relacion_item'),
    path('item/nuevo/', views.crear_item_regla, name='crear_item_regla'),
    
    path('items/', views.listado_items_regla, name='listado_items_regla'),
    path('item/nuevo/', views.crear_item_regla, name='crear_item_regla'),
    path('item/<int:pk>/editar/', views.editar_item_regla, name='editar_item_regla'),
    path('item/<int:pk>/eliminar/', views.eliminar_item_regla, name='eliminar_item_regla'),
    path('relaciones/', views.listado_relaciones, name='listado_relaciones'),
    
    path('validar_relaciones/', validar_reglas, name="validar_reglas_link"),
    path('eliminar/<int:id>/', eliminar_regla, name="eliminar_regla"),
    
    path('reglas/editar/<int:pk>/', editar_regla, name='editar_regla'),

]
