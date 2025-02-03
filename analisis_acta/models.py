from tkinter import CASCADE
from django.db import models

class ActividadLegalizacion(models.Model):
    nombre= models.CharField(max_length=200, null=True)    
    class Meta:
        ordering = ["nombre"]
        verbose_name = "Actividades legalización"
        verbose_name_plural = "Actividades legalización"
        
    def __str__(self):
        return str(self.nombre)
    
class VariableAnalisis(models.Model):
    region= models.CharField(max_length=200, null=True)
    contrato= models.CharField(max_length=200, null=True)
    
    class Meta:
        ordering = ["region"]
        verbose_name = "Variables contrato"
        verbose_name_plural = "Variables contrato"
        
    def __str__(self):
        return str(self.region)+ " " + str(self.contrato)
    
class Novedad_acta(models.Model):    
    pedido = models.CharField(max_length=200, default=0, null=True)
    actividad = models.CharField(max_length=200, default=0, null=True)
    municipio = models.CharField(max_length=200, default=0, null=True)
    pagina = models.CharField(max_length=200, default=0, null=True)
    item = models.CharField(max_length=200, default=0, null=True)
    novedad = models.CharField(max_length=200, default=0, null=True)
    estado = models.CharField(max_length=100, default="Aplica", null=True)


    class Meta:
        ordering = ["actividad"]
        verbose_name = "Novedades Acta"
        verbose_name_plural = "Novedades Acta"
        
    def __str__(self):
        return str(self.pedido)+ " " + str(self.novedad)

class Acta(models.Model):    
    pedido=models.CharField(max_length=100, default=0, null=True)
    area_operativa=models.CharField(max_length=100, default=0, null=True)
    subz=models.CharField(max_length=100, default=0, null=True)
    ruta=models.CharField(max_length=100, default=0, null=True)
    municipio=models.CharField(max_length=100, default=0, null=True)
    contrato=models.CharField(max_length=100, default=0, null=True)
    acta=models.CharField(max_length=100, default=0, null=True)
    actividad=models.CharField(max_length=100, default=0, null=True)
    fecha_estado=models.CharField(max_length=100, default=0, null=True)
    pagina=models.CharField(max_length=100, default=0, null=True)
    urbrur=models.CharField(max_length=100, default=0, null=True)
    tipre=models.CharField(max_length=100, default=0, null=True)
    red_interna=models.CharField(max_length=100, default=0, null=True)
    tipo_operacion=models.CharField(max_length=100, default=0, null=True)
    descent=models.CharField(max_length=100, default=0, null=True)
    tipo=models.CharField(max_length=100, default=0, null=True)
    cobro=models.CharField(max_length=100, default=0, null=True)
    suminis=models.CharField(max_length=100, default="0", null=True)
    item_cont=models.CharField(max_length=100, default="0", null=True)
    item_res=models.CharField(max_length=100, default=0, null=True)
    cantidad=models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True)
    vlr_cliente=models.CharField(max_length=100, default=0, null=True)
    valor_costo=models.CharField(max_length=100, default=0, null=True)
    tipo_item=models.CharField(max_length=100, default=0, null=True)


    class Meta:
        ordering = ["actividad"]
        verbose_name = "Acta"
        verbose_name_plural = "Acta"
        
    def __str__(self):
        return str(self.pedido)

class Materiales(models.Model):
    material = models.CharField(max_length=100, default=0, null=True)
    
    class Meta:
        verbose_name = 'Materiales'
        verbose_name_plural = 'Materiales'

    def __str__(self):
        return str(self.material)
        

