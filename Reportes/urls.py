from django.urls import path
from .views import goIndex,Saludar,traerReporte, crearReporte, guardarReporte, verEliminarReporte,traerTodosReportes,modificarReporte, eliminarReporte,guardarCambios

urlpatterns = [
    path('index/', goIndex, name= 'goIndex'),
    path('home/',Saludar, name='saludar'),
    path('', traerTodosReportes, name='listar_reportes'),
    path('reporte/<int:id_reporte>/', traerReporte, name='reporte'),
    path('crear_reporte/', crearReporte, name= "crear_reporte"),
    path('registrar_reporte/', guardarReporte , name= "guardar_reporte"),

    path('eliminar_reporte_ver/<int:id_eliminar>/', verEliminarReporte, name= "ver_eliminar_reporte"),
    path('eliminar_reporte/<int:id_eliminar>/',eliminarReporte, name="eliminar_reporte"),
    
    path('modificar_reporte/<int:id_modificar>/', modificarReporte, name="modificar_reporte"),
    path('actualizar_reporte/<int:id_modificar>/', guardarCambios, name="guardar_cambios")
]