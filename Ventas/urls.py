from django.urls import path
from .views import (
    obtener_venta_carrito, generar_producto, mostrar_carritos, 
    agregar_item_carrito, generar_carrito, mostrar_productos_carrito, 
    generar_usuario, eliminar_carrito_vista, eliminar_item_carrito_vista # Añadir nuevas vistas
)

urlpatterns = [
    path('ventas/<int:id>/', obtener_venta_carrito, name='ventas_detalle'),
    path('ventas-generales/', mostrar_carritos, name='ventas_generales'),
    path('generar-registro/', generar_producto, name='generar_registro'),
    path('generar-usuario/', generar_usuario, name='generar_usuario'),
    
    path('generar-carrito/<int:id>/', generar_carrito, name='generar_carrito_para_usuario'), 
    path('generar-carrito/nuevo/', generar_carrito, name='generar_nuevo_usuario_y_carrito'),

    path('agregar-item-carrito/<int:id_carrito>/<int:id_producto>/<int:cantidad>/', agregar_item_carrito, name='agregar_item_carrito'),
    path('mostrar-productos/<int:id>/', mostrar_productos_carrito, name='mostrar_productos_carrito'),

    path('eliminar-carrito/<int:id_carrito>/', eliminar_carrito_vista, name='eliminar_carrito'),
    path('eliminar-item/<int:id_item_carrito>/', eliminar_item_carrito_vista, name='eliminar_item_carrito'),
]