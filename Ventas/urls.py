from django.urls import path
from .views import saludar
# from .views import

urlpatterns = [
    path('', saludar, name="ventas_app")
    
]