# Generated by Django 4.1.2 on 2023-06-26 02:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0032_ingresarsalidaproductos_hora_producto_hora_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='devolucion',
            name='hora',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='devolucion',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
