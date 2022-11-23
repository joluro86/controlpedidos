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
    pedido=models.CharField(max_length=50, default=0)
    actividad=models.CharField(max_length=100, default=0)
    instalador=models.CharField(max_length=200, default=0)
    fecha=models.CharField(max_length=50, default=0)
    codigo=models.CharField(max_length=50, default=0)
    cantidad=models.CharField(max_length=50, default=0)
    valor=models.CharField(max_length=50, default=0)
    total=models.CharField(max_length=50, default=0)

    class Meta:
        verbose_name = "Fénix"
        verbose_name_plural = "Fénix"

class ValorBonificacion(models.Model):
    pedido=models.CharField(max_length=50, default=0)
    instalador=models.CharField(max_length=100, default=0)
    fecha=models.CharField(max_length=100, default=0)
    valor_fenix=models.CharField(max_length=50, default=0)
    valor_perseo=models.CharField(max_length=50, default=0)
    bonificacion=models.CharField(max_length=50, default=0)

    class Meta:
        verbose_name = "Valor Bonificacion"
        verbose_name_plural = "Valor Bonificacion"
