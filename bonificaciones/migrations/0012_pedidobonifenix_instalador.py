# Generated by Django 4.0.6 on 2022-11-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonificaciones', '0011_rename_instalacion_pedidobonifenix_pagina_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidobonifenix',
            name='instalador',
            field=models.CharField(default=0, max_length=100),
        ),
    ]