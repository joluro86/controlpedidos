from django.contrib import admin
from Analisis_acta.models import *
from import_export.admin import ImportExportModelAdmin 
from import_export import resources

class ActaResource(resources.ModelResource):
    class Meta:
        model = Acta

class MaterialResource(resources.ModelResource):
    class Meta:
        model = Materiales
        use_bulk = False

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


admin.site.register(Acta, Acta_Admin)
admin.site.register(Novedad_acta, Novedades_Admin)
admin.site.register(Materiales, Materiales_Admin)
