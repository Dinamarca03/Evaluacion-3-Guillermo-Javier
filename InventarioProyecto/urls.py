"""InventarioProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from moduloApp.views import * #Todos los elementos de la vista


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
  
    
    path('registrar/', registrar, name= 'registrar'),
    path('proveedor/', proveedor, name= 'proveedor'),
    path('cerrarSesion/', cerrarSesion, name= 'cerrarSesion'),
    path('inicioSesion/', inicioSesion, name= 'inicioSesion'),

    path('sucursales/', sucursales, name= 'sucursales'),
    path('ingresarSucursales/', ingresarSucursales, name= 'ingresarSucursales'),
    path('borrarSucursales/<int:id>', borrarSucursales, name= 'borrarSucursales'),


    path('productos/', productos, name= 'productos'),
    path('ingresarProductos/', ingresarProductos, name= 'ingresarProductos'),
    path('editarProductos/<int:id>', editarProductos, name= 'editarProductos'),
    path('borrarProductos/<int:id>', borrarProductos, name= 'borrarProductos'),




    path('devoluciones/', devoluciones, name= 'devoluciones'),
    path('ingresarDevoluciones/', ingresarDevoluciones, name= 'ingresarDevoluciones'),
    path('borrarDevoluciones/<int:id>', borrarDevoluciones, name= 'borrarDevoluciones'),

    




]

