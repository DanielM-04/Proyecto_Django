from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito, Producto, Categoria, ItemCarrito, Usuario
from django.http import Http404
from django.utils import timezone

def obtener_carritos():
    carritos = Carrito.objects.all()
    total_general_ventas = Carrito.total_ventas()
    data = {
        'titulo': 'Ventas Generales',
        'mensaje': 'Listado de todos los carritos y ventas totales.',
        'carrito': carritos,
        'total_ventas': total_general_ventas
    }
    return data

def obtener_carrito(id):
    try:
        carrito = Carrito.objects.get(id=id)
        items_del_carrito = ItemCarrito.objects.filter(carrito=carrito)
        data = {
            'titulo': f'Detalles del Carrito {carrito.id}',
            'mensaje': f'Detalles del carrito de {carrito.usuario.username}.',
            'carrito': carrito,
            'item': items_del_carrito
        }
    except Carrito.DoesNotExist:
        data = {
            'titulo': 'Error',
            'mensaje': f'Carrito con id {id} no encontrado.'
            
        }
    return data
def mostrar_carritos(request):
    data = obtener_carritos()
    return render(request, 'ventas_generales.html', data)

def generar_carrito(request, id=None):
    try:
        if id is not None:
            usuario = get_object_or_404(Usuario, id=id)
            mensaje_usuario = f"para el usuario existente {usuario.username}"
        else:
            unique_username = f"user_auto_{timezone.now().strftime('%Y%m%d%H%M%S%f')}"
            usuario = Usuario(username=unique_username)
            usuario.set_password('defaultpassword123') 
            usuario.save()
            mensaje_usuario = f"para el nuevo usuario {usuario.username}"

        carrito_existente = Carrito.objects.filter(usuario=usuario).first()
        if carrito_existente:
            return HttpResponse(f"Ya existe un carrito {mensaje_usuario}.")
        
        nuevo_carrito = Carrito(usuario=usuario)
        nuevo_carrito.save()
        return HttpResponse(f"Carrito generado exitosamente {mensaje_usuario} con ID de carrito {nuevo_carrito.id}.")

    except Http404:
        return HttpResponse(f"Error: Usuario con id {id} no encontrado.", status=404)
    except Exception as e:
        return HttpResponse(f"Error al generar el carrito: {e}", status=500)

def agregar_item_carrito(request, id_carrito, id_producto, cantidad=1):
    try:
        carrito = get_object_or_404(Carrito, id=id_carrito)
        producto = get_object_or_404(Producto, id=id_producto)
        
        item_existente, created = ItemCarrito.objects.get_or_create(
            carrito=carrito,
            producto=producto,
            defaults={'cantidad': cantidad, 'precio_unitario': producto.precio}
        )
        if not created:
            item_existente.cantidad += cantidad
            item_existente.save()
            mensaje = f"Cantidad del item '{producto.nombre}' actualizada en el carrito."
        else:
            mensaje = f"Item '{producto.nombre}' agregado al carrito."
        
        return HttpResponse(mensaje)
    except Http404:
        return HttpResponse("Error: Carrito o Producto no encontrado.", status=404)
    except Exception as e:
        return HttpResponse(f"Error al agregar item al carrito: {e}", status=500)

def eliminar_carrito_vista(request, id_carrito):
    if request.method == 'POST':
        try:
            carrito = get_object_or_404(Carrito, id=id_carrito)
            carrito.delete()
            return redirect('ventas_generales') 
        except Http404:
            return HttpResponse("Error: Carrito no encontrado.", status=404)
        except Exception as e:
            return HttpResponse(f"Error al eliminar el carrito: {e}", status=500)
    return redirect('ventas_generales')

def eliminar_item_carrito_vista(request, id_item_carrito):
    if request.method == 'POST':
        try:
            item_carrito = get_object_or_404(ItemCarrito, id=id_item_carrito)
            id_carrito_actual = item_carrito.carrito.id
            item_carrito.delete()
            return redirect('ventas_detalle', id=id_carrito_actual)
        except Http404:
            return HttpResponse("Error: Item de carrito no encontrado.", status=404)
        except Exception as e:
            return HttpResponse(f"Error al eliminar el item del carrito: {e}", status=500)
    return redirect('ventas_generales')

def obtener_venta_carrito(request, id):
    data = obtener_carrito(id)
        
    print(f"ID del carrito: {id}")
    return render(request, 'ventas_detalle.html', data)

def mostrar_productos_carrito(request, id):
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
    return render(request, 'mostrar_productos.html', data)

def mostrar_productos(request):
    data = obtener_carritos()
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    data['productos'] = ', '.join([str(producto) for producto in productos])
    data['categorias'] = ', '.join([str(categoria) for categoria in categorias])
    return render(request, 'mostrar_productos.html', data)

def generar_usuario(request):
    try:
        nuevo_usuario = Usuario(
            username='usuario_prueba',
            password='contraseña_segura'
        )
        
        if Usuario.objects.filter(username=nuevo_usuario.username).exists():
            return HttpResponse("El usuario ya existe.", status=400)
        
        nuevo_usuario.set_password(nuevo_usuario.password)
        nuevo_usuario.save()
        return HttpResponse("Usuario generado exitosamente.")
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

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
