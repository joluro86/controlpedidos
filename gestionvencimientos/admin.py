from django.contrib import admin
from gestionvencimientos.models import *
from import_export.admin import ImportExportModelAdmin 
from import_export import resources


# Register your models here.
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

class EncargadoResource(resources.ModelResource):
    class Meta:
        model = Encargado

class ActaResource(resources.ModelResource):
    class Meta:
        model = Acta

class NovedadActaResource(resources.ModelResource):
    class Meta:
        model = Novedad_acta

class ActividadResource(resources.ModelResource):
    class Meta:
        model = Actividad

class ActividadEpmResource(resources.ModelResource):
    class Meta:
        model = Actividad_epm
        
class AnsResource(resources.ModelResource):
    class Meta:
        model = Ans

class ActividadResource(resources.ModelResource):
    class Meta:
        model = Actividad

class AnsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('Pedido', 'Actividad', 'Fecha_Inicio_ANS', 'dias_vencimiento_epm' ,'fecha_vence_epm','dias_vencimiento' , 'Area_Trabajo', 'fecha_vencimiento' )
    resource_class = AnsResource
    list_filter = ('Estado',)
    search_fields = ['Pedido', 'Actividad', 'Area_Trabajo']
    
class EncargadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','nombre',)
    class Meta:
        model = Encargado

class ActividadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre','encargado','dias_urbano', 'dias_rural')
    class Meta:
        model = Actividad
        
class Actividad_epm_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre','dias_urbano', 'dias_rural')
    class Meta:
        model = Actividad_epm

class Novedades_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad', 'novedad')
    class Meta:
        model = Novedad_acta

class Acta_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad', 'item_cont')
    class Meta:
        model = Acta

# aqui

class GuiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre_perseo', 'nombre_fenix')
admin.site.register(Guia, GuiaAdmin)

class NumeroActaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(NumeroActa, NumeroActaAdmin)

class MatfenixAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('concatenacion', 'pedido', 'actividad', 'fecha', 'codigo', 'cantidad')
admin.site.register(matfenix, MatfenixAdmin)     

class MatPerseoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('concatenacion', 'pedido', 'actividad', 'fecha', 'codigo', 'cantidad', 'acta')
admin.site.register(matperseo, MatPerseoAdmin)

class FaltantePerseoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('concatenacion', 'pedido', 'actividad', 'fecha', 'codigo', 'cantidad', 'acta','cantidad_fenix','diferencia')
admin.site.register(faltanteperseo, FaltantePerseoAdmin)



class FaltantePerseoResource(resources.ModelResource):
    class Meta:
        model = faltanteperseo

class PerseoResource(resources.ModelResource):
    class Meta:
        model = matperseo

class FenixResource(resources.ModelResource):
    class Meta:
        model = matfenix 


admin.site.register(Stock, Stock_Admin)
admin.site.register(Material_A_Buscar, Material_A_Buscar_Admin)
admin.site.register(Acta, Acta_Admin)
admin.site.register(Oficial, OficialAdmin)
admin.site.register(Inicio, IngresoAdmin)
admin.site.register(Despacho, DespachoAdmin)
admin.site.register(Material_utilizado_perseo, Material_utilizado_perseo_Admin)
admin.site.register(Liquidacion_acta_epm, Liquidacion_acta_epm_Admin)

admin.site.register(Novedad_acta, Novedades_Admin)
admin.site.register(Ans, AnsAdmin)
admin.site.register(Encargado, EncargadoAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Actividad_epm, Actividad_epm_Admin )
