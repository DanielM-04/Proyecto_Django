from django.urls import path
from . import views

app_name = 'producto'

urlpatterns = [
    path('', views.lista_productos, name='lista'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle'),
    path('crear/', views.crear_producto, name='crear'),
    path('editar/<int:id>/', views.editar_producto, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar'),
    path('buscar/', views.buscar_filtrar_productos, name='buscar'),
    path('ranking/', views.ranking_productos, name='ranking'),
    path('comparar/', views.comparar_productos, name='comparar'),
    path('categorias/', views.crud_categorias, name='crud_categorias'),

]
