from django.db import models

# Create your models here.
class Valor_referencia(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Valor referencia'
        verbose_name_plural = 'Valor referencia'



class Perseo_produccion(models.Model):
    pedido=models.CharField(max_length=50, default=0)
    actividad=models.CharField(max_length=100, default=0)
    instalador=models.CharField(max_length=200, default=0)
    fecha=models.DateField(default=0)
    codigo=models.CharField(max_length=50, default=0)
    cantidad=models.DecimalField(decimal_places=3, max_digits=10)
    valor=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
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
    mano_obra= models.IntegerField(default=0)
    materiales = models.IntegerField(default=0)
    valor_referencia = models.IntegerField(default=0)
    producido = models.IntegerField(default=0)
    treinta_porciento = models.IntegerField(default=0)
    por_persona = models.IntegerField(default=0)
    
    class Meta:

        verbose_name = 'Produccion dia dia'
        verbose_name_plural = 'Produccion dia dia'
        db_table = 'Produccion dia dia'
        

    
    
