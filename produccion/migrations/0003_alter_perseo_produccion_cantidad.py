# Generated by Django 4.0.6 on 2024-01-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_novedadproduccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perseo_produccion',
            name='cantidad',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]