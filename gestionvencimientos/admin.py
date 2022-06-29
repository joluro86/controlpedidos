from django.contrib import admin
from gestionvencimientos.models import Actividad, Actividad_epm, Ans, Encargado
from import_export.admin import ImportExportModelAdmin 
from import_export import resources


# Register your models here.

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
    
admin.site.register(Ans, AnsAdmin)
admin.site.register(Encargado, EncargadoAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Actividad_epm, Actividad_epm_Admin )
