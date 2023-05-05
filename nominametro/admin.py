from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
from import_export import resources

from nominametro.models import Cargo, Concepto, Novedad_nomina, plantilla, prenomina, Mejia

class StockBuscarResource(resources.ModelResource):
    class Meta:
        model = prenomina

class prenomina_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('empleado','nombre_del_empleado', 'descripción_del_turno','concepto','nombre_del_concepto','préstamo','salario_básico_hora','tiempo','valor')
    class Meta:
        model = prenomina

admin.site.register(prenomina, prenomina_Admin)

class StockBuscarResource(resources.ModelResource):
    class Meta:
        model = Mejia

class mejia_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nit',)
    class Meta:
        model = Mejia

admin.site.register(Mejia, mejia_Admin)


class StockBuscarResource(resources.ModelResource):
    class Meta:
        model = prenomina

class Plantilla_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nit', 'cedula','nombre', 'apellido')
    class Meta:
        model = plantilla

admin.site.register(plantilla, Plantilla_Admin)

class Concepto_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('concepto','conversor', 'factor', 'tipo')
    class Meta:
        model = Concepto

admin.site.register(Concepto, Concepto_Admin)

class Novedad_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('empleado','novedad')
    class Meta:
        model = Novedad_nomina

admin.site.register(Novedad_nomina, Novedad_Admin)

class Cargo_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cedula','cargo')
    class Meta:
        model = Cargo

admin.site.register(Cargo, Cargo_Admin)



