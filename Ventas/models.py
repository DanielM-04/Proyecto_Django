from django.db import models

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        unidad = "unidad" if self.cantidad == 1 else "unidades"
        return f"{self.id} - {self.producto} - {self.cantidad} {unidad} - ${self.precio_unitario} c/u - Subtotal: ${self.subtotal}"
    
class ProcesoCheckout(models.Model):
    id = models.AutoField(primary_key=True)
    direccion_envio = models.CharField(max_length=255)
    metodo_pago = models.CharField(max_length=50)
    estado_pago = models.CharField(max_length=50, default='Pendiente')
    fecha_pago = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Checkout {self.id} - {self.usuario.username} {self.estado_pago}"
    
class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    proceso_checkout = models.ForeignKey(ProcesoCheckout, on_delete=models.CASCADE)
    # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Factura {self.id} - Total: {self.total}"
    
class HistorialCompras(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Compra {self.id} - Cliente: {self.factura.usuario.username}"
    
class Devolucion(models.Model):
    id = models.AutoField(primary_key=True)
    motivo = models.CharField(max_length=255)
    fecha_devolucion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Devolucion {self.id} - Factura: {self.factura.id} - Estado: {self.estado}"