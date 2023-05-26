from django.contrib import admin
from .models import producto,devolucion, sucursal

# Register your models here.

# puedo tener acceso desde el panel de administrador


admin.site.register(devolucion)
admin.site.register(producto)
admin.site.register(sucursal)





