# Generated by Django 4.1.2 on 2023-05-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0002_rename_productos_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=100)),
                ('fecha', models.CharField(max_length=100)),
                ('hora', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
