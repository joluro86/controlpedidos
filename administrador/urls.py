from django.contrib import admin
from django.urls import path
from administrador.views import index

urlpatterns = [
    path('new_admin/', index, name="index_admin"),
    ]