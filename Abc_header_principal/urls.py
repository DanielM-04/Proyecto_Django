from django.urls import path, include

urlpatterns = [
    # otras urls...
    path('productos/', include('productos.urls')),
]
