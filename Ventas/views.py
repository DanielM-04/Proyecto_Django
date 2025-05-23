from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Carrito, Producto, Categoria, ItemCarrito, Usuario

# Obtener los carritos de todos los usuarios
def obtener_carritos():
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

# Obtener los detalles de un carrito específico
def obtener_carrito(id):
    try:
        carrito = Carrito.objects.get(id=id)
        items_del_carrito = ItemCarrito.objects.filter(carrito=carrito)
        data = {
            'titulo': 'Detalles del Carrito',
            'mensaje': 'Detalles del carrito.',
            'carrito': carrito,
            'item': items_del_carrito
        }
    except Carrito.DoesNotExist:
        data = {
            'titulo': 'Error',
            'mensaje': 'Carrito no encontrado.'
        }
    return data

# Vista para mostrar el carrito
def mostrar_carritos(request):
    data = obtener_carritos()
    return render(request, 'ventas_generales.html', data)

# Crear un nuevo carrito
def generar_carrito(request, id=None):
    try:
        usuario = Usuario.objects.get(id=id)
        if usuario:
            # Verifica si ya existe un carrito para el usuario
            carrito_existente = Carrito.objects.filter(usuario=usuario).first()
            if carrito_existente:
                return HttpResponse("Ya existe un carrito para este usuario.")
        
        nuevo_carrito = Carrito(
            usuario=usuario
        )
        nuevo_carrito.save()
        return HttpResponse("Carrito generado exitosamente.")
    except Usuario.DoesNotExist:
        return HttpResponse(f"Error: Usuario con id {id} no encontrado.", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

# Agregar un item al carrito
def agregar_item_carrito(request, id_carrito, id_producto, cantidad=1):
    try:
        carrito = Carrito.objects.get(id=id_carrito)
        producto = Producto.objects.get(id=id_producto)
        usuario = carrito.usuario
        
        # Crear el item del carrito
        nuevo_item_carrito = ItemCarrito(
            carrito=carrito,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=producto.precio
        )
        nuevo_item_carrito.save()

        return HttpResponse("Item agregado al carrito exitosamente.")
    except Carrito.DoesNotExist:
        return HttpResponse(f"Error: Carrito con id {id_carrito} no encontrado.", status=404)
    except Producto.DoesNotExist:
        return HttpResponse(f"Error: Producto con id {id_producto} no encontrado.", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)
    
# Obtener los detalles de un carrito específico
def obtener_venta_carrito(request, id):
    data = obtener_carrito(id)
        
    print(f"ID del carrito: {id}")
    return render(request, 'ventas_detalle.html', data)












# No se va a usar 
def mostrar_productos(request):
    data = obtener_carritos()
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    data['productos'] = ', '.join([str(producto) for producto in productos])
    data['categorias'] = ', '.join([str(categoria) for categoria in categorias])
    return render(request, 'mostrar_productos.html', data)

# No se va a usar 
def generar_usuario(request):
    try:
        nuevo_usuario = Usuario(
            username='usuario_prueba',
            password='contraseña_segura'
        )
        
        # Asegurar que no existe
        if Usuario.objects.filter(username=nuevo_usuario.username).exists():
            return HttpResponse("El usuario ya existe.", status=400)
        
        nuevo_usuario.set_password(nuevo_usuario.password)
        nuevo_usuario.save()
        return HttpResponse("Usuario generado exitosamente.")
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

# No se va a usar 
def generar_producto(request):
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