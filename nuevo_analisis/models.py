from django.db import models

class ItemRegla(models.Model):
    TIPO = [
        ('suministro', 'Suministro'),
        ('actividad', 'Actividad'),
        ('obra', 'Obra'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=30, choices=TIPO)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


class RelacionItemRegla(models.Model):
    COMPARADORES = [
        ('igual_a', 'Igual a'),
        ('mayor_igual_a', 'Mayor o igual a'),
        ('mayor_que', 'Mayor que'),
        ('menor_igual_a', 'Menor o igual a'),
        ('menor_que', 'Menor que'),
        ('diferente_de', 'Diferente de'),
    ]
    FACTOR=[
        ('unico','Unico'),
        ('multiple','Multiple')
    ]   
    TIPO_REQUERIDO = [
        ('suministro','Suministro'),
        ('actividad','Actividad')
    ]  
    item = models.ForeignKey(ItemRegla, on_delete=models.CASCADE, related_name='relaciones')
    requiere_cantidad = models.BooleanField(default=False)
    cantidad_requerida = models.PositiveIntegerField(default=1)
    tipo_requerido = models.CharField(max_length=30, choices=TIPO_REQUERIDO, default="suministro")
    item_requerido = models.ForeignKey(ItemRegla, on_delete=models.CASCADE, related_name='es_requerido_por')
    comparador = models.CharField(max_length=30, choices=COMPARADORES)
    factor = models.CharField(max_length=30, choices=FACTOR, default="unico")
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item} requiere {self.item_requerido} {self.get_comparador_display()} {self.cantidad}"

