from django.db import models

# Create your models here.
class PedidoMedidores(models.Model):
    pedido=models.CharField(max_length=100, default=0, null=True)
    municipio=models.CharField(max_length=100, default=0, null=True)
    actividad=models.CharField(max_length=100, default=0, null=True)
    pagina=models.CharField(max_length=100, default=0, null=True)
    item_cont=models.CharField(max_length=100, default=0, null=True)
    suminis=models.CharField(max_length=100, default=0, null=True)
    cantidad=models.CharField(max_length=100, default=0, null=True)

    class Meta:
        verbose_name = 'Acta Medidores'
        verbose_name_plural = 'Acta Medidoress'

    def __str__(self):
        return self.pedido

class NovedadMedidores(models.Model):
    pedido=models.ForeignKey(PedidoMedidores, on_delete= models.CASCADE)
    novedad = models.CharField(max_length=200, default=0, null=True)

    class Meta:
        verbose_name = 'Novedades Medidores'
        verbose_name_plural = 'Novedades Medidoress'

    def __str__(self):
        return str(self.pedido)




