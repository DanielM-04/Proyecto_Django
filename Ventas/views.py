from django.http import HttpResponse
from django.shortcuts import render
from .models import Carrito, ProcesoCheckout, Factura, HistorialCompras, Devolucion

def get_carrito():
    try:
        carrito = Carrito.objects.all()
        data = {
            'titulo': 'Página Principal',
            'mensaje': 'Bienvenido a la página principal.',
            'carrito': carrito,
            'total_ventas': sum(item.subtotal for item in carrito)
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
    producto = 'Medicamento Z'
    cantidad = 10
    precio_unitario = 50.00
    subtotal = cantidad * precio_unitario
    
    nuevo_registro = Carrito(
        producto=producto,
        cantidad=cantidad,
        precio_unitario=precio_unitario,
        subtotal=subtotal
    )
    nuevo_registro.save()
    return HttpResponse("Registro generado exitosamente.")