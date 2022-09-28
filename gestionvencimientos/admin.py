from django.contrib import admin
from gestionvencimientos.models import *
from import_export.admin import ImportExportModelAdmin 
from import_export import resources

class EncargadoResource(resources.ModelResource):
    class Meta:
        model = Encargado

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

class GuiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre_perseo', 'nombre_fenix')

class NumeroActaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class MatfenixAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('concatenacion', 'pedido', 'actividad', 'fecha', 'codigo', 'cantidad')

class MatPerseoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('concatenacion', 'pedido', 'actividad', 'fecha', 'codigo', 'cantidad', 'acta')

class FaltantePerseoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('concatenacion', 'pedido', 'actividad', 'fecha', 'codigo', 'cantidad', 'acta','cantidad_fenix','diferencia')

class FaltantePerseoResource(resources.ModelResource):
    class Meta:
        model = faltanteperseo

class PerseoResource(resources.ModelResource):
    class Meta:
        model = matperseo

class FenixResource(resources.ModelResource):
    class Meta:
        model = matfenix 

admin.site.register(Guia, GuiaAdmin)
admin.site.register(Ans, AnsAdmin)
admin.site.register(Encargado, EncargadoAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Actividad_epm, Actividad_epm_Admin )
admin.site.register(faltanteperseo, FaltantePerseoAdmin)
admin.site.register(matperseo, MatPerseoAdmin)
admin.site.register(NumeroActa, NumeroActaAdmin)
admin.site.register(matfenix, MatfenixAdmin)     
