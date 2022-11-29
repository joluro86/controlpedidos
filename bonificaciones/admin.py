from django.contrib import admin
from bonificaciones.models import *
from import_export.admin import ImportExportModelAdmin 
from import_export import resources

class PedidoBoniPerseo_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad','instalador','fecha','codigo','cantidad','valor','total','acta', 'descuento_de_fenix')
    class Meta:
        model = PedidoBoniPerseo
admin.site.register(PedidoBoniPerseo, PedidoBoniPerseo_Admin)

class PedidoBoniFenix_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad', 'pagina', 'tipo', 'codigo','cantidad','valor','total')
    class Meta:
        model = PedidoBoniFenix
admin.site.register(PedidoBoniFenix, PedidoBoniFenix_Admin)

class ProducidoDia_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('instalador','fecha','producido')
    class Meta:
        model = ProducidoDia
admin.site.register(ProducidoDia, ProducidoDia_Admin)

class PromedioMensual_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('instalador','fecha', 'valor_producido_mes', 'numero_de_dias_laborados', 'promedio', 'bonificacion')
    class Meta:
        model = PromedioMensual
admin.site.register(PromedioMensual, PromedioMensual_Admin )
