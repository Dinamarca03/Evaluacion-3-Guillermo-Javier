from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=50)
    valor_unitario = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class devolucion(models.Model):
    nombre_producto = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    hora = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre_producto

class sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    numero_telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_sucursal
    
class Rol(models.Model):
    USUARIO = 'US'
    ADMIN = 'AD'
    ROLES_CHOICES = [
        (USUARIO, 'Usuario'),
        (ADMIN, 'Administrador'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=2, choices=ROLES_CHOICES, default=USUARIO)