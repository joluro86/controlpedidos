# Generated by Django 4.0.6 on 2024-01-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0008_alter_dia_dia_mano_obra_alter_dia_dia_materiales_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dia_dia',
            name='mano_obra',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dia_dia',
            name='materiales',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dia_dia',
            name='por_persona',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dia_dia',
            name='producido',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dia_dia',
            name='treinta_porciento',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dia_dia',
            name='valor_referencia',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='perseo_produccion',
            name='fecha',
            field=models.DateField(default=0),
        ),
        migrations.AlterField(
            model_name='perseo_produccion',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='perseo_produccion',
            name='valor',
            field=models.IntegerField(default=0),
        ),
    ]
