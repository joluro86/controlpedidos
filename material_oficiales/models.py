from django.db import models


class Oficial(models.Model):
    nombre = models.CharField(verbose_name='Oficial', max_length=500)
    
    class Meta:
        verbose_name = 'Oficial'
        verbose_name_plural = 'Oficiales'

    def __str__(self):
        return str(self.nombre)

class Inicio(models.Model):
    encargado = models.CharField(verbose_name='Oficial', max_length=500)
    codigo = models.CharField(verbose_name='Código', max_length=100)
    cantidad = models.CharField(verbose_name='Cantidad', max_length=100)
    
    class Meta:
        verbose_name = 'Cantidadi Inicio Oficial'
        verbose_name_plural = 'Cantidad Inicio Oficial'

    def __str__(self):
        return str(self.encargado) + " tiene de " + str(self.codigo)+ " " + str(self.cantidad)

class Despacho(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=100)
    fecha = models.CharField(verbose_name='Fecha', max_length=500)
    encargado = models.CharField(verbose_name='Encargado', max_length=500, default='0')
    cantidad = models.CharField(verbose_name='Cantidad', max_length=100, default='0')
    
    class Meta:
        verbose_name = 'Despacho oficial'
        verbose_name_plural = 'Despachos oficiales'

    def __str__(self):
        return str(self.codigo)

class Reintegro(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=100)
    fecha = models.CharField(verbose_name='Fecha', max_length=500)
    encargado = models.CharField(verbose_name='Encargado', max_length=500, default='0')
    cantidad = models.CharField(verbose_name='Cantidad', max_length=100, default='0')
    
    class Meta:
        verbose_name = 'Reintegro oficial'
        verbose_name_plural = 'Reintegros oficiales'

    def __str__(self):
        return str(self.codigo)

class Liquidacion_acta_epm(models.Model):
    pedido = models.CharField(verbose_name='Pedido', max_length=10)
    actividad = models.CharField(verbose_name='Actividad', max_length=500)
    item_cont = models.CharField(verbose_name='item_cont', max_length=100)
    cantidad = models.CharField(verbose_name='Cantidad', max_length=100)
    encargado = models.CharField(verbose_name='Encargado', max_length=100, default='0')
    conc_pedido_codigo = models.CharField(verbose_name='concatenacion', max_length=100, default='0')
    
    class Meta:
        verbose_name = 'Liquidación Acta Epm'
        verbose_name_plural = 'Liquidación Acta Epm'

    def __str__(self):
        return str(self.pedido)

class Material_utilizado_perseo(models.Model):
    pedido = models.CharField(verbose_name='Pedido', max_length=10)
    actividad = models.CharField(verbose_name='Actividad', max_length=500, default='0')
    instalador = models.CharField(verbose_name='Instalador', max_length=500)
    fecha = models.CharField(verbose_name='Fecha', max_length=100)
    codigo = models.CharField(verbose_name='Código', max_length=100)
    cantidad = models.CharField(verbose_name='Cantidad', max_length=100, default='0')
    conc_pedido_codigo = models.CharField(verbose_name='concatenacion', max_length=100, default='0')
    
    class Meta:
        verbose_name = 'Material Utilizado Perseo'
        verbose_name_plural = 'Material Utilizado Perseo'

    def __str__(self):
        return str(self.pedido) + str(self.instalador)

class Material_A_Buscar(models.Model):
    nombre = models.CharField(verbose_name='Oficial', max_length=500, default='--')
    
    class Meta:
        verbose_name = 'Material a buscar'
        verbose_name_plural = 'Material a buscar'

    def __str__(self):
        return str(self.nombre)

class Stock(models.Model):
    encargado = models.CharField(verbose_name='Oficial', default='0', max_length=300)
    codigo = models.CharField(verbose_name='Código', default='0', max_length=100)
    inicio = models.CharField(verbose_name='Inicio', default='0', max_length=100)
    despachado = models.CharField(verbose_name='Despachado', default='0', max_length=100)
    reintegrado = models.CharField(verbose_name='Reintegrado', default='0', max_length=100)
    epm = models.CharField(verbose_name='Epm', default='0', max_length=100)
    diferencia = models.CharField(verbose_name='Diferencia', default='0', max_length=100)

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'

    def __str__(self):
        return str(self.codigo)+": "+str(self.diferencia)


