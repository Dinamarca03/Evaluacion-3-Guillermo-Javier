# Generated by Django 4.1.2 on 2023-06-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0009_remove_sucursal_nombre_sucursal_sucursal_id_sucursal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ingresarSalidaProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_producto', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
