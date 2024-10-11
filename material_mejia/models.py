from django.db import models

class Pedido(models.Model):
    pedido = models.CharField(max_length=255)  # Columna D
    actividad = models.CharField(max_length=255)  # Columna L
    instalador = models.CharField(max_length=255)  # Columna M
    codigo = models.CharField(max_length=255)  # Columna S
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)  # Columna U
    fecha = models.DateField()  # Columna Z
    acta = models.CharField(max_length=255)  # Columna AA

    def __str__(self):
        return f"Pedido {self.pedido} - {self.actividad}"
    

class ActaB(models.Model):
    pedido = models.CharField(max_length=255)  # Columna A
    actividad = models.CharField(max_length=255)  # Columna H
    codigo = models.CharField(max_length=255)  # Columna S o R
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)  # Columna U

    def __str__(self):
        return f"Acta {self.pedido} - Código {self.codigo}"

    

class MaterialSeleccionado(models.Model):
    codigo = models.CharField(max_length=255)  # Campo para el código de material
    guia = models.CharField(max_length=255)    # Campo para la guía (el semejante en Acta)

    def __str__(self):
        return f"Material {self.codigo} - Guía {self.guia}"

from django.db import models

class ComparacionPedido(models.Model):
    pedido = models.CharField(max_length=255)  # Tomado del modelo Pedido
    codigo = models.CharField(max_length=255)  # Tomado del modelo Pedido    
    suma_material_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Puede ser cero
    suma_material_acta = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Puede ser cero
    diferencia = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Diferencia entre acta y pedido
    observacion = models.TextField(blank=True, null=True)  # Campo opcional para observaciones
    actividad = models.CharField(max_length=255)  # Tomado del modelo Pedido
    fecha = models.DateField(null=True, blank=True)  # Tomado del modelo Pedido
    instalador = models.CharField(max_length=255)  # Tomado del modelo Pedido

    def __str__(self):
        return f"Comparación Pedido {self.pedido} - Diferencia {self.diferencia}"


