# Generated by Django 4.1.2 on 2023-07-01 04:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0036_ingresarsalidaproductos_accion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ingresarEntradaProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_producto', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('cantidad_comprada', models.PositiveIntegerField(default=0)),
                ('accion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
        ),
    ]