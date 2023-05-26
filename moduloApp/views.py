from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def index(request):
    return render(request, 'sistema/index.html')
#Registrar usuario
def registrar(request):

    if request.method == 'GET':
        return render(request, 'sistema/registrar.html', 
        {
            'form': UserCreationForm
        })
        
    else:
        if request.POST['password1'] == request.POST['password2']:
            #Registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index') #redirecciona al index una vez el usuario fue creado con exito
            except:
                return render(request, 'sistema/registrar.html', 
                {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })
            

        return render(request, 'sistema/registrar.html', 
                {
                    'form': UserCreationForm,
                    "error": 'Contraseñas no coinciden'
                })



#proveedor
def proveedor(request):
    return render(request, 'sistema/proveedor.html')

def cerrarSesion(request):
    logout(request)
    return redirect('index')

def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'sistema/inicioSesion.html', {
        'form': AuthenticationForm
        })
    else:

        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sistema/inicioSesion.html',
            {
                'form': AuthenticationForm,
                'error': "El usuario o contraseña son incorrectos"
            })
        else:
            login(request, user)
            return redirect('index')


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
 

