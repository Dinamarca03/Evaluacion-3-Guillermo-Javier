from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

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

class CustomUserCreationForm(UserCreationForm):
    rol = forms.ChoiceField(choices=Rol.ROLES_CHOICES, required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('rol',)