from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Rol
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'sistema/index.html')
#Registrar usuario
def registrar(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'sistema/registrar.html', {'form': form})
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    user = form.save()
                    rol = Rol(usuario=user, rol=form.cleaned_data['rol'])
                    rol.save()
                    login(request, user)
                    return redirect('index')
                except:
                    return render(request, 'sistema/registrar.html', {'form': form, "error": 'Usuario ya existe'})
            else:
                return render(request, 'sistema/registrar.html', {'form': form, "error": 'Contraseñas no coinciden'})
        else:
            return render(request, 'sistema/registrar.html', {'form': form})


#proveedor
def proveedor(request):
    return render(request, 'sistema/proveedor.html')

def cerrarSesion(request):
    logout(request)
    return redirect('index')

def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'sistema/inicioSesion.html', {
            'form': AuthenticationForm()
        })
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '¡Autenticación exitosa!')
            return redirect('index')
        else:
            messages.error(request, 'El usuario o contraseña son incorrectos')
            return render(request, 'sistema/inicioSesion.html', {
                'form': AuthenticationForm()
            })

def sucursales(request):
   # return render(request, 'sucursal/sucursales.html')
    sucursales = sucursal.objects.all()
    return render(request, 'sucursal/sucursales.html.',{'sucursales':sucursales})

def ingresarSucursales(request):
    if request.method == 'GET':
        form = ingresarSucursalesForm()
        return render(request, 'sucursal/ingresarSucursal.html', {'form': form})
    else:
        form = ingresarSucursalesForm(request.POST)
        if form.is_valid():
            form.save()
            sucursales = sucursal.objects.all() # Obtener todos los productos
            return render(request, 'sucursal/sucursales.html', {'sucursales': sucursales})
        else:
            return render(request, 'sucursal/ingresarSucursal.html', {'form': form})

def borrarSucursales(request, id):
    sucursales = sucursal.objects.get(id=id)
    sucursales.delete()
    return redirect('/sucursales')

def editarSucursales(request, id):
    SUCURSALES = sucursal.objects.get(id=id)
    print(sucursal)
    data = {
        'form': ingresarSucursalesForm(instance=SUCURSALES),
        'titulo': 'Editar ficha de sucursal'
    }
    if (request.method == 'POST'):
        form = ingresarSucursalesForm(request.POST, instance=SUCURSALES)
        if (form.is_valid()):
            form.save()
            return redirect('/sucursales')
        else:
            data['form'] = form
    return render(request, 'sucursal/ingresarSucursal.html',data)




def productos(request):
    productos = producto.objects.all()
    return render(request, 'productos/productos.html.',{'productos':productos})

def ingresarProductos(request):
    if request.method == 'GET':
        form = ingersarProductosForm()
        return render(request, 'productos/ingresarProductos.html', {'form': form})
    else:
        form = ingersarProductosForm(request.POST)
        if form.is_valid():
            form.save()
            productos = producto.objects.all()  # Obtener todos los productos
            return render(request, 'productos/productos.html', {'productos': productos})
        else:
            return render(request, 'productos/ingresarProductos.html', {'form': form})

def borrarProductos(request, id):
    productos = producto.objects.get(id=id)
    productos.delete()
    return redirect('/productos')


def editarProductos(request, id):
    PRODUCTO = producto.objects.get(id=id)
    data = {
        'form': ingersarProductosForm(instance=PRODUCTO), 
        'titulo': 'Editar ficha de Producto'
    }

    if request.method == 'POST':
        form = ingersarProductosForm(request.POST, instance=PRODUCTO)
        if form.is_valid():
            form.save()
            return redirect('/productos')
        else:
            data['form'] = form

    return render(request, 'productos/ingresarProductos.html', data)











def devoluciones (request):
    devoluciones = devolucion.objects.all()
    return render(request, 'devoluciones/devoluciones.html.',{'devoluciones':devoluciones})



def ingresarDevoluciones(request):

    if request.method == 'GET':
        form = ingresarDevolucionesForm()
        return render(request, 'devoluciones/ingresarDevoluciones.html', {'form': form})
    else:
        form = ingresarDevolucionesForm(request.POST)
        if form.is_valid():
            form.save()
            devoluciones = devolucion.objects.all() # Obtener todos los productos
            return render(request, 'devoluciones/devoluciones.html', {'devoluciones': devoluciones})
        else:
            return render(request, 'devoluciones/ingresarDevoluciones.html', {'form': form})


def borrarDevoluciones(request, id):
    devoluciones = devolucion.objects.get(id=id)
    devoluciones.delete()
    return redirect('/devoluciones')
 
def editarDevoluciones(request, id):
    DEVOLUCION = devolucion.objects.get(id=id)
    print(devolucion)
    data = {
        'form': ingresarDevolucionesForm(instance=DEVOLUCION),
        'titulo': 'Editar ficha de devolución'
    }
    if request.method == 'POST':
        form = ingresarDevolucionesForm(request.POST, instance=DEVOLUCION)
        if form.is_valid():
            form.save()
            return redirect('/devoluciones')
        else:
            data['form'] = form
    return render(request, 'devoluciones/ingresarDevoluciones.html', data)
