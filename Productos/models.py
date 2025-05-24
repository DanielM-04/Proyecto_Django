from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_caducidad = models.DateField()
    ranking = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

# --- esta mierda ---

class Resena(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='resenas')
    usuario = models.CharField(max_length=100)  
    puntuacion = models.PositiveSmallIntegerField() 
    comentario = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Resena {self.puntuacion} para {self.producto.nombre}'

class ProductoComparacion(models.Model):
    producto1 = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comparaciones_producto1')
    producto2 = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comparaciones_producto2')
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('producto1', 'producto2')

    def __str__(self):
        return f'Comparación entre {self.producto1.nombre} y {self.producto2.nombre}'
