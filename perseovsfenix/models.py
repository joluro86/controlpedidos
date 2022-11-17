from django.db import models

class NumeroActa(models.Model):
    numero= models.IntegerField()

    class Meta:
        verbose_name = 'Acta actual'
        verbose_name_plural = 'Acta actual'

    def __str__(self):
        return str('Acta # ' + str(self.numero))

class Guia(models.Model):
    nombre_perseo = models.CharField(verbose_name='Nombre Perseo', max_length=100)
    nombre_fenix = models.CharField(verbose_name='Nombre Fenix', max_length=100)
    
    class Meta:
        verbose_name = 'guia'
        verbose_name_plural = 'guias'

    def __str__(self):
        return str(self.nombre_perseo)

class matperseo(models.Model):
    pedido=models.CharField(verbose_name='Pedido', max_length=10)
    actividad=models.CharField(verbose_name='Actividad', max_length=500)
    fecha=models.CharField(verbose_name='Fecha', max_length=100)
    codigo=models.CharField(verbose_name='Código', max_length=100)
    cantidad=models.DecimalField(verbose_name='Cantidad', decimal_places=2, default=0, max_digits=6)   
    acta= models.CharField(verbose_name='Acta', max_length=100, default='0') 
    concatenacion= models.CharField(verbose_name='Concat', max_length=100, default="0")

    class Meta:
        db_table = 'perseo'
        verbose_name = 'Material Perseo'
        verbose_name_plural = 'Material Perseo'
        ordering = ['fecha']

    def __str__(self):
        return str(self.pedido)

class matfenix(models.Model):
    pedido=models.CharField(verbose_name='Pedido', max_length=10)
    actividad=models.CharField(verbose_name='Actividad', max_length=500)
    fecha=models.CharField(verbose_name='Fecha', max_length=100)
    codigo=models.CharField(verbose_name='Código', max_length=100)
    cantidad=models.DecimalField(verbose_name='Cantidad', decimal_places=2, default=0, max_digits=6)    
    concatenacion= models.CharField(verbose_name='Concat', max_length=100, default="0")
    enperseo = models.IntegerField(default=0) 

    class Meta:
        db_table = 'fenix'
        verbose_name = 'Material Fenix'
        verbose_name_plural = 'Material Fenix'
        ordering = ['fecha']

    def __str__(self):
        return str(self.pedido)

class NovedadPerseoVsFenix(models.Model):
    concatenacion= models.CharField(verbose_name='Concat', max_length=100, default="0")
    pedido=models.CharField(verbose_name='Pedido', max_length=10)
    actividad=models.CharField(verbose_name='Actividad', max_length=500)
    fecha=models.CharField(verbose_name='Fecha', max_length=100)
    codigo=models.CharField(verbose_name='Código', max_length=100)
    cantidad=models.DecimalField(verbose_name='Cantidad', decimal_places=2, default=0, max_digits=6)   
    acta= models.CharField(verbose_name='Acta', max_length=100, default=0)  
    observacion = models.CharField(verbose_name='Observación', max_length=200, default="-")
    cantidad_fenix=models.DecimalField(verbose_name='Can Fenix', decimal_places=2, default=0, max_digits=6) 
    diferencia=models.DecimalField(verbose_name='Diferencia', decimal_places=2, default=0, max_digits=6)

    class Meta:
        db_table = 'faltanteperseo'
        verbose_name = 'Faltante Perseo'
        verbose_name_plural = 'Faltante Perseo'
        ordering = ['fecha']

    def __str__(self):
        return str(self.pedido)


