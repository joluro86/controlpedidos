# Generated by Django 5.1.4 on 2025-06-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuevo_analisis', '0025_relacionultimocaracter_todos_los_registros_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacionultimocaracter',
            name='item_caracter',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ítems caracter'),
        ),
    ]
