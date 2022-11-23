from django.contrib import admin
from bonificaciones.models import *
from import_export.admin import ImportExportModelAdmin 
from import_export import resources

class PedidoBoniPerseo_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad','instalador','fecha','codigo','cantidad','valor','total','acta')
    class Meta:
        model = PedidoBoniPerseo
admin.site.register(PedidoBoniPerseo, PedidoBoniPerseo_Admin)

class PedidoBoniFenix_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad','instalador','fecha','codigo','cantidad','valor','total')
    class Meta:
        model = PedidoBoniFenix
admin.site.register(PedidoBoniFenix, PedidoBoniFenix_Admin)

class ValorBonificacion_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','instalador','fecha','valor_fenix','valor_perseo', 'bonificacion')
    class Meta:
        model = ValorBonificacion
admin.site.register(ValorBonificacion, ValorBonificacion_Admin)
