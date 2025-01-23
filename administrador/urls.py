from django.contrib import admin
from django.urls import path
from administrador.views import index, editar_actividad

urlpatterns = [
    path('new_admin/', index, name="index_admin"),
    path('editar-actividad/<int:actividad_id>/', editar_actividad, name='editar_actividad'),
    ]