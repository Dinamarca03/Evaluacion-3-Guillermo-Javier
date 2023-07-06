from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Rol
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.db import IntegrityError
from django.db.models import Sum
from reportlab.pdfgen import canvas
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from datetime import date, datetime
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO



# Create your views here.
@never_cache
@login_required
def index(request):
    # Verificar si es la primera sesión del usuario
    if not request.session.get('primera_sesion', False):
        request.session['primera_sesion'] = True  # Marcar la sesión como la primera

        # Agregar el mensaje de Swal.fire al contexto
        messages.success(request, 'Bienvenido al sistema Bambini')

    return render(request, 'sistema/index.html')



#Registrar usuario
@never_cache
@login_required
def registrar(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'usuarios/registrar.html', {'form': form})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    user = form.save()
                    rol = Rol(usuario=user, rol=form.cleaned_data.get('rol'))
                    rol.save()
                    login(request, user)
                    return redirect('index')
                except IntegrityError:
                    error = 'usuario creado con exito'
            else:
                error = 'El usuario ya existe'
        else:
            error = 'Las contraseñas no coinciden'
            print(form.errors)
        
        return render(request, 'usuarios/registrar.html', {'form': form, 'error': error})

@never_cache
@login_required
def perfil(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña actualizada con éxito.')
            return redirect('perfil')
        else:
            messages.error(request, 'Por favor, corrija los errores.')
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'usuarios/perfil.html', {'form': form})

@never_cache
@login_required
def suma_cantidad(request):
    suma_total = producto.objects.aggregate(suma_cantidad=Sum('cantidad'))['suma_cantidad']
    productos = producto.objects.all()
    return render(request, 'productos/productos.html', {'productos': productos, 'suma_total': suma_total})  

@never_cache
@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('inicioSesion')
@never_cache
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

@never_cache
@login_required
def sucursales(request):
   # return render(request, 'sucursal/sucursales.html')
    sucursales = sucursal.objects.all()
    return render(request, 'sucursal/sucursales.html.',{'sucursales':sucursales})

@never_cache
@login_required
def ingresarSucursales(request):
    if request.method == 'GET':
        form = ingresarSucursalesModelForm()
        return render(request, 'sucursal/ingresarSucursal.html', {'form': form})
    else:
        form = ingresarSucursalesModelForm(request.POST)
        if form.is_valid():
            form.save()
            sucursales = sucursal.objects.all() # Obtener todos los productos
            return render(request, 'sucursal/sucursales.html', {'sucursales': sucursales})
        else:
            return render(request, 'sucursal/ingresarSucursal.html', {'form': form})
        
@never_cache
@login_required   
def borrarSucursales(request, id):
    sucursales = sucursal.objects.get(id=id)
    sucursales.delete()
    return redirect('sucursales')

@never_cache
@login_required
def editarSucursales(request, id):
    SUCURSALES = sucursal.objects.get(id=id)
    print(sucursal)
    data = {
        'form': ingresarSucursalesModelForm(instance=SUCURSALES),
        'titulo': 'Editar ficha de sucursal'
    }
    if (request.method == 'POST'):
        form = ingresarSucursalesModelForm(request.POST, instance=SUCURSALES)
        if (form.is_valid()):
            form.save()
            return redirect('/sucursales')
        else:
            data['form'] = form
    return render(request, 'sucursal/ingresarSucursal.html',data)

@never_cache
@login_required
def productos(request):
    productos = producto.objects.all()
    suma_total = producto.objects.aggregate(suma_cantidad=Sum('cantidad'))['suma_cantidad']
    return render(request, 'productos/productos.html', {'productos': productos, 'suma_total': suma_total})

@never_cache
@login_required
def ingresarProductos(request):
    if request.method == 'GET':
        form = ingresarProductosModelForm()
        return render(request, 'productos/ingresarProductos.html', {'form': form})
    else:
        form = ingresarProductosModelForm(request.POST)
        if form.is_valid():
            form.save()
            suma_total = producto.objects.aggregate(suma_cantidad=Sum('cantidad'))['suma_cantidad']
            productos = producto.objects.all()
            return render(request, 'productos/productos.html', {'productos': productos, 'suma_total': suma_total})
        else:
            return render(request, 'productos/ingresarProductos.html', {'form': form})
        

@never_cache
@login_required
def borrarProductos(request, id):
    productos = producto.objects.get(id=id)
    productos.delete()
    return redirect('/productos')

@never_cache
@login_required
def editarProductos(request, id):
    PRODUCTO = producto.objects.get(id=id)
    data = {
        'form': ingresarProductosModelForm(instance=PRODUCTO), 
        'titulo': 'Editar ficha de Producto'
    }

    if request.method == 'POST':
        form = ingresarProductosModelForm(request.POST, instance=PRODUCTO)
        if form.is_valid():
            form.save()
            return redirect('/productos')
        else:
            data['form'] = form

    return render(request, 'productos/ingresarProductos.html', data)

@never_cache
@login_required
def comprar_producto(request, producto_id):
    producto_obj = get_object_or_404(producto, id=producto_id)

    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
        accion = request.POST['accion']

        if accion == 'agregar':
            producto_obj.cantidad += cantidad
            producto_obj.save()
            # Crear la entrada de productos y guardarla
            entrada_producto = ingresarEntradaProductos(
                nombre=producto_obj.nombre.nombre_producto,
                id_producto=producto_obj.id_producto,
                tipo_producto=producto_obj.tipo_producto,
                cantidad=producto_obj.cantidad,
                fecha=date.today(),
                hora=datetime.now().strftime("%H:%M:%S"),
                cantidad_comprada=cantidad,
                accion=accion
            )
            entrada_producto.save()
            return redirect('productos')
        elif accion == 'descontar':
            if producto_obj.cantidad >= cantidad:
                producto_obj.cantidad -= cantidad
                producto_obj.save()
                # Crear la salida de productos y guardarla
                salida_producto = ingresarSalidaProductos(
                    nombre=producto_obj.nombre.nombre_producto,
                    id_producto=producto_obj.id_producto,
                    tipo_producto=producto_obj.tipo_producto,
                    cantidad=producto_obj.cantidad,
                    fecha=date.today(),
                    hora=datetime.now().strftime("%H:%M:%S"),
                    cantidad_comprada=cantidad,
                    accion=accion
                )
                salida_producto.save()
                return redirect('productos')
            else:
                return HttpResponse('La cantidad a descontar supera la cantidad disponible del producto.')

    return render(request, 'productos/comprar_producto.html', {'producto': producto_obj})



@never_cache
@login_required
def historialentrada(request):
    entradas = ingresarEntradaProductos.objects.all()
    context = {
        'entradas': entradas
    }
    return render(request, 'productos/historialEntrada.html', context)



@never_cache
@login_required
def salidaproductos(request):
    salidas = ingresarSalidaProductos.objects.all()
    return render(request, 'productos/salidaProductos.html', {'salidas': salidas})

@never_cache
@login_required
def ingresar_salida_productos(request):
    if request.method == 'GET':
        form = ingresarSalidaProductosModelForm()
        return render(request, 'productos/ingresarSalidaProductos.html', {'form': form})
    else:
        form = ingresarSalidaProductosModelForm(request.POST)
        if form.is_valid():
            form.save()
            salidas = ingresarSalidaProductos.objects.all()  # Obtener todas las salidas
            return render(request, 'productos/salidaProductos.html', {'salidas': salidas})
        else:
            return render(request, 'productos/ingresarSalidaProductos.html', {'form': form})
        
@never_cache
@login_required
def borrarSalida(request, id):
    salidas = ingresarSalidaProductos.objects.get(id=id)
    salidas.delete()
    return redirect('/salidaProductos')

@never_cache
@login_required
def editarSalida(request, id):
    salida = ingresarSalidaProductos.objects.get(id=id)
    data = {
        'form': ingresarSalidaProductosModelForm(instance=salida),
        'titulo': 'Editar ficha de Salida de Productos'
    }

    if request.method == 'POST':
        form = ingresarSalidaProductosModelForm(request.POST, instance=salida)
        if form.is_valid():
            form.save()
            return redirect('/salidaProductos')
        else:
            data['form'] = form

    return render(request, 'productos/ingresarSalidaProductos.html', data)

""" Devoluciones """
@never_cache
@login_required
def devoluciones (request):
    devoluciones = devolucion.objects.all()
    return render(request, 'devoluciones/devoluciones.html',{'devoluciones':devoluciones})
from django.http import JsonResponse
@never_cache
@login_required

def ingresarDevoluciones(request):
    if request.method == 'GET':
        form = ingresarDevolucionesModelForm()
        return render(request, 'devoluciones/ingresarDevoluciones.html', {'form': form})
    else:
        form = ingresarDevolucionesModelForm(request.POST)
        if form.is_valid():
            venta_id = form.cleaned_data['id_venta'].id
            cantidad = form.cleaned_data['cantidad']
            fecha = form.cleaned_data['fecha']
            hora = form.cleaned_data['hora']

            salida_producto = get_object_or_404(ingresarSalidaProductos, id=venta_id)

            devolucion_obj = form.save(commit=False)
            devolucion_obj.nombre_producto = salida_producto.nombre
            devolucion_obj.id_producto = salida_producto.id_producto  # Asignar el ID del producto
            devolucion_obj.save()

            producto_original = get_object_or_404(producto, id_producto=salida_producto.id_producto)
            producto_original.cantidad += cantidad
            producto_original.save()

            devoluciones = devolucion.objects.all()
            id_producto = salida_producto.id_producto  # Obtener el ID del producto
            return render(request, 'devoluciones/devoluciones.html', {'devoluciones': devoluciones, 'nombre_producto': salida_producto.nombre, 'id_producto': id_producto})
        else:
            return render(request, 'devoluciones/ingresarDevoluciones.html', {'form': form})


def get_nombre_producto(request):
    if request.method == 'GET' and 'id' in request.GET:
        id_producto = request.GET['id']
        producto = ingresarSalidaProductos.objects.filter(id=id_producto).first()
        nombre_producto = producto.nombre if producto else ''
        data = {'nombre_producto': nombre_producto}
        return JsonResponse(data)
    return JsonResponse({})
def get_id_producto(request):
    id_venta = request.GET.get('id')
    devolucion = ingresarSalidaProductos.objects.get(id_venta_id=id_venta)
    data = {'id_producto': devolucion.id_producto}
    return JsonResponse(data)


 

@never_cache
@login_required
def borrarDevoluciones(request, id):
    devoluciones = devolucion.objects.get(id=id)
    devoluciones.delete()
    return redirect('/devoluciones')

@never_cache
@login_required
def editarDevoluciones(request, id):
    DEVOLUCION = devolucion.objects.get(id=id)
    print(devolucion)
    data = {
        'form': ingresarDevolucionesModelForm(instance=DEVOLUCION),
        'titulo': 'Editar ficha de devolución'
    }
    if request.method == 'POST':
        form = ingresarDevolucionesModelForm(request.POST, instance=DEVOLUCION)
        if form.is_valid():
            form.save()
            return redirect('/devoluciones')
        else:
            data['form'] = form
    return render(request, 'devoluciones/ingresarDevoluciones.html', data)

@never_cache
@login_required
def nombreProductos(request):
    nproductos = nombreProducto.objects.all() # Obtener todos los productos
    return render(request, 'productos/nombreProductos.html', {'nproductos': nproductos})

@never_cache
@login_required
def ingresarNombreProductos(request):
    if request.method == 'GET':
        form = nombreProductoModelForm()
        return render(request, 'productos/ingresarNombreProductos.html', {'form': form})
    else:
        form = nombreProductoModelForm(request.POST)
        if form.is_valid():
            form.save()
            nproductos = nombreProducto.objects.all() # Obtener todos los productos
            return render(request, 'productos/nombreProductos.html', {'nproductos': nproductos})
        else:
            return render(request, 'productos/ingresarNombreProductos.html', {'form': form})

@never_cache
@login_required
def borrarNombreProducto(request, id):
    nproductos = nombreProducto.objects.get(id=id)
    nproductos.delete()
    return redirect('/nombreProductos')

@never_cache
@login_required
def editarNombreProductos(request, id):
    NPRODUCTOS = nombreProducto.objects.get(id=id)
    print(nombreProducto)
    data = {
        'form': nombreProductoModelForm(instance=NPRODUCTOS),
        'titulo': 'Editar ficha de Productos'
    }
    if request.method == 'POST':
        form = nombreProductoModelForm(request.POST, instance=NPRODUCTOS)
        if form.is_valid():
            form.save()
            return redirect('/nombreProductos')
        else:
            data['form'] = form
    return render(request, 'productos/ingresarNombreProductos.html', data)

@never_cache
@login_required
def calcular_suma_resta(request):
    # Cálculo de sumas y restas

    suma = producto.objects.all().aggregate(Sum('cantidad'))

    data = {
        'suma': suma,
    }
    return render(request, 'productos/productos.html', data)

@never_cache
@login_required
def reportes(request):
    return render(request, 'sistema/reportes.html')


@never_cache
@login_required
def generar_reporte_productos(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_productos.pdf"'

    productos = producto.objects.order_by('-fecha', '-hora').all()

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

    elements = []
    styles = getSampleStyleSheet()

    # Título del reporte de productos
    title = Paragraph("Reporte de Productos", styles['Title'])
    elements.append(title)

    # Datos de los productos
    data = [['ID', 'Nombre', 'Tipo', 'Valor Unitario', 'Cantidad']]
    for prod in productos:
        data.append([prod.id, prod.nombre, prod.tipo_producto, prod.valor_unitario, prod.cantidad])

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Crear tabla
    table = Table(data)
    table.setStyle(style)
    elements.append(table)

    # Construir el documento PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

@never_cache
@login_required
def generar_reporte_sucursales(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_sucursales.pdf"'

    sucursales = sucursal.objects.all()

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

    elements = []
    styles = getSampleStyleSheet()

    # Título del reporte de sucursales
    title = Paragraph("Reporte de Sucursales", styles['Title'])
    elements.append(title)

    # Datos de las sucursales
    data = [['ID', 'Nombre', 'Dirección', 'Número de Teléfono']]
    for sucur in sucursales:
        data.append([sucur.id_sucursal, sucur.nombre, sucur.direccion, sucur.numero_telefono])

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Crear tabla
    table = Table(data)
    table.setStyle(style)
    elements.append(table)

    # Construir el documento PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

@never_cache
@login_required
def generar_reporte_devoluciones(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_devoluciones.pdf"'

    devoluciones = devolucion.objects.order_by('-fecha', '-hora').all()

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

    elements = []
    styles = getSampleStyleSheet()

    # Título del reporte de devoluciones
    title = Paragraph("Reporte de Devoluciones", styles['Title'])
    elements.append(title)

    # Datos de las devoluciones
    data = [['ID', 'Nombre producto', 'Fecha', 'Hora', 'Cantidad']]
    for devolu in devoluciones:
        data.append([devolu.id, devolu.nombre_producto, devolu.fecha, devolu.hora, devolu.cantidad])

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Crear tabla
    table = Table(data)
    table.setStyle(style)
    elements.append(table)

    # Construir el documento PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response



from django.views.decorators.cache import never_cache
@never_cache
@login_required
def mi_vista_protegida(request):
    # Tu lógica de vista aquí
    return render(request, 'sistema/inicioSesion.html')




""" Categorias """
@never_cache
@login_required
def viewCategoria (request):
    categorias = categoria.objects.all()
    return render(request, 'categoria/categoria.html',{'categorias':categorias})

@never_cache
@login_required
def ingresarCategoria(request):
    if request.method == 'GET':
        form = categoriaModelForm()
        return render(request, 'categoria/ingresarCategoria.html', {'form': form})
    else:
        form = categoriaModelForm(request.POST)
        if form.is_valid():
            form.save()
            categorias = categoria.objects.all()
            return render(request, 'categoria/categoria.html', {'categorias': categorias})
            return redirect('viewCategoria')
        
        else:
            return render(request, 'categoria/ingresarCategoria.html', {'form': form})

@never_cache
@login_required
def borrarCategoria(request, id):
    categorias = categoria.objects.get(id=id)
    categorias.delete()
    return redirect('/viewCategoria')

@never_cache
@login_required
def editarCategoria(request, id):
    CATEGORIA = categoria.objects.get(id=id)
    data = {
        'form': categoriaModelForm(instance=CATEGORIA),
        'titulo': 'Editar ficha de Categoria'
    }
    if request.method == 'POST':
        form = categoriaModelForm(request.POST, instance=CATEGORIA)
        if form.is_valid():
            form.save()
            return redirect('viewCategoria')
        else:
            data['form'] = form
    return render(request, 'categoria/ingresarCategoria.html', data)



@never_cache
@login_required
def generar_reporte(request):
    salidas = ingresarSalidaProductos.objects.order_by('-fecha', '-hora').all()


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_productos.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

    elements = []

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Datos de la tabla
    data = [['Nombre', 'Tipo de producto', 'Cantidad', 'Fecha', 'Hora', 'Cantidad comprada']]
    for salida in salidas:
        data.append([salida.nombre, salida.tipo_producto, salida.cantidad, salida.fecha, salida.hora, salida.cantidad_comprada])

    # Crear tabla
    table = Table(data)
    table.setStyle(style)
    elements.append(table)

    # Construir el documento PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

@never_cache
@login_required
def generar_reporte2(request):
    salidas = ingresarEntradaProductos.objects.order_by('-fecha', '-hora').all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_productos.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

    elements = []

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Datos de la tabla
    data = [['Nombre', 'Tipo de producto', 'Cantidad', 'Fecha', 'Hora', 'Cantidad comprada']]
    for salida in salidas:
        data.append([salida.nombre, salida.tipo_producto, salida.cantidad, salida.fecha, salida.hora, salida.cantidad_comprada])

    # Crear tabla
    table = Table(data)
    table.setStyle(style)
    elements.append(table)

    # Construir el documento PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

@never_cache
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.save()
        return redirect('perfil')  # Redirigir a la página de perfil
    return render(request, 'usuarios/editarPerfil.html')


@never_cache
@login_required
def usuarios(request):
    usuarios = User.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'usuarios/usuarios.html', context)

@never_cache
@login_required
def borrarUsuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('/usuarios')
