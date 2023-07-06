# Generated by Django 4.1.2 on 2023-06-26 02:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0031_remove_stock_motivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresarsalidaproductos',
            name='hora',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='hora',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ingresarsalidaproductos',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
