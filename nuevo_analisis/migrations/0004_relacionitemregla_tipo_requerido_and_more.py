# Generated by Django 5.1.4 on 2025-05-28 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuevo_analisis', '0003_relacionitemregla_factor'),
    ]

    operations = [
        migrations.AddField(
            model_name='relacionitemregla',
            name='tipo_requerido',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='itemregla',
            name='tipo',
            field=models.CharField(choices=[('suministro', 'Suministro'), ('actividad', 'Actividad'), ('obra', 'Obra')], max_length=30),
        ),
    ]
