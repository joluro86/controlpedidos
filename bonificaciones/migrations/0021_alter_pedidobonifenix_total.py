# Generated by Django 4.0.6 on 2022-11-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonificaciones', '0020_alter_pedidoboniperseo_descuento_de_fenix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidobonifenix',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]