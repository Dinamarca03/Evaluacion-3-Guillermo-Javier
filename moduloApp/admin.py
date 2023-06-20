from django.contrib import admin
from .models import producto,devolucion, sucursal
from .models import Rol

# Register your models here.

# puedo tener acceso desde el panel de administrador


admin.site.register(devolucion)
admin.site.register(producto)
admin.site.register(sucursal)
admin.site.register(Rol)





