from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static



from Programacion.views import *
urlpatterns = [
    path('acrev/', acrev, name="acrev"),
    path('amrtr/', amrtr, name="amrtr"),
    path('legalizaciones/', lega, name="lega"),
    path('inconsistencias/', inconsistencias, name="inconsistencias"),
    path('programador/', programador, name="programador"),
] +static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)


