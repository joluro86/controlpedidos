# Generated by Django 4.0.6 on 2022-12-07 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonificaciones', '0024_novedadbonificacion_pedido'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PedidoBoniFenix',
            new_name='Fenix',
        ),
        migrations.RenameModel(
            old_name='PedidoBoniPerseo',
            new_name='Perseo',
        ),
    ]