# Generated by Django 4.0.6 on 2024-10-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_mejia', '0005_comparacionpedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparacionpedido',
            name='codigo',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
