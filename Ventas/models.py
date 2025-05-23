from django.db import models
from Usuarios.models import Usuario
from Productos.models import Producto

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username} - {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}"

    @property
    def total_carrito(self):
        # Calcula el total sumando los subtotales de todos los ItemCarrito asociados
        return sum(item.subtotal for item in self.items.all())

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.carrito}"

class ProcesoCheckout(models.Model):
    ESTADO_PAGO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        ('Fallido', 'Fallido'),
        ('Reembolsado', 'Reembolsado'),
    ]
    
    METODO_PAGO_CHOICES = [
        ('TarjetaCredito', 'Tarjeta de Crédito'),
        ('TarjetaDebito', 'Tarjeta de Débito'),
        ('PSE', 'PSE'),
        ('Efectivo', 'Efectivo'), # Ejemplo, si aplica
    ]

    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    direccion_envio = models.CharField(max_length=255)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO_CHOICES)
    estado_pago = models.CharField(max_length=50, choices=ESTADO_PAGO_CHOICES, default='Pendiente')
    fecha_pago = models.DateTimeField(auto_now_add=True) # Considerar null=True, blank=True si el pago no es inmediato

    @property
    def total(self):
        # El total del checkout es el total del carrito asociado
        return self.carrito.total_carrito

    def __str__(self):
        return f"Checkout para {self.carrito} - Estado: {self.get_estado_pago_display()}"

class Factura(models.Model):
    proceso_checkout = models.OneToOneField(ProcesoCheckout, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    # Podrías añadir un campo para el número de factura si es necesario
    # numero_factura = models.CharField(max_length=50, unique=True, blank=True, null=True)


    def __str__(self):
        return f"Factura {self.id} para {self.proceso_checkout.carrito.usuario.username} - {self.fecha_emision.strftime('%Y-%m-%d')}"

    @property
    def total_factura(self):
        return self.proceso_checkout.total

class HistorialCompras(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='historial_compras')
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True) # Esto podría ser redundante si Factura.fecha_emision es suficiente

    def __str__(self):
        return f"Compra de {self.usuario.username} - Factura {self.factura.id} - {self.fecha_compra.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name_plural = "Historial de Compras"
        ordering = ['-fecha_compra']


class Devolucion(models.Model):
    ESTADO_DEVOLUCION_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
        ('Procesada', 'Procesada'),
    ]

    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='devoluciones')
    # Considerar añadir una relación a ItemCarrito si las devoluciones son por ítem específico
    # item_carrito = models.ForeignKey(ItemCarrito, on_delete=models.SET_NULL, null=True, blank=True)
    motivo = models.TextField() # TextField podría ser más apropiado para un motivo detallado
    fecha_devolucion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADO_DEVOLUCION_CHOICES, default='Pendiente')

    def __str__(self):
        return f"Devolución para Factura {self.factura.id} - Estado: {self.get_estado_display()}"

    class Meta:
        verbose_name_plural = "Devoluciones"
        ordering = ['-fecha_devolucion']
