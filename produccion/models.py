from django.db import models

# Create your models here.
class Valor_referencia(models.Model):
    valor = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Valor referencia'
        verbose_name_plural = 'Valor referencia'



class Perseo_produccion(models.Model):
    pedido= models.CharField(max_length=50, default=0)
    actividad= models.CharField(max_length=100, default=0)
    instalador= models.CharField(max_length=200, default=0)
    fecha= models.DateField(default=0)
    codigo= models.CharField(max_length=50, default=0)
    cantidad= models.DecimalField(decimal_places=3, max_digits=10)
    valor= models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    total= models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    acta=models.CharField(max_length=50, default=0)
    
    class Meta:
        verbose_name = 'Produccion Perseo'
        verbose_name_plural = 'Produccion Perseo'
        db_table = 'Produccion Perseo'

class NovedadProduccion(models.Model):
    pedido = models.ForeignKey(Perseo_produccion, on_delete=models.CASCADE)
    novedad= models.CharField(max_length=200, null=False)
    
    class Meta:
        verbose_name = 'Produccion novedades'
        verbose_name_plural = 'Produccion novedades'
        db_table = 'Produccion novedades'
        
class Dia_dia(models.Model):
    instalador = models.CharField(max_length=200)
    fecha = models.DateField()
    mano_obra= models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    materiales = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    valor_referencia = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    producido = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    treinta_porciento = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    por_persona = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    
    class Meta:

        verbose_name = 'Produccion dia dia'
        verbose_name_plural = 'Produccion dia dia'
        db_table = 'Produccion dia dia'
        

    
    
