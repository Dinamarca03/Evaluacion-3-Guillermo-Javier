# Generated by Django 4.1.2 on 2023-06-22 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0007_rename_id_sucursal_sucursal_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucion',
            name='nombre_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloApp.sucursal'),
        ),
    ]