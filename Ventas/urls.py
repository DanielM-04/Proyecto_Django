from django.urls import path
from .views import ventas, paramVentas, generar_registro, home, paramVentasGenerales

urlpatterns = [
    path('ventas/', ventas, name='ventas'),
    path('ventas/<int:id>/', paramVentas, name='ventas_detalle'),
    path('ventas-generales/', paramVentasGenerales, name='ventas_generales'),
    path('generar-registro/', generar_registro, name='generar_registro'),
    path('index/', home, name='index'),
]