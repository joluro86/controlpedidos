# Generated by Django 4.0.6 on 2023-04-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analisis_acta', '0003_alter_acta_item_cont_alter_acta_suminis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acta',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]