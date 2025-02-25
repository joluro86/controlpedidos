# Generated by Django 5.1.4 on 2025-01-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analisis_acta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiales',
            name='material',
            field=models.CharField(default=0, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='novedad_acta',
            name='actividad',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='novedad_acta',
            name='estado',
            field=models.CharField(default='Aplica', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='novedad_acta',
            name='item',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='novedad_acta',
            name='municipio',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='novedad_acta',
            name='novedad',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='novedad_acta',
            name='pagina',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='novedad_acta',
            name='pedido',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='novedad_acta',
            name='tipre',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
    ]
