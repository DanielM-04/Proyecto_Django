from django.contrib import admin
from . models import Reporte, Clientes_Frecuente, Stoks_Critico


admin.site.register(Reporte)
admin.site.register(Clientes_Frecuente)
admin.site.register(Stoks_Critico)

# Register your models here.
