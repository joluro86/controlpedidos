# Generated by Django 4.0.6 on 2024-01-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0009_alter_dia_dia_mano_obra_alter_dia_dia_materiales_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dia_dia',
            name='mano_obra',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=11),
        ),
    ]