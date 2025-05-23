from django.urls import path
from .views import ventas, paramVentas, generar_registro, home, paramVentasGenerales, generar_item_carrito, generar_carrito

urlpatterns = [
    path('ventas/', ventas, name='ventas'),
    path('ventas/<int:id>/', paramVentas, name='ventas_detalle'),
    path('ventas-generales/', paramVentasGenerales, name='ventas_generales'),
    path('generar-registro/', generar_registro, name='generar_registro'),
    path('index/', home, name='index'),
    path('generar-item-carrito/', generar_item_carrito, name='generar-item-carrito'),
    path('generar-carrito/', generar_carrito, name='generar-carrito'),
]