# Generated by Django 4.0.6 on 2023-02-01 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominametro', '0010_alter_concepto_factor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prenomina',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]