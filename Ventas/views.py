from django.http import HttpResponse
from django.shortcuts import render
from .models import Carrito, Producto, Categoria, ItemCarrito, Usuario

def get_carrito():
    try:
        carrito = Carrito.objects.all()
        data = {
            'titulo': 'Página Principal',
            'mensaje': 'Carrito.',
            'carrito': carrito,
            'total_ventas': Carrito.total_ventas()
        }
    except Exception as e:
        data = {
            'titulo': 'Error',
            'mensaje': str(e)
        }
    return data

def get_items_carrito():
    try:
        carrito_item = ItemCarrito.objects.all()
        data = {
            'titulo': 'Página Principal',
            'mensaje': 'Carrito.',
            'carrito_item': carrito_item,
            'total_ventas': ItemCarrito.subtotal()
        }
    except Exception as e:
        data = {
            'titulo': 'Error',
            'mensaje': str(e)
        }
    return data

def home(request):
    data = get_carrito()
    return render(request, 'index.html', data)

def ventas(request):
    data = {
        'titulo': 'Página de Ventas',
        'mensaje': 'Bienvenido a la página de ventas.'
    }
    return render(request, 'ventas.html', data)

def paramVentas(request, id):
    try:
        carrito = Carrito.objects.get(id=id)
        data = {
            'titulo': 'Detalles del Carrito',
            'carrito': carrito,
            'id': carrito.id,
            'producto': carrito.producto,
            'cantidad': carrito.cantidad,
            'precio_unitario': carrito.precio_unitario,
            'subtotal': carrito.subtotal
        }
    except Carrito.DoesNotExist:
        data = {
            'titulo': 'Error',
            'mensaje': 'Carrito no encontrado.'
        }
        
    print(f"ID del carrito: {id}")
    return render(request, 'ventas_detalle.html', data)

def paramVentasGenerales(request):
    data = get_carrito()
    return render(request, 'ventas_generales.html', data)

def generar_registro(request):
    nombre = 'acetaminofen'
    descripcion = 'pastas'
    categoria = Categoria(nombre='medicamento') 
    categoria.save()
    precio = '2'
    stock = '3'
    fecha_caducidad = '3000-10-08'
    
    nuevo_registro = Producto(
        nombre = nombre,
        descripcion = descripcion,
        categoria = categoria,
        precio = precio,
        stock = stock,
        fecha_caducidad = fecha_caducidad
    )
    nuevo_registro.save()
    return HttpResponse("Registro generado exitosamente.")

def generar_item_carrito(request):
    try:
        # Toma primer usuario
        usuario = Usuario.objects.first()
        if not usuario:
            return HttpResponse("No hay usuarios creados.", status=400)

        # Toma primera categoria
        categoria = Categoria.objects.first()
        if not categoria:
            categoria = Categoria(nombre="Categoría por defecto")
            categoria.save()

        # Crear el producto correctamente con todos los campos requeridos
        producto = Producto(
            nombre="Ejemplo",
            descripcion="Producto de prueba",
            categoria=categoria,
            precio=81,
            stock=50,
            fecha_caducidad="2030-12-31"
        )
        producto.save()

        # Crear el carrito asociado al usuario
        carrito = Carrito(usuario=usuario)
        carrito.save()

        # Crear el item del carrito
        nuevo_item_carrito = ItemCarrito(
            carrito=carrito,
            producto=producto,
            cantidad=21,
            precio_unitario=81
        )
        nuevo_item_carrito.save()

        return HttpResponse("Item generado en carrito exitosamente.")

    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

def generar_carrito(request):
    usuario = Usuario()
    usuario.save()
    fecha_creacion = '2500-10-08'

    nuevo_carrito = Carrito(
        usuario = usuario,
        fecha_creacion = fecha_creacion
    )

    nuevo_carrito.save()
    return HttpResponse("Item generado en carrito exitosamente.")