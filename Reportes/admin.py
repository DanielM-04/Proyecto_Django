from django.contrib import admin
from . models import Reporte, ClienteFrecuente, StockCritico


admin.site.register(Reporte)
admin.site.register(ClienteFrecuente)
admin.site.register(StockCritico)

# Register your models here.
