from django.urls import path
from .views import goIndex,Saludar,traerReporte

urlpatterns = [
    path('index/', goIndex, name= 'goIndex'),
    path('home/',Saludar, name='saludar'),
    path('reporte/<int:id_reporte>/', traerReporte, name='reporte'),
]