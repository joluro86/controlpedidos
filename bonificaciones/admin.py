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
    list_display = ('pedido','actividad', 'pagina', 'tipo', 'codigo','cantidad','valor','total')
    class Meta:
        model = PedidoBoniFenix
admin.site.register(PedidoBoniFenix, PedidoBoniFenix_Admin)

class ValorBonificacion_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','instalador','fecha','valor_fenix','valor_perseo', 'diferencia')
    class Meta:
        model = ValorBonificacion
admin.site.register(ValorBonificacion, ValorBonificacion_Admin)

class BonificacionDia_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('instalador','fecha','laborado', 'bonificacion')
    class Meta:
        model = BonificacionDia
admin.site.register(BonificacionDia, BonificacionDia_Admin)

class ActividadBon_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre',)
    class Meta:
        model = ActividadBon
admin.site.register(ActividadBon, ActividadBon_Admin)

class DatosBon_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre','valor')
    class Meta:
        model = DatosBon
admin.site.register(DatosBon, DatosBon_Admin)

class Rancho_fecha_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('fecha_inicial','fecha_final')
    class Meta:
        model = RangoFechas
admin.site.register(RangoFechas, Rancho_fecha_Admin)

class PromedioDiario_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('instalador','fecha', 'valor_producido_mes', 'numero_de_dias_laborados', 'promedio', 'bonificacion')
    class Meta:
        model = PromedioDiario
admin.site.register(PromedioDiario, PromedioDiario_Admin)
