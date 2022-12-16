from django.db import models

class Perseo(models.Model):
    pedido=models.CharField(max_length=50, default=0)
    actividad=models.CharField(max_length=100, default=0)
    instalador=models.CharField(max_length=200, default=0)
    fecha=models.CharField(max_length=50, default=0)
    codigo=models.CharField(max_length=50, default=0)
    cantidad=models.CharField(max_length=50, default=0)
    valor=models.CharField(max_length=50, default=0)
    total=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    acta=models.CharField(max_length=50, default=0)
    descuento_de_fenix = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Perseo"
        verbose_name_plural = "Perseo"

    def calculo_descuento_fenix(self):
        if str(self.codigo[:1]).isdigit():
            pass
        else:
            self.descuento_de_fenix = self.total
        self.fecha = self.fecha[:10]
        self.save()

class Fenix(models.Model):
    pedido = models.CharField(max_length=50, default=0)
    actividad = models.CharField(max_length=100, default=0)
    urbrur = models.CharField(max_length=50, default=0)
    tipo = models.CharField(max_length=50, default=0)
    codigo = models.CharField(max_length=50, default=0)
    cantidad = models.CharField(max_length=50, default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
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
    producido=models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Producido diario"
        verbose_name_plural = "Producido diario"



class PromedioDiario(models.Model):
    instalador = models.CharField(max_length=100, default=0)
    valor_producido_mes = models.CharField(max_length=100, default=0)
    numero_de_dias_laborados = models.CharField(max_length=100, default=0)
    adicional = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonificacion_cuadrilla = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonificacion_persona = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Promedio"
        verbose_name_plural = "Promedio"

class NovedadBonificacion(models.Model):
    pedido = models.CharField(max_length=200, default=0)
    descripcion = models.CharField(max_length=200, default="--")

    class Meta:
        verbose_name = "Novedades"
        verbose_name_plural = "Novedades"





        
