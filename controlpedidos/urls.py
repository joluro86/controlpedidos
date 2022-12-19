from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

from gestionvencimientos.views import *
urlpatterns = [
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
    path('medidores/', importar_acta_medidores, name="medidores_cables"),
    path('gestion-medidores/', gestion_medidores, name="gestion_medidores"),
    path('eliminar-medidores/', reiniciar_medidores, name="reiniciar_medidores"),
    path('accounts/', include('django.contrib.auth.urls')),

    path('analisis/', include('Analisis_acta.urls')),
    path('programar/', include('Programacion.urls')),
    path('comparativo/', include('perseovsfenix.urls')),
    path('material_oficiales/', include('material_oficiales.urls')),
    path('ped-bonficiaciones/', include('bonificaciones.urls')),

    path('inventariobd/', gestionar_acta_perseo_inventario, name="gestionar_acta_perseo_inventario"), 
    path('oficial/', calculo_inventario_por_oficial, name="calculo_inventario_por_oficial"),
    path('oficial_reiniciar/', reiniciar_bd_oficiales, name="reiniciar_bd_oficiales"),

    # NUEVO ANALISIS

    path('nuevo_analisis/', include('analisis.urls')),

] +static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)


