from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import login


from gestionvencimientos.views import amrtr, busqueda_vencidos, acrev, calculo_next_week, direccionamiento, lega, otros_pedidos, calculo_pendientes, cierre_masivo,  cerrar_pedido, eliminar_bd, fechas, gestion_bd, index, limpiar_base, menu_pendientes, pedidos_week, vencidos

urlpatterns = [
    path('admin/', admin.site.urls, name="administrador"),
    path('inicio/', index, name="home"),
    path('pendientes/<int:id_dia>', calculo_pendientes, name="pendientes"),
    path('proxsemana/<int:id_dia>', calculo_next_week,
         name="pendientes_next_week"),
    path('pendientes/', menu_pendientes, name="menu_pendientes"),
    path('limpiar/', limpiar_base, name="limpiar"),
    path('eliminar/', eliminar_bd, name="eliminar"),
    path('fechas/', fechas, name="fechas"),
    path('vencidos/', vencidos, name="vencidos"),
    path('vencidos_todos/', busqueda_vencidos, name="vencidos_todos"),
    path('gestion/', gestion_bd, name="gestionbd"),
    path('cerrar/<int:id_pedido>/<str:fecha_cierre>/<str:hora_cierre>',
         cerrar_pedido, name="cerrar"),
    path('week/<int:id_week>/', pedidos_week, name="week"),
    path('otros/<int:cliente>/<int:apla>/<int:pendi>/',
         otros_pedidos, name="otros"),
    path('cierre_masivo/<str:fecha_cierre>/<str:hora_cierre>/',
         cierre_masivo, name="cierre_masivo"),
    path('acrev/',
         acrev, name="acrev"),
    path('amrtr/',
         amrtr, name="amrtr"),
    path('legalizaciones/',
         lega, name="lega"),
    path('direccionamiento/',
         direccionamiento, name="direccion"),
    path('accounts/', include('django.contrib.auth.urls')),
]
