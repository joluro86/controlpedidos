from django.contrib import admin
import import_export
from gestionvencimientos.models import Actividad, Ans, Encargado, Municipio, Vencido
from import_export.admin import ImportExportModelAdmin 
from import_export import resources


# Register your models here.
class AnsResource(resources.ModelResource):
    class Meta:
        model = Ans

class ActividadResource(resources.ModelResource):
    class Meta:
        model = Actividad

class AnsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('Pedido', 'Actividad', 'Fecha_Inicio_ANS', 'dias_vencimiento' , 'Area_Trabajo', 'fecha_vencimiento')
    resource_class = AnsResource
    list_filter = ('Estado',)
    search_fields = ['Pedido', 'Actividad', 'Area_Trabajo']
    
class EncargadoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    class Meta:
        model = Encargado

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre','encargado','dias_urbano', 'dias_rural')
    class Meta:
        model = Actividad
        
class VencidoAdmin(admin.ModelAdmin):
    list_display = ('Pedido','Actividad','fecha_cierre')
    class Meta:
        model = Vencido

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    class Meta:
        model = Municipio
    
admin.site.register(Ans, AnsAdmin)
admin.site.register(Encargado, EncargadoAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Vencido, VencidoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
