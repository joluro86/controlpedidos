# Generated by Django 4.0.6 on 2022-11-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonificaciones', '0016_rename_bonificaciondia_producidodia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producidodia',
            old_name='excedente',
            new_name='producido',
        ),
        migrations.RemoveField(
            model_name='producidodia',
            name='laborado',
        ),
        migrations.AddField(
            model_name='pedidoboniperseo',
            name='identificador',
            field=models.CharField(default=0, max_length=50),
        ),
    ]