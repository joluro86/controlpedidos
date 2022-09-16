from tkinter import CASCADE
from django.db import models

class Ans(models.Model):    
    Pedido = models.TextField(max_length=100, default=0, null=True)
    Subped = models.CharField(max_length=100, default=0, null=True)
    Soli = models.CharField(max_length=200, null=True, default=0)
    Producto_id = models.CharField(max_length=200, null=True, default=0)
    Tipo_Trabajo = models.CharField(max_length=200, null=True, default=0)
    Tipo_Elemento_ID = models.CharField(max_length=200, null=True, default=0)
    Fecha_Recibo = models.CharField(max_length=500, default=0)
    Fecha_Ingreso_Sol = models.CharField(max_length=500, default=0)
    Fecha_Concepto = models.CharField(max_length=500, default=0)
    Fecha_Inicio_ANS = models.CharField(max_length=500, default=0)
    Días_ANS = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    Estado = models.CharField(max_length=500, null=True, default=0)
    Concepto = models.CharField(max_length=500, null=True, default=0)
    Nombre_concepto = models.CharField(max_length=500, null=True, default=0)
    ClienteID = models.CharField(max_length=500, null=True, default=0)
    Nombre_Cliente = models.CharField(max_length=500, null=True, default=0)
    Telefono = models.CharField(max_length=100, null=True, default=0)
    Correo = models.CharField(max_length=100, null=True, default=0)
    Direccion_Correspondencia = models.CharField(max_length=5000, null=True)
    Municipio_Correspondencia = models.CharField(max_length=5000, null=True)
    Telefono_Contacto = models.CharField(max_length=5000, null=True, default=0)
    Celular_Contacto = models.CharField(max_length=5000, null=True, default=0)
    Direccion = models.CharField(max_length=5000, null=True)
    Municipio = models.CharField(max_length=5000, null=True)
    Instalación = models.CharField(max_length=5000, null=True)
    Area_Operativa = models.CharField(max_length=5000, null=True)
    Subzona = models.CharField(max_length=5000, null=True)
    Area_Trabajo = models.CharField(max_length=5000, null=True)
    Ruta = models.CharField(max_length=5000, null=True)
    Coordenadax = models.CharField(max_length=5000, null=True)
    Coordenaday = models.CharField(max_length=5000, null=True)
    Actividad = models.CharField(max_length=5000, null=True)
    Equipo = models.CharField(max_length=5000, null=True)
    Nombre = models.CharField(max_length=5000, null=True)
    Fecha_Programación = models.CharField(max_length=5000, default=0)
    Num_Proyecto = models.CharField(max_length=500, null=True)
    Tipo_Dirección = models.CharField(max_length=10000, null=True)
    Observación = models.CharField(max_length=5000, null=True)
    Observación_Solicitud = models.CharField(max_length=5000, null=True)
    Pedido_CRM = models.CharField(max_length=5000, null=True, default=0)
    dias_vencimiento = models.IntegerField(verbose_name="Dias de vencimiento", default=0)
    dias_vencimiento_epm = models.IntegerField(verbose_name="Dias de vencimiento epm", default=0)
    fecha_vencimiento = models.CharField(max_length=30, verbose_name="Fecha vencimiento", default=0)
    encargado = models.CharField(max_length=100, null=True)
    estado_cierre = models.IntegerField(default=0, null=True, blank=True)
    fecha_cierre = models.CharField(max_length=100, null=True, default=0)
    fecha_vence_sin_hora= models.CharField(max_length=50, default=0)
    hora_vencimiento = models.CharField(max_length=50, default=0)
    fecha_vence_epm= models.CharField(max_length=50, default=0)

    class Meta:
        ordering = ["fecha_vencimiento"]
        verbose_name = "Programador"
        verbose_name_plural = "Programador"
        
    def __str__(self):
        return str(self.Pedido)

class Encargado(models.Model):
    nombre = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Encargado"
        verbose_name_plural = "Encargados"

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    dias_urbano = models.CharField(max_length=50, null=True)
    dias_rural = models.CharField(max_length=50, null=True)
    encargado = models.ForeignKey(
        Encargado, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        
class Actividad_epm(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    dias_urbano = models.CharField(max_length=50, null=True)
    dias_rural = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Actividad epm"
        verbose_name_plural = "Actividades epm"

class Vencido(models.Model):
    Pedido = models.TextField(max_length=100, default=0)
    Instalación = models.CharField(max_length=5000, null=True)
    Actividad = models.CharField(max_length=5000, null=True)
    Observación = models.CharField(max_length=5000, null=True)
    fecha_vencimiento = models.CharField(max_length=30, verbose_name="Fecha vencimiento", null=True, default="Sin registro")
    encargado = models.CharField(max_length=100, null=True)
    fecha_cierre = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Vencido"
        verbose_name_plural = "Vencidos"

class Municipio(models.Model):
    nombre = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

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
    concatenacion= models.CharField(verbose_name='Concat', max_length=100, default="0")
    pedido=models.CharField(verbose_name='Pedido', max_length=10)
    actividad=models.CharField(verbose_name='Actividad', max_length=500)
    fecha=models.CharField(verbose_name='Fecha', max_length=100)
    codigo=models.CharField(verbose_name='Código', max_length=100)
    cantidad=models.DecimalField(verbose_name='Cantidad', decimal_places=2, default=0, max_digits=6)   
    acta= models.CharField(verbose_name='Acta', max_length=100, default=0) 
    enfenix = models.IntegerField(default=0)  

    class Meta:
        db_table = 'perseo'
        verbose_name = 'Material Perseo'
        verbose_name_plural = 'Material Perseo'
        ordering = ['fecha']

    def __str__(self):
        return str(self.pedido)

class matfenix(models.Model):
    concatenacion= models.CharField(verbose_name='Concat', max_length=100, default="0")
    pedido=models.CharField(verbose_name='Pedido', max_length=10)
    actividad=models.CharField(verbose_name='Actividad', max_length=500)
    fecha=models.CharField(verbose_name='Fecha', max_length=100)
    codigo=models.CharField(verbose_name='Código', max_length=100)
    cantidad=models.DecimalField(verbose_name='Cantidad', decimal_places=2, default=0, max_digits=6)    
    enperseo = models.IntegerField(default=0) 

    class Meta:
        db_table = 'fenix'
        verbose_name = 'Material Fenix'
        verbose_name_plural = 'Material Fenix'
        ordering = ['fecha']

    def __str__(self):
        return str(self.pedido)

class faltanteperseo(models.Model):
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
        verbose_name_plural = 'Cantidadi Inicio Oficial'

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

