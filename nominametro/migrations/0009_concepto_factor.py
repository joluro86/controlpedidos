# Generated by Django 4.0.6 on 2023-01-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominametro', '0008_prenomina_conversor'),
    ]

    operations = [
        migrations.AddField(
            model_name='concepto',
            name='factor',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4),
        ),
    ]
