# Generated by Django 4.0.6 on 2023-02-07 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominametro', '0013_novedad_nomina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=200)),
                ('cargo', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'db_table': 'cargos',
                'order_with_respect_to': 'cedula',
            },
        ),
    ]