from django.contrib import admin
from bonificaciones.models import *
from import_export.admin import ImportExportModelAdmin 
from import_export import resources

class PedidoBoniPerseo_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad','instalador','fecha','codigo','cantidad','valor','total','acta', 'descuento_de_fenix')
    class Meta:
        model = Perseo
admin.site.register(Perseo, PedidoBoniPerseo_Admin)

class PedidoBoniFenix_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad', 'tipo', 'codigo','cantidad','valor','total')
    class Meta:
        model = Fenix
admin.site.register(Fenix, PedidoBoniFenix_Admin)

class ProducidoDia_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('instalador','fecha','producido')
    class Meta:
        model = ProducidoDia
admin.site.register(ProducidoDia, ProducidoDia_Admin)

class PromedioDiario_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('instalador','valor_producido_mes', 'numero_de_dias_laborados', 'adicional', 'bonificacion_cuadrilla', 'bonificacion_persona')
    class Meta:
        model = PromedioDiario
admin.site.register(PromedioDiario, PromedioDiario_Admin )

class NovedadBonificacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('descripcion','pedido')
    class Meta:
        model = NovedadBonificacion
admin.site.register(NovedadBonificacion, NovedadBonificacionAdmin )
