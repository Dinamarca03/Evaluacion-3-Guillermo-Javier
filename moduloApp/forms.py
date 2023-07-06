from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class ingresarProductosForm(forms.Form):
    nombre = forms.ModelChoiceField(queryset=nombreProducto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    id_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_producto = forms.ModelChoiceField(queryset=categoria.objects.all(), label="Categoría de Producto", widget=forms.Select(attrs={'class': 'form-control'}))
    valor_unitario = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sucursal = forms.ModelChoiceField(queryset=sucursal.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), initial=timezone.now().date())
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))


class ingresarProductosModelForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'
    nombre = forms.ModelChoiceField(queryset=nombreProducto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    id_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_producto = forms.ModelChoiceField(queryset=categoria.objects.all(), label="Categoría de Producto", widget=forms.Select(attrs={'class': 'form-control'}))
    valor_unitario = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sucursal = forms.ModelChoiceField(queryset=sucursal.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), initial=timezone.now().date())
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))




class ingresarSalidaProductosForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), initial=timezone.now().date())
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))

class ingresarSalidaProductosModelForm(forms.ModelForm):
    class Meta:
        model = ingresarSalidaProductos
        fields = '__all__'
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), initial=timezone.now().date())
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))

class ingresarEntradaProductosForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), initial=timezone.now().date())
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))

class ingresarEntradaProductosModelForm(forms.ModelForm):
    class Meta:
        model = ingresarSalidaProductos
        fields = '__all__'
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), initial=timezone.now().date())
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))





class ingresarDevolucionesForm(forms.Form):
    id_venta = forms.ModelChoiceField(queryset=ingresarSalidaProductos.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), initial=timezone.now().date())
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))


class ingresarDevolucionesModelForm(forms.ModelForm):
    class Meta:
        model = devolucion
        exclude = ['nombre_producto','id_producto'] 
        fields = '__all__'
    id_venta = forms.ModelChoiceField(queryset=ingresarSalidaProductos.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), initial=timezone.now().date())
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))

class ingresarSucursalesForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_sucursal = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero_telefono = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class ingresarSucursalesModelForm(forms.ModelForm):
    class Meta:
        model = sucursal
        fields = '__all__'
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_sucursal = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero_telefono = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class stockForm(forms.Form):
    id_producto_stock = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre_producto = forms.ModelChoiceField(queryset=producto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    tipo_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class stockModelForm(forms.ModelForm):
    class Meta:
        model = stock
        fields = '__all__'
    id_producto_stock = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre_producto = forms.ModelChoiceField(queryset=producto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    tipo_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class nombreProductoForm(forms.Form):
    nombre_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class nombreProductoModelForm(forms.ModelForm):
    class Meta:
        model = nombreProducto
        fields = '__all__'
        
    nombre_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class CustomUserCreationForm(UserCreationForm):
    rol = forms.ChoiceField(choices=Rol.ROLES_CHOICES, required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('rol','username', 'first_name', 'last_name','password1','password2')





class categoriaForm(forms.Form):
    nombre_categoria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_categoria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class categoriaModelForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'
        
    nombre_categoria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_categoria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
