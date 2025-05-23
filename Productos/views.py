from django.shortcuts import render

def productos(request):
    # Puedes pasar contexto con datos reales o de prueba
    context = {
        "titulo": "Listado de Productos",
        "productos": ["Producto A", "Producto B", "Producto C"]
    }
    return render(request, 'index_productos.html', context)
