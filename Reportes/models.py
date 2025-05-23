from django.db import models
from Usuarios.models import Usuario  
from Productos.models import Producto  

class Reporte(models.Model):
    Elegir_Periodo = [
        ['Diario', 'Diario'],
        ['Semanal', 'Semanal'],
        ['Mensual', 'Mensual'],
        ['Anual', 'Anual']
    ]
    periodo = models.CharField(max_length=10, choices=Elegir_Periodo)
    total_ventas = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cantidad_transacciones = models.IntegerField()
    metodo_de_pago = models.JSONField(default=dict)
    productos_comprados = models.JSONField(default=dict)
    fecha_creacion_reporte = models.DateTimeField(auto_now_add=True)

class ClienteFrecuente(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    total_compras = models.IntegerField()
    productos_mas_comprados = models.ManyToManyField(Producto)  
    
class StockCritico(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    umbral = models.IntegerField(default=10)
    fecha_creacion_reporte = models.DateTimeField(auto_now_add=True)