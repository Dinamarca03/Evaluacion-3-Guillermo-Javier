# Generated by Django 4.1.2 on 2023-07-02 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0043_devolucion_nombre_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devolucion',
            name='nombre_producto',
        ),
    ]
