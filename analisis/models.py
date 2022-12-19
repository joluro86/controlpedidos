from django.db import models

# Create your models here.

class Acta_analisis(models.Model):
    pedido=models.CharField(max_length=100, default=0)
    subz = models.CharField(max_length=100, default=0)
    municipio=models.CharField(max_length=100, default=0)
    actividad=models.CharField(max_length=100, default=0)
    pagina=models.CharField(max_length=100, default=0)
    urbrur=models.CharField(max_length=100, default=0)
    tipre=models.CharField(max_length=100, default=0)
    tipo=models.CharField(max_length=100, default=0)
    suminis=models.CharField(max_length=100, default=0)
    item_cont=models.CharField(max_length=100, default=0)
    cantidad=models.CharField(max_length=100, default=0)


    class Meta:
        ordering = ["pedido"]
        verbose_name = 'Acta_analisis'
        verbose_name_plural = 'Acta_analisis'

    def __str__(self):
        return self.pedido

