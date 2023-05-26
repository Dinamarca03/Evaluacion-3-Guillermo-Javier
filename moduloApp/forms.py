from django.forms import ModelForm
from .models import *

class ingersarProductosForm(ModelForm):
    class Meta:
        model = producto
        fields = ['nombre','tipo_producto','valor_unitario','cantidad']

class ingresarDevolucionesForm(ModelForm):
    class Meta:
        model = devolucion
        fields = ['nombre_producto','fecha','hora','cantidad']

class ingresarSucursalesForm(ModelForm):
    class Meta:
        model = sucursal
        fields = ['nombre_sucursal','direccion','numero_telefono']
