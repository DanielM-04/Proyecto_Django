from django.contrib import admin
from .models import Categoria, Producto,ProductoComparacion,Resena

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(ProductoComparacion)
admin.site.register(Resena)

# Register your models here.
