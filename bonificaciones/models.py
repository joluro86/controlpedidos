from django.db import models

class PedidoBoniPerseo(models.Model):
    pedido=models.CharField(max_length=50, default=0)
    actividad=models.CharField(max_length=100, default=0)
    instalador=models.CharField(max_length=200, default=0)
    fecha=models.CharField(max_length=50, default=0)
    codigo=models.CharField(max_length=50, default=0)
    cantidad=models.CharField(max_length=50, default=0)
    valor=models.CharField(max_length=50, default=0)
    total=models.CharField(max_length=50, default=0)
    acta=models.CharField(max_length=50, default=0)

    class Meta:
        verbose_name = "Perseo"
        verbose_name_plural = "Perseo"

class PedidoBoniFenix(models.Model):
    pedido = models.CharField(max_length=50, default=0)
    actividad = models.CharField(max_length=100, default=0)
    pagina = models.CharField(max_length=50, default=0)
    urbrur = models.CharField(max_length=50, default=0)
    tipo = models.CharField(max_length=50, default=0)
    codigo = models.CharField(max_length=50, default=0)
    cantidad = models.CharField(max_length=50, default=0)
    valor = models.CharField(max_length=50, default=0)
    total = models.CharField(max_length=50, default=0)
    instalador = models.CharField(max_length=100, default=0)
    fecha=models.CharField(max_length=50, default=0)

    class Meta:
        verbose_name = "Fénix"
        verbose_name_plural = "Fénix"

class ValorBonificacion(models.Model):
    pedido=models.CharField(max_length=50, default=0)
    instalador=models.CharField(max_length=100, default=0)
    fecha=models.CharField(max_length=100, default=0)
    valor_fenix=models.CharField(max_length=50, default=0)
    valor_perseo=models.CharField(max_length=50, default=0)
    diferencia=models.CharField(max_length=50, default=0)

    class Meta:
        verbose_name = "Pedido Bonificación"
        verbose_name_plural = "Pedido Bonificación"

class BonificacionDia(models.Model):
    instalador=models.CharField(max_length=100, default=0)
    fecha=models.CharField(max_length=100, default=0)
    laborado=models.CharField(max_length=50, default=0)
    bonificacion=models.CharField(max_length=50, default=0)

    class Meta:
        verbose_name = "Bonificación diaria"
        verbose_name_plural = "Bonificaciones diarias"

class ActividadBon(models.Model):
    nombre = models.CharField(max_length=100, default=0)

    class Meta:
        verbose_name = "Actividad Bon"
        verbose_name_plural = "Actividades Bon"

class DatosBon(models.Model):
    nombre = models.CharField(max_length=100, default=0)
    valor = models.CharField(max_length=100, default=0)

    class Meta:
        verbose_name = "Datos Bon"
        verbose_name_plural = "Datos Bon"

class RangoFechas(models.Model):
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        verbose_name = "Rango fechas"
        verbose_name_plural = "Rango fechas"

class PromedioDiario(models.Model):
    instalador = models.CharField(max_length=100, default=0)
    fecha = models.DateField()
    valor_producido_mes = models.CharField(max_length=100, default=0)
    numero_de_dias_laborados = models.CharField(max_length=100, default=0)
    promedio = models.CharField(max_length=100, default=0)
    bonificacion = models.CharField(max_length=100, default=0)

    class Meta:
        verbose_name = "Promedio diario"
        verbose_name_plural = "Promedio diario"





        
