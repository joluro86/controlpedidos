from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
from import_export import resources
from material_oficiales.models import *

class StockBuscarResource(resources.ModelResource):
    class Meta:
        model = Stock

class Stock_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('encargado','codigo', 'inicio', 'despachado', 'epm', 'diferencia')
    class Meta:
        model = Stock

class Material_A_BuscarResource(resources.ModelResource):
    class Meta:
        model = Material_A_Buscar

class Material_A_Buscar_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre',)
    class Meta:
        model = Material_A_Buscar

class IngresoResource(resources.ModelResource):
    class Meta:
        model = Inicio

class IngresoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('encargado','codigo','cantidad')
    class Meta:
        model = Inicio

class OficialResource(resources.ModelResource):
    class Meta:
        model = Oficial

class OficialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre',)
    class Meta:
        model = Oficial

class DespachoResource(resources.ModelResource):
    class Meta:
        model = Despacho

class DespachoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('codigo','fecha', 'encargado','cantidad')
    class Meta:
        model = Despacho

class ReintegroResource(resources.ModelResource):
    class Meta:
        model = Reintegro

class ReintegroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('codigo','fecha', 'encargado','cantidad')
    class Meta:
        model = Reintegro

class Liquidacion_acta_epmResource(resources.ModelResource):
    class Meta:
        model = Liquidacion_acta_epm

class Liquidacion_acta_epm_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad', 'item_cont','cantidad')
    class Meta:
        model = Liquidacion_acta_epm

class Material_utilizado_perseoResource(resources.ModelResource):
    class Meta:
        model = Material_utilizado_perseo

class Material_utilizado_perseo_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','instalador', 'fecha','codigo','cantidad')
    class Meta:
        model = Material_utilizado_perseo

admin.site.register(Stock, Stock_Admin)
admin.site.register(Material_A_Buscar, Material_A_Buscar_Admin)
admin.site.register(Oficial, OficialAdmin)
admin.site.register(Inicio, IngresoAdmin)
admin.site.register(Despacho, DespachoAdmin)
admin.site.register(Material_utilizado_perseo, Material_utilizado_perseo_Admin)
admin.site.register(Liquidacion_acta_epm, Liquidacion_acta_epm_Admin)
admin.site.register(Reintegro, ReintegroAdmin)
