from django.db import models

class ActaSello(models.Model):    
    pedido = models.CharField(max_length=50, null=True)
    municipio = models.CharField(max_length=50, null=True)
    actividad = models.CharField(max_length=50, null=True)
    fecha = models.CharField(max_length=50, null=True)
    pagina = models.CharField(max_length=50, null=True)
    cantidad = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Acta sellos'
        verbose_name_plural = 'Acta sellos'
        
class MaterialInstalado(models.Model):
    consecutivo = models.CharField(max_length=50, null=True)
    pedido = models.CharField(max_length=50, null=True)
    esta_en_acta = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Materiales instalados'
        verbose_name_plural = 'Materiales instalados'
        
class SerieSello(models.Model):
    consecutivo = models.CharField(max_length=50, null=True)  
    serie = models.CharField(max_length=50, null=True)  
    pedido = models.CharField(max_length=50, null=True)  
    instalador = models.CharField(max_length=50, null=True)  
    va_en_informe = models.BooleanField(default=False)
       

    class Meta:
        verbose_name = "Serie sello"
        verbose_name_plural = "Series Sellos"



    