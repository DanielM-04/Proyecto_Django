from django.db import models
from Usuarios.models import Usuario
from Productos.models import Producto

class Reporte(models.Model):
    PERIODOS = [
        ('Diario', 'Diario'),
        ('Semanal', 'Semanal'),
        ('Mensual', 'Mensual'),
        ('Anual', 'Anual')
    ]
    periodo = models.CharField(max_length=10, choices=PERIODOS)
    total_ventas = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_transacciones = models.IntegerField()
    fecha_creacion_reporte = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reporte {self.get_periodo_display()} - {self.fecha_creacion_reporte.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Reporte de Ventas"
        verbose_name_plural = "Reportes de Ventas"
        ordering = ['-fecha_creacion_reporte']

class ClienteFrecuente(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reportes_cliente_frecuente')
    total_compras = models.IntegerField()
    productos_mas_comprados = models.ManyToManyField(Producto, related_name='reportes_producto_frecuente')
    fecha_calculo = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cliente Frecuente: {self.cliente.username} - {self.total_compras} compras"

    class Meta:
        verbose_name = "Cliente Frecuente"
        verbose_name_plural = "Clientes Frecuentes"
        ordering = ['-total_compras', 'cliente__username']


class StockCritico(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='reportes_stock_critico')
    stock_actual = models.IntegerField()
    umbral = models.IntegerField(default=10)
    fecha_creacion_reporte = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Stock Crítico: {self.producto.nombre} (Actual: {self.stock_actual}, Umbral: {self.umbral})"

    class Meta:
        verbose_name = "Reporte de Stock Crítico"
        verbose_name_plural = "Reportes de Stock Crítico"
        ordering = ['-fecha_creacion_reporte', 'producto__nombre']
