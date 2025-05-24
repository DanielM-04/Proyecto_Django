from django import views
from django.urls import path
from .views import crear_usuario, listar_usuarios,ver_usuario,editar_usuario,eliminar_usuario,buscar_usuario, login_usuario, estadisticas_usuarios

urlpatterns = [
    path('crear/', crear_usuario, name='crear_usuario'),
    path('', listar_usuarios, name='listar_usuarios'),
    path('<int:id>/', ver_usuario, name='ver_usuario'),
    path('editar/<int:id>/', editar_usuario, name='editar_usuario'),
    path('eliminar/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
    path('buscar/', buscar_usuario, name='buscar_usuario'),
    path('estadisticas/', estadisticas_usuarios, name='estadisticas'),
    path('login/', login_usuario, name='login'),
]