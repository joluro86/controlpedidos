from django.contrib import admin
from analisis.models import *
from import_export.admin import ImportExportModelAdmin 
from import_export import resources
from perseovsfenix.models import Guia

class EncargadoResource(resources.ModelResource):
    class Meta:
        model = Acta_analisis

class Actia_analisis_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','municipio','actividad','pagina','urbrur','tipre','tipo','suminis','item_cont','cantidad',)
    class Meta:
        model = Acta_analisis

admin.site.register(Acta_analisis, Actia_analisis_Admin)
    

