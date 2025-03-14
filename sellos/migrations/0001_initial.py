# Generated by Django 5.1.4 on 2025-02-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActaSello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.CharField(max_length=50, null=True)),
                ('municipio', models.CharField(max_length=50, null=True)),
                ('actividad', models.CharField(max_length=50, null=True)),
                ('fecha', models.CharField(max_length=50, null=True)),
                ('pagina', models.CharField(max_length=50, null=True)),
                ('cantidad', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Acta sellos',
                'verbose_name_plural': 'Acta sellos',
            },
        ),
        migrations.CreateModel(
            name='MaterialInstalado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consecutivo', models.CharField(max_length=50, null=True)),
                ('pedido', models.CharField(max_length=50, null=True)),
                ('esta_en_acta', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Materiales instalados',
                'verbose_name_plural': 'Materiales instalados',
            },
        ),
        migrations.CreateModel(
            name='SerieSello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consecutivo', models.CharField(max_length=50, null=True)),
                ('serie', models.CharField(max_length=50, null=True)),
                ('pedido', models.CharField(max_length=50, null=True)),
                ('instalador', models.CharField(max_length=50, null=True)),
                ('va_en_informe', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Serie sello',
                'verbose_name_plural': 'Series Sellos',
            },
        ),
    ]
