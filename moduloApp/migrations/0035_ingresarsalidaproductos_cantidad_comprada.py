# Generated by Django 4.1.1 on 2023-07-01 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0034_alter_devolucion_nombre_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresarsalidaproductos',
            name='cantidad_comprada',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
