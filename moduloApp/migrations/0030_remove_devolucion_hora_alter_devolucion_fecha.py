# Generated by Django 4.1.2 on 2023-06-25 20:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0029_devolucion_hora_alter_devolucion_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devolucion',
            name='hora',
        ),
        migrations.AlterField(
            model_name='devolucion',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
