# your_app_name/models.py
from django.db import models

class ItemRegla(models.Model):
    TIPO = [
        ('suminis', 'Suministro'),
        ('actividad', 'Actividad'),
        ('item_cont', 'Obra'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=30, choices=TIPO)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Ítem de Regla"
        verbose_name_plural = "Ítems de Regla"


class RelacionItemRegla(models.Model):
    COMPARADORES = [
        ('igual_a', 'Igual a'),
        ('mayor_a', 'Mayor a'),
        ('menor_a', 'Menor a'),
    ]
    FACTOR = [
        ('unico', 'Unico'),
        ('multiple', 'Multiple')
    ]
    # CONJUNTO es un campo nuevo que has añadido
    CONJUNTO = [
        ('todos', 'Todos'),
        ('uno', 'Uno')
    ]
    
    TIPO_ITEM=[ 
        ('suminis', 'Suministro'),
        ('actividad', 'Actividad'),
        ('item_cont', 'Obra'),
        ]

    objeto = models.ForeignKey(
        ItemRegla, on_delete=models.CASCADE, related_name='relaciones',
        verbose_name="Objeto Principal"
    )
    requiere_cantidad = models.BooleanField(default=False, verbose_name="¿Requiere Cantidad?")
    cantidad_condicion = models.PositiveIntegerField(default=1, verbose_name="Cantidad Condición")
    factor = models.CharField(max_length=30, choices=FACTOR, verbose_name="Factor de Búsqueda")
    
    # ¡IMPORTANTE! Asegúrate de que el max_length sea suficiente
    # para el formato "200410,200411". 30 es muy corto para esto.
    item_busqueda = models.CharField(max_length=255, verbose_name="Ítem(s) de Búsqueda")
    tipo_item_busqueda = models.CharField(max_length=30, choices=TIPO_ITEM, default="suministro", verbose_name="Tipo Item busqueda") # Añadido verbose_name
    conjuncion = models.CharField(max_length=30, choices=CONJUNTO, default="todos", verbose_name="Condición Lógica") # Añadido verbose_name
    comparador = models.CharField(max_length=30, choices=COMPARADORES, verbose_name="Comparador")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad Requerida")

    def __str__(self):
        # Asegúrate de que los atributos 'objeto' y 'Item_busqueda' existan
        # en el momento de llamar a __str__.
        # Si 'item' o 'item_requerido' no son atributos de este modelo,
        # usa 'objeto' y 'Item_busqueda' que sí lo son.
        return f"{self.objeto.nombre} requiere {self.item_busqueda} {self.get_comparador_display()} {self.cantidad}"

    class Meta:
        verbose_name = "Relación de Ítem de Regla"
        verbose_name_plural = "Relaciones de Ítems de Regla"