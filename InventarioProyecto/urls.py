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
    path('index/', index, name='index'),
    path('suma-cantidad/',suma_cantidad, name='suma_cantidad'),
    path('reportes/', reportes, name='reportes'),
    path('generar_reporte_productos/', generar_reporte_productos, name='generar_reporte_productos'),
    path('generar_reporte_sucursales/', generar_reporte_sucursales, name='generar_reporte_sucursales'),
    path('generar_reporte_devoluciones/', generar_reporte_devoluciones, name='generar_reporte_devoluciones'),
    
    path('registrar/', registrar, name= 'registrar'),
    path('cerrarSesion/', cerrarSesion, name= 'cerrarSesion'),
    path('', inicioSesion, name= 'inicioSesion'),

    path('sucursales/', sucursales, name= 'sucursales'),
    path('ingresarSucursales/', ingresarSucursales, name= 'ingresarSucursales'),
    path('editarSucursales/<int:id>', editarSucursales, name= 'editarSucursales'),
    path('borrarSucursales/<int:id>', borrarSucursales, name= 'borrarSucursales'),


    path('productos/', productos, name= 'productos'),
    path('ingresarProductos/', ingresarProductos, name= 'ingresarProductos'),
    path('editarProductos/<int:id>', editarProductos, name= 'editarProductos'),
    path('borrarProductos/<int:id>', borrarProductos, name= 'borrarProductos'),
    path('comprar-producto/<int:producto_id>/', comprar_producto, name='comprarProducto'),
    
    path('historialentrada/', historialentrada, name= 'historialentrada'),


    path('nombreProductos/', nombreProductos, name= 'nombreProductos'),
    path('ingresarNombreProductos/', ingresarNombreProductos, name= 'ingresarNombreProductos'),
    path('editarNombreProductos/<int:id>', editarNombreProductos, name= 'editarNombreProductos'),
    path('borrarNombreProducto/<int:id>', borrarNombreProducto, name= 'borrarNombreProducto'),

    



    path('ingresar_salida_productos/', ingresar_salida_productos, name= 'ingresar_salida_productos'),
    path('salidaProductos/', salidaproductos, name= 'salidaProductos'),
    path('borrarSalida/<int:id>', borrarSalida, name= 'borrarSalida'),
    path('editarSalida/<int:id>', editarSalida, name= 'editarSalida'),


    path('devoluciones/', devoluciones, name= 'devoluciones'),
    path('ingresarDevoluciones/', ingresarDevoluciones, name= 'ingresarDevoluciones'),
    path('borrarDevoluciones/<int:id>', borrarDevoluciones, name= 'borrarDevoluciones'),
    path('editarDevoluciones/<int:id>', editarDevoluciones, name= 'editarDevoluciones'),



    path('viewCategoria/', viewCategoria, name= 'viewCategoria'),
    path('ingresarCategoria/', ingresarCategoria, name= 'ingresarCategoria'),
    path('borrarCategoria/<int:id>', borrarCategoria, name= 'borrarCategoria'),
    path('editarCategoria/<int:id>', editarCategoria, name= 'editarCategoria'),


    path('editarDevoluciones/<int:id>/<int:cantidad>/', editarDevoluciones, name='editarDevoluciones'),

    path('generar-reporte/', generar_reporte, name='generar_reporte'),
    path('generar-reporte2/', generar_reporte2, name='generar_reporte2'),

    path('perfil/', perfil, name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),


    path('usuarios/', usuarios, name='usuarios'),
    path('borrarUsuario/<int:id>/', borrarUsuario, name='borrarUsuario'),
    path('get_nombre_producto/', get_nombre_producto, name='get_nombre_producto'),
    path('get_id_producto/', get_id_producto, name='get_id_producto'),


    




]

