from django.urls import path
<<<<<<< HEAD
from .views import obtener_venta_carrito, generar_producto, mostrar_carritos, agregar_item_carrito, generar_carrito, mostrar_productos, generar_usuario

urlpatterns = [
    path('ventas/<int:id>/', obtener_venta_carrito, name='ventas_detalle'),
    path('ventas-generales/', mostrar_carritos, name='ventas_generales'),
    path('generar-registro/', generar_producto, name='generar_registro'),
    path('generar-usuario/', generar_usuario, name='generar-usuario'),
=======
from .views import saludar
# from .views import

urlpatterns = [
    path('', saludar, name="ventas_app")
>>>>>>> Productos
    
    path('generar-carrito/<int:id>/', generar_carrito, name='generar-carrito'),
    path('agregar-item-carrito/<int:id_carrito>/<int:id_producto>/<int:cantidad>', agregar_item_carrito, name='generar-item-carrito'),
    path('mostrar-productos/', mostrar_productos, name='mostrar-productos'),
]