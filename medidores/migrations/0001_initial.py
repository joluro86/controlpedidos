# Generated by Django 4.0.6 on 2022-10-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActaMedidores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.CharField(default=0, max_length=100, null=True)),
                ('area_operativa', models.CharField(default=0, max_length=100, null=True)),
                ('subz', models.CharField(default=0, max_length=100, null=True)),
                ('ruta', models.CharField(default=0, max_length=100, null=True)),
                ('municipio', models.CharField(default=0, max_length=100, null=True)),
                ('contrato', models.CharField(default=0, max_length=100, null=True)),
                ('acta', models.CharField(default=0, max_length=100, null=True)),
                ('actividad', models.CharField(default=0, max_length=100, null=True)),
                ('fecha_estado', models.CharField(default=0, max_length=100, null=True)),
                ('pagina', models.CharField(default=0, max_length=100, null=True)),
                ('urbrur', models.CharField(default=0, max_length=100, null=True)),
                ('tipre', models.CharField(default=0, max_length=100, null=True)),
                ('red_interna', models.CharField(default=0, max_length=100, null=True)),
                ('tipo_operacion', models.CharField(default=0, max_length=100, null=True)),
                ('descent', models.CharField(default=0, max_length=100, null=True)),
                ('tipo', models.CharField(default=0, max_length=100, null=True)),
                ('cobro', models.CharField(default=0, max_length=100, null=True)),
                ('suminis', models.CharField(default=0, max_length=100, null=True)),
                ('item_cont', models.CharField(default=0, max_length=100, null=True)),
                ('item_res', models.CharField(default=0, max_length=100, null=True)),
                ('cantidad', models.CharField(default=0, max_length=100, null=True)),
                ('vlr_cliente', models.CharField(default=0, max_length=100, null=True)),
                ('valor_costo', models.CharField(default=0, max_length=100, null=True)),
                ('tipo_item', models.CharField(default=0, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Acta Medidores',
                'verbose_name_plural': 'Acta Medidoress',
            },
        ),
    ]