from django.db import models

class Reporte(models.Model):
    Elegir_Periodo = [
        ['Diario', 'Diario'],
        ['Semanal', 'Semanal'],
        ['Mensual', 'Mensual'],
        ['Anual', 'Anual']
    ]
    periodo = models.CharField(max_length=10,choices=Elegir_Periodo)
    total_ventas = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cantidad_transacciones = models.IntegerField()
    metodo_de_pago = models.JSONField(default=dict)
    productos_comprados = models.JSONField(default=dict)
    fecha_creacion_reporte = models.DateTimeField(auto_now_add=True)

class Clientes_Frecuente(models.Model):
    cliente_id = models.IntegerField()
    total_compras = models.IntegerField()
    productos_mas_comprados = models.JSONField(default=list)

class Stoks_Critico(models.Model):
    umbral = models.IntegerField()
    productos_bajo_stock = models.JSONField(default=list)
    fecha_creacion_reporte = models.DateTimeField(auto_now_add=True)
