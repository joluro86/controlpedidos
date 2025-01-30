from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static 

from gestionvencimientos.views import registrar_acta, calculo_inventario_por_oficial, reiniciar_medidores, reiniciar_bd_oficiales, gestion_medidores, reiniciar_medidores, gestionar_acta_perseo_inventario, pedidos_week, otros_pedidos, vencimientos_contrato, vencimientos_epm,  index, fechas, vencidos, busqueda_pendientes, busqueda_vencidos, gestion_bd, cerrar_pedido,  limpiar_base, eliminar_bd, subir_acta_ans, calculo_pendientes, calculo_next_week, calculo_last_week, menu_pendientes
urlpatterns = [
    path('subir_acta_ans/', subir_acta_ans, name="subir_acta_ans"),
    path('admin/', admin.site.urls, name="administrador"),
    path('', index, name="home"),
    path('pendientes/<int:id_dia>', calculo_pendientes, name="pendientes"),
    path('proxsemana/<int:id_dia>', calculo_next_week, name="pendientes_next_week"),
    path('antsemana/<int:id_dia>', calculo_last_week, name="pendientes_last_week"),
    path('pendientes/', menu_pendientes, name="menu_pendientes"),
    path('limpiar/', limpiar_base, name="limpiar"),
    path('eliminar/', eliminar_bd, name="eliminar"),
    path('fechas/', fechas, name="fechas"),
    path('vencidos/', vencidos, name="vencidos"),
    path('vencidos_todos/', busqueda_vencidos, name="vencidos_todos"),
    path('gestion/', gestion_bd, name="gestionbd"),
    path('cerrar/<int:id_pedido>/', cerrar_pedido, name="cerrar"),
    path('week/<int:id_week>/', pedidos_week, name="week"),
    path('otros/<int:cliente>/<int:apla>/<int:pendi>/', otros_pedidos, name="otros"),
    path('epm/<str:inicio>/<str:final>/', vencimientos_epm, name="epm"),
    path('contrato/<str:inicio>/<str:final>/', vencimientos_contrato, name="contrato"),
    path('gestion-medidores/', gestion_medidores, name="gestion_medidores"),
    path('eliminar-medidores/', reiniciar_medidores, name="reiniciar_medidores"),
    path('accounts/', include('django.contrib.auth.urls')),

    path('analisis/', include('analisis_acta.urls')),
    path('programar/', include('programacion.urls')),
    path('comparativo/', include('perseovsfenix.urls')),
    path('material_oficiales/', include('material_oficiales.urls')),
    path('ped-bonficiaciones/', include('bonificaciones.urls')),

    path('inventariobd/', gestionar_acta_perseo_inventario, name="gestionar_acta_perseo_inventario"), 
    path('oficial/', calculo_inventario_por_oficial, name="calculo_inventario_por_oficial"),
    path('oficial_reiniciar/', reiniciar_bd_oficiales, name="reiniciar_bd_oficiales"),

    path('nomina/', include('nominametro.urls')),
    
    path('produccion/', include('produccion.urls')),
    path('material_mejia/', include('material_mejia.urls')),

    path('registrar-acta/', registrar_acta, name='registrar_acta'),
    path('administrador/', include('administrador.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


