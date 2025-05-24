from django.urls import path, include

urlpatterns = [
    path('ventas/', include('ventas.urls')),
    path('productos/', include('productos.urls')),
]
