from django.contrib import admin
from gestionvencimientos.models import *
from import_export.admin import ImportExportModelAdmin 
from sellos.models import ActaSello, MaterialInstalado, SerieSello

class ActaSelloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','cantidad')
    class Meta:
        model = ActaSello
        
class MaterialInstaladoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','esta_en_acta')
    class Meta:
        model = MaterialInstalado
        
class SerieSelloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pedido','va_en_informe')
    class Meta:
        model = SerieSello
        

admin.site.register(ActaSello, ActaSelloAdmin)
admin.site.register(MaterialInstalado, MaterialInstaladoAdmin)
admin.site.register(SerieSello, SerieSelloAdmin)
