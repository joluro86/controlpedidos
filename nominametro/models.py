from django.db import models

# Create your models here.

class prenomina(models.Model):
    centro_de_costos = models.CharField(max_length=100, default='-')
    nombre_del_centro_de_costos = models.CharField(max_length=100, default='-')
    empleado = models.CharField(max_length=100, default='-')
    nombre_del_empleado = models.CharField(max_length=200, default='-')
    turno = models.CharField(max_length=100, default='-')
    descripción_del_turno = models.CharField(max_length=200, default='-')
    concepto = models.CharField(max_length=100, default='-')
    nombre_del_concepto = models.CharField(max_length=200, default='-')
    vinculación = models.CharField(max_length=100, default='-')
    préstamo = models.CharField(max_length=100, null=True, default='-')
    salario_básico_hora = models.CharField(max_length=100,  null=True, default='-')
    tiempo = models.DecimalField(max_digits=12, decimal_places=4, default=0.00)
    valor = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    conversor = models.CharField(max_length=200, default='-')
    tipo = models.CharField(max_length=200, default='0')
    factor = models.CharField(max_length=200, default='0')


    class Meta:
        verbose_name = 'prenomina'
        verbose_name_plural = 'prenomina'
        db_table = 'prenomina'
        order_with_respect_to = 'empleado'

    def __str__(self):
        return str(self.empleado)


class plantilla(models.Model):

    cedula = models.CharField(max_length=200, default='-')
    nombre = models.CharField(max_length=200, default='-')
    apellido = models.CharField(max_length=200, default='-')
    codigo = models.CharField(max_length=200, default='-')
    cargo = models.CharField(max_length=200, default='-')
    salario_mensual_basico = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    valor_hora_ordin = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    periodo_fecha_inicial = models.CharField(max_length=200, default='-')
    periodo_fecha_final = models.CharField(max_length=200, default='-')
    horas_ordinarias = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    on_0_35 = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    ed_1_25 = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    en_1_75 = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    fd_0_75 = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    fn_1_1 = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    efd_2 = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    efn_2_5 = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    d_o_f_d_1_75 = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    d_o_f_n_2_1 = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    ausencias_remuneradas_hora =models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    ausencias_no_remuneradas_hora = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    incapacidad_por_enfermedad_general_horas = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    vr_auxilio_transporte_o_auxilio_de_conectividad = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    otros_ingresos_no_prestacionales = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    otros_ingresos_prestacionales = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    total_devengado = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    deducción_retención_en_la_fuente = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    otras_deducciones = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    deducciones_sgss = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    neto_a_pagar = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)

    class Meta:

        verbose_name = 'plantilla'
        verbose_name_plural = 'plantilla'
        db_table = 'plantilla'
        order_with_respect_to = 'nombre'

    def __str__(self):
        return str(self.nombre)

    def definir_cargo(self):
        try:
            self.cargo= Cargo.objects.get(cedula=self.cedula).cargo
            self.save()
        except:
            pass

    def definir_salario(self):
        try:
            self.salario_mensual_basico= Cargo.objects.get(cedula=self.cedula).salario
            self.save()
        except:
            pass

class Concepto(models.Model):
    concepto = models.CharField(max_length=200)
    conversor = models.CharField(max_length=200)
    factor = models.DecimalField(max_digits=6, decimal_places=4, default=1.0000)
    tipo = models.CharField(max_length=200, default='0')


    class Meta:
        verbose_name = 'Concepto'
        verbose_name_plural = 'Conceptos'
        db_table = 'conceptos'
        order_with_respect_to = 'concepto'

    def __str__(self):
        return str(self.concepto)

class Novedad_nomina(models.Model):
    empleado = models.CharField(max_length=200)
    novedad = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Novedad nomina'
        verbose_name_plural = 'Novedad nomina'
        db_table = 'novedad_nomina'
        order_with_respect_to = 'empleado'

    def __str__(self):
        return str(self.empleado) + " novedad: " + str(self.novedad)

class Cargo(models.Model):
    cedula = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    salario = models.CharField(max_length=200, default=0)

    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'cargos'
        order_with_respect_to = 'cedula'

    def __str__(self):
        return str(self.cargo) 






