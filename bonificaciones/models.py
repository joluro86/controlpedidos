from django.db import models

class Perseo(models.Model):
    pedido=models.CharField(max_length=50, default=0)
    actividad=models.CharField(max_length=100, default=0)
    instalador=models.CharField(max_length=200, default=0)
    fecha=models.CharField(max_length=50, default=0)
    codigo=models.CharField(max_length=50, default=0)
    cantidad=models.CharField(max_length=50, default=0)
    valor=models.CharField(max_length=50, default=0)
    total=models.CharField(max_length=50, default=0)
    acta=models.CharField(max_length=50, default=0)
    descuento_de_fenix = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Perseo"
        verbose_name_plural = "Perseo"

class Fenix(models.Model):
    pedido = models.CharField(max_length=50, default=0)
    actividad = models.CharField(max_length=100, default=0)
    urbrur = models.CharField(max_length=50, default=0)
    tipo = models.CharField(max_length=50, default=0)
    codigo = models.CharField(max_length=50, default=0)
    cantidad = models.CharField(max_length=50, default=0)
    valor = models.CharField(max_length=50, default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    instalador = models.CharField(max_length=100, default=0)
    fecha=models.CharField(max_length=50, default=0)

    class Meta:
        verbose_name = "Fénix"
        verbose_name_plural = "Fénix"

class ProducidoDia(models.Model):
    instalador=models.CharField(max_length=100, default=0)
    fecha=models.CharField(max_length=100, default=0)
    valor_fenix = models.CharField(max_length=100, default=0)
    valor_perseo_descuento = models.CharField(max_length=100, default=0)
    producido=models.CharField(max_length=50, default=0)

    class Meta:
        verbose_name = "Producido diario"
        verbose_name_plural = "Producido diario"


class PromedioMensual(models.Model):
    instalador = models.CharField(max_length=100, default=0)
    fecha = models.DateField()
    valor_producido_mes = models.CharField(max_length=100, default=0)
    numero_de_dias_laborados = models.CharField(max_length=100, default=0)
    promedio = models.CharField(max_length=100, default=0)
    bonificacion = models.CharField(max_length=100, default=0)

    class Meta:
        verbose_name = "Promedio mensual"
        verbose_name_plural = "Promedio mensual"

class NovedadBonificacion(models.Model):
    pedido = models.CharField(max_length=200, default=0)
    descripcion = models.CharField(max_length=200, default="--")

    class Meta:
        verbose_name = "Novedades"
        verbose_name_plural = "Novedades"





        
