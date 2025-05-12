from django.urls import path
from .views import goIndex,Saludar,traerReporte, crearReporte, guardarReporte, eliminarReporte,traerTodosReportes,modificarReporte

urlpatterns = [
    path('index/', goIndex, name= 'goIndex'),
    path('home/',Saludar, name='saludar'),
    path('', traerTodosReportes, name='listar_reportes'),
    path('reporte/<int:id_reporte>/', traerReporte, name='reporte'),
    path('crear_reporte/', crearReporte, name= "crear_reporte"),
    path('registrar_reporte/', guardarReporte , name= "guardar_reporte"),
    path('eliminar_reporte/', eliminarReporte, name= "eliminar_reporte"),
    path('modificar_reporte/', modificarReporte, name="modificar_reporte"),
]