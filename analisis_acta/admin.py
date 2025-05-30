from django.contrib import admin
from analisis_acta.models import *
from import_export.admin import ImportExportModelAdmin 
from import_export import resources

class VariableResource(resources.ModelResource):
    class Meta:
        model = VariableAnalisis
class ActaResource(resources.ModelResource):
    class Meta:
        model = Acta

class MaterialResource(resources.ModelResource):
    class Meta:
        model = Materiales
        use_bulk = False

class Variable_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('region', 'contrato')
    class Meta:
        model = VariableAnalisis
        
class Materiales_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('material',)
    class Meta:
        model = Materiales

class NovedadActaResource(resources.ModelResource):
    class Meta:
        model = Novedad_acta

class Novedades_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad', 'novedad')
    class Meta:
        model = Novedad_acta

class Acta_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad', 'item_cont')
    class Meta:
        model = Acta

admin.site.register(VariableAnalisis, Variable_Admin)
admin.site.register(Acta, Acta_Admin)
admin.site.register(Novedad_acta, Novedades_Admin)
admin.site.register(Materiales, Materiales_Admin)
