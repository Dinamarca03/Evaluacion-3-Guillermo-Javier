# Generated by Django 4.1.1 on 2023-07-01 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0035_ingresarsalidaproductos_cantidad_comprada'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresarsalidaproductos',
            name='accion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
