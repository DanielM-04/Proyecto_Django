from django.contrib import admin
from .models import Carrito, ProcesoCheckout, Factura, HistorialCompras, Devolucion

admin.site.register(Carrito)
admin.site.register(ProcesoCheckout)
admin.site.register(Factura)
admin.site.register(HistorialCompras)
admin.site.register(Devolucion)