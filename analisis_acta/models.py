from tkinter import CASCADE
from django.db import models
from django.db.models import Sum

class ActividadLegalizacion(models.Model):
    nombre= models.CharField(max_length=200, null=True)    
    class Meta:
        ordering = ["nombre"]
        verbose_name = "Actividades legalización"
        verbose_name_plural = "Actividades legalización"
        
    def __str__(self):
        return str(self.nombre)
    
class VariableAnalisis(models.Model):
    region= models.CharField(max_length=200, null=True)
    contrato= models.CharField(max_length=200, null=True)
    codigo_sellos= models.CharField(max_length=200, null=True)
    
    class Meta:
        ordering = ["region"]
        verbose_name = "Variables contrato"
        verbose_name_plural = "Variables contrato"
        
    def __str__(self):
        return str(self.region)+ " " + str(self.contrato)
    
class Novedad_acta(models.Model):    
    pedido = models.CharField(max_length=200, default=0, null=True)
    actividad = models.CharField(max_length=200, default=0, null=True)
    municipio = models.CharField(max_length=200, default=0, null=True)
    pagina = models.CharField(max_length=200, default=0, null=True)
    item = models.CharField(max_length=200, default=0, null=True)
    novedad = models.CharField(max_length=200, default=0, null=True)
    estado = models.CharField(max_length=100, default="Aplica", null=True)
    fecha = models.CharField(max_length=100, default="Sin fecha", null=True)

    class Meta:
        ordering = ["actividad"]
        verbose_name = "Novedades Acta"
        verbose_name_plural = "Novedades Acta"
        unique_together = ('pedido', 'novedad')
        
    def __str__(self):
        return str(self.pedido)+ " " + str(self.novedad)

class Acta(models.Model):    
    pedido=models.CharField(max_length=100, default=0, null=True)
    area_operativa=models.CharField(max_length=100, default=0, null=True)
    subz=models.CharField(max_length=100, default=0, null=True)
    ruta=models.CharField(max_length=100, default=0, null=True)
    municipio=models.CharField(max_length=100, default=0, null=True)
    contrato=models.CharField(max_length=100, default=0, null=True)
    acta=models.CharField(max_length=100, default=0, null=True)
    actividad=models.CharField(max_length=100, default=0, null=True)
    fecha_estado=models.CharField(max_length=100, default=0, null=True)
    pagina=models.CharField(max_length=100, default=0, null=True)
    urbrur=models.CharField(max_length=100, default=0, null=True)
    tipre=models.CharField(max_length=100, default=0, null=True)
    red_interna=models.CharField(max_length=100, default=0, null=True)
    tipo_operacion=models.CharField(max_length=100, default=0, null=True)
    descent=models.CharField(max_length=100, default=0, null=True)
    tipo=models.CharField(max_length=100, default=0, null=True)
    cobro=models.CharField(max_length=100, default=0, null=True)
    suminis=models.CharField(max_length=100, default="0", null=True)
    item_cont=models.CharField(max_length=100, default="0", null=True)
    item_res=models.CharField(max_length=100, default=0, null=True)
    cantidad=models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True)
    vlr_cliente=models.CharField(max_length=100, default=0, null=True)
    valor_costo=models.CharField(max_length=100, default=0, null=True)
    tipo_item=models.CharField(max_length=100, default=0, null=True)


    class Meta:
        ordering = ["actividad"]
        verbose_name = "Acta"
        verbose_name_plural = "Acta"
        
    def __str__(self):
        return str(self.pedido)

class Materiales(models.Model):
    material = models.CharField(max_length=100, default=0, null=True)
    
    class Meta:
        verbose_name = 'Materiales'
        verbose_name_plural = 'Materiales'

    def __str__(self):
        return str(self.material)
    

from django.db.models import Sum

from django.db import models
from django.db.models import Sum

class CantidadItem(models.Model):
    TIPO_RESTRICCION = [
        ('EXACTO', 'Exacto'),
        ('MAXIMO', 'Máximo'),
    ]

    item = models.CharField("Item cobro", max_length=50)
    cantidad_cobro = models.IntegerField()  # La cantidad máxima o exacta
    tipo_restriccion = models.CharField(
        max_length=10, choices=TIPO_RESTRICCION, default='EXACTO'
    )  # Definir si es exacto, máximo o rango
    max_cantidad = models.IntegerField(null=True, blank=True)  # Para rango máximo

    class Meta:
        verbose_name = 'Cantidades Items'
        verbose_name_plural = 'Cantidades Items'

    def verificar_cantidad(self, pedido, cantidad):
        """Verifica si la cantidad cumple con la restricción definida y devuelve un mensaje en caso de error"""
        suma_cantidad = Acta.objects.filter(
            pedido=pedido,
            item_cont=self.item
        ).aggregate(suma=Sum('cantidad'))['suma'] or 0  # Si no hay valores, usa 0

        # Lógica de verificación según el tipo de restricción
        if self.tipo_restriccion == 'Exacto':
            if suma_cantidad != cantidad:
                return f"La cantidad cobrada ({suma_cantidad}) no coincide con la cantidad exacta requerida ({cantidad})."
        
        elif self.tipo_restriccion == 'Máximo':
            if suma_cantidad > self.cantidad_cobro:
                return f"La cantidad cobrada ({suma_cantidad}) excede el máximo permitido ({self.cantidad_cobro})."
        
        return None  # Si todo está bien, no hay mensaje de error


    @classmethod
    def crear_cantidad_item(cls, item_nuevo, cantidad, tipo_restriccion='EXACTO', min_cantidad=None, max_cantidad=None):
        cantidad_item, creado = cls.objects.get_or_create(
            item=item_nuevo,
            defaults={'cantidad_cobro': cantidad, 'tipo_restriccion': tipo_restriccion, 'min_cantidad': min_cantidad, 'max_cantidad': max_cantidad}
        )

        if not creado:  # Si ya existe, actualiza los valores
            cantidad_item.cantidad_cobro = cantidad
            cantidad_item.tipo_restriccion = tipo_restriccion
            if min_cantidad is not None:
                cantidad_item.min_cantidad = min_cantidad
            if max_cantidad is not None:
                cantidad_item.max_cantidad = max_cantidad
            cantidad_item.save()

        return cantidad_item
           

class RelacionItem(models.Model):
    item = models.ForeignKey(Acta, on_delete=models.CASCADE)
    item_relacion = models.CharField(max_length=30)
    
    def verificar_relacion(self):
        return Acta.objects.filter(pedido=self.item.pedido, 
                            item_cont=self.item_relacion).aggregate(suma=Sum('cantidad'))<1
    

