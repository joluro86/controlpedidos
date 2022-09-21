from tkinter import CASCADE
from django.db import models

class Novedad_acta(models.Model):    
    pedido = models.CharField(max_length=200, default=0)
    actividad = models.CharField(max_length=200, default=0)
    municipio = models.CharField(max_length=200, default=0)
    pagina = models.CharField(max_length=200, default=0)
    item = models.CharField(max_length=200, default=0)
    novedad = models.CharField(max_length=200, default=0)
    estado = models.CharField(max_length=100, default="Aplica")
    tipre = models.CharField(max_length=200, default=0)


    class Meta:
        ordering = ["actividad"]
        verbose_name = "Novedades Acta"
        verbose_name_plural = "Novedades Acta"
        
    def __str__(self):
        return str(self.pedido)+ " " + str(self.novedad)

class Acta(models.Model):    
    pedido=models.CharField(max_length=100, default=0)
    area_operativa=models.CharField(max_length=100, default=0)
    subz=models.CharField(max_length=100, default=0)
    ruta=models.CharField(max_length=100, default=0)
    municipio=models.CharField(max_length=100, default=0)
    contrato=models.CharField(max_length=100, default=0)
    acta=models.CharField(max_length=100, default=0)
    actividad=models.CharField(max_length=100, default=0)
    fecha_estado=models.CharField(max_length=100, default=0)
    pagina=models.CharField(max_length=100, default=0)
    urbrur=models.CharField(max_length=100, default=0)
    tipre=models.CharField(max_length=100, default=0)
    red_interna=models.CharField(max_length=100, default=0)
    tipo_operacion=models.CharField(max_length=100, default=0)
    descent=models.CharField(max_length=100, default=0)
    tipo=models.CharField(max_length=100, default=0)
    cobro=models.CharField(max_length=100, default=0)
    suminis=models.CharField(max_length=100, default=0)
    item_cont=models.CharField(max_length=100, default=0)
    item_res=models.CharField(max_length=100, default=0)
    cantidad=models.CharField(max_length=100, default=0)
    vlr_cliente=models.CharField(max_length=100, default=0)
    valor_costo=models.CharField(max_length=100, default=0)
    tipo_item=models.CharField(max_length=100, default=0)


    class Meta:
        ordering = ["actividad"]
        verbose_name = "Acta"
        verbose_name_plural = "Acta"
        
    def __str__(self):
        return str(self.pedido)

