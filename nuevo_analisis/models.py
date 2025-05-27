from django.db import models

class ReglaItemActividad(models.Model):
    COMPARADORES = [
        ('==', 'Igual a'),
        ('>=', 'Mayor o igual a'),
        ('>', 'Mayor que'),
        ('<=', 'Menor o igual a'),
        ('<', 'Menor que'),
        ('!=', 'Diferente de'),
    ]

    nombre = models.CharField(max_length=100)
    item_cont = models.CharField(max_length=50, help_text="Código de actividad (campo item_cont)")
    suminis_requerido = models.CharField(max_length=50, help_text="Código de suministro requerido (campo suminis)")
    comparador = models.CharField(max_length=2, choices=COMPARADORES, default='==')
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Si hay actividad {self.item_cont}, debe haber suministro {self.suminis_requerido} {self.comparador} {self.cantidad}"

class ReglaSuministro(models.Model):
    COMPARADORES = [
        ('==', 'Igual a'),
        ('>=', 'Mayor o igual a'),
        ('>', 'Mayor que'),
        ('<=', 'Menor o igual a'),
        ('<', 'Menor que'),
        ('!=', 'Diferente de'),
    ]

    nombre = models.CharField(max_length=100)
    suminis_origen = models.CharField(max_length=50, help_text="Suministro que activa la regla")
    requiere_suminis = models.CharField(max_length=50, blank=True, null=True, help_text="Otro suministro que se requiere")
    requiere_item_cont = models.CharField(max_length=50, blank=True, null=True, help_text="O una actividad (item_cont) que se requiere")
    comparador = models.CharField(max_length=2, choices=COMPARADORES, default='==')
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        destino = self.requiere_suminis or self.requiere_item_cont
        return f"Si hay suministro {self.suminis_origen}, debe haber {destino} {self.comparador} {self.cantidad}"
