from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms


class nombreProducto(models.Model):
    nombre_producto = models.CharField(max_length=100, unique=True)
    id_producto = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_producto

class categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100, unique=True)
    id_categoria = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_categoria



class sucursal(models.Model):
    nombre = models.CharField(max_length=10)
    id_sucursal = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)
    numero_telefono = models.IntegerField()

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.id_sucursal


""" Ingreso de Productos """
from django.utils import timezone
class producto(models.Model):
    nombre = models.ForeignKey(nombreProducto, on_delete=models.CASCADE)
    id_producto = models.CharField(max_length=100, unique=True)
    tipo_producto = models.ForeignKey(categoria, on_delete=models.CASCADE)
    valor_unitario = models.IntegerField()
    cantidad = models.IntegerField()
    sucursal = models.ForeignKey(sucursal, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre.nombre


class ingresarSalidaProductos(models.Model):
    nombre = models.CharField(max_length=100)
    id_producto = models.CharField(max_length=50)
    tipo_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha =  models.DateField(default=timezone.now)
    hora = models.TimeField(auto_now_add=True)
    cantidad_comprada = models.PositiveIntegerField(default=0)
    accion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Salida"
        verbose_name_plural = "Salidas"

    def __str__(self):
        return str(self.id)
    
class ingresarEntradaProductos(models.Model):
    nombre = models.CharField(max_length=100)
    id_producto = models.CharField(max_length=50)
    tipo_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha =  models.DateField(default=timezone.now)
    hora = models.TimeField(auto_now_add=True)
    cantidad_comprada = models.PositiveIntegerField(default=0)
    accion = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return self.nombre



class devolucion(models.Model):
    id_venta = models.ForeignKey(ingresarSalidaProductos, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100, default='')
    id_producto = models.CharField(max_length=50, default='')  # Campo adicional para el tipo de producto
    cantidad = models.IntegerField()
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Devolucion"
        verbose_name_plural = "Devoluciones"

    def __str__(self):
        return str(self.id_venta.id)




class stock(models.Model):
    id_producto_stock = models.CharField(max_length=100)
    nombre_producto = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.id_producto_stock


class Rol(models.Model):
    USUARIO = 'US'
    ADMIN = 'AD'
    ROLES_CHOICES = [
        (USUARIO, 'Usuario'),
        (ADMIN, 'Administrador'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=2, choices=ROLES_CHOICES, default=USUARIO)

    def __str__(self):
        return self.usuario.username


@receiver(post_save, sender=User)
def crear_rol_usuario(sender, instance, created, **kwargs):
    if created:
        Rol.objects.create(usuario=instance)


