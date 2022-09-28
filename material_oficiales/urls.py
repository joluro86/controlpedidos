from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

from gestionvencimientos.views import *
urlpatterns = [

    path('inventariobd/', gestionar_acta_perseo_inventario, name="gestionar_acta_perseo_inventario"), 
    path('oficial/', calculo_inventario_por_oficial, name="calculo_inventario_por_oficial"),
    path('oficial_reiniciar/', reiniciar_bd_oficiales, name="reiniciar_bd_oficiales"),

] +static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)


