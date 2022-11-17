from django.contrib import admin
from Analisis_acta.models import *
from import_export.admin import ImportExportModelAdmin 
from import_export import resources

from perseovsfenix.models import *

### NUMERO ACTA
class NumeroActaResource(resources.ModelResource):
    list_display = ('numero',)
    class Meta:
        model = NumeroActa

class NumeroActa_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('numero',)
    class Meta:
        model = Novedad_acta

admin.site.register(NumeroActa, NumeroActa_Admin)

#### MATERIAL PERSEO
class MatPerseoResource(resources.ModelResource):
    list_display = ('pedido','actividad', 'fecha', 'codigo', 'cantidad', 'concatenacion')
    class Meta:
        model = matperseo

class MatPerseo_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad', 'fecha', 'codigo', 'cantidad', 'acta', 'concatenacion')
    class Meta:
        model = matperseo

admin.site.register(matperseo, MatPerseo_Admin)

#### MATERIAL FENIX
class MatFenixResource(resources.ModelResource):
    list_display = ('numero',)
    class Meta:
        model = matfenix

class MatFenix_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','actividad', 'fecha', 'codigo', 'cantidad', 'concatenacion')
    class Meta:
        model = matfenix

admin.site.register(matfenix, MatFenix_Admin)

#### NOVEDAD PERSEO VS FENIX
class NovedadPerseoVsFenixResource(resources.ModelResource):
    list_display = ( 'concatenacion', 'pedido','actividad', 'fecha', 'codigo', 'cantidad', 'acta', 'observacion', 'cantidad_fenix', 'diferencia')
    class Meta:
        model = NovedadPerseoVsFenix

class NovedadPerseoVsFenix_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ( 'concatenacion', 'pedido','actividad', 'fecha', 'codigo', 'cantidad', 'acta', 'observacion', 'cantidad_fenix', 'diferencia')
    class Meta:
        model = NovedadPerseoVsFenix

admin.site.register(NovedadPerseoVsFenix, NovedadPerseoVsFenix_Admin)
