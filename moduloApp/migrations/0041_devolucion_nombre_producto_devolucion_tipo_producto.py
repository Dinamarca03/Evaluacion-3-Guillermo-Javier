# Generated by Django 4.1.2 on 2023-07-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0040_rename_nombre_producto_devolucion_id_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='devolucion',
            name='nombre_producto',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devolucion',
            name='tipo_producto',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
