# Generated by Django 4.1.2 on 2023-07-05 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0050_remove_devolucion_nombre_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='devolucion',
            name='nombre_producto',
            field=models.CharField(default='', max_length=100),
        ),
    ]