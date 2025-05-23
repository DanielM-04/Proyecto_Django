from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Producto, Categoria, Resena
from django.db.models import F, FloatField, ExpressionWrapper
from .forms import ProductoForm 

# --- CRUDs de mierda---

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista.html', {'productos': productos})


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    full_stars = int(producto.ranking)
    half_star = (producto.ranking - full_stars) >= 0.5
    empty_stars = 5 - full_stars - (1 if half_star else 0)
    
    context = {
       'producto': producto,
       'full_stars': range(full_stars),
       'half_star': half_star,
       'empty_stars': range(empty_stars),
    }
    return render(request, 'detalle.html', context)

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto:lista')
    else:
        form = ProductoForm()
    categorias = Categoria.objects.all()
    return render(request, 'formulario.html', {'form': form, 'accion': 'Crear', 'categorias': categorias})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto:lista')
    else:
        form = ProductoForm(instance=producto)
    categorias = Categoria.objects.all()
    return render(request, 'formulario.html', {'form': form, 'accion': 'Editar', 'categorias': categorias, 'producto': producto})



def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto:lista')
    return render(request, 'eliminar.html', {'producto': producto})


def buscar_filtrar_productos(request):
    query = request.POST.get('query', '').strip()
    categoria_id = request.POST.get('categoria', '')
    
    productos = Producto.objects.all()

    if query:
        productos = productos.filter(nombre__icontains=query)

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    categorias = Categoria.objects.all()

    return render(request, 'busqueda.html', {
        'resultados': productos,
        'categorias': categorias,
        'query': query,
        'categoria_seleccionada': int(categoria_id) if categoria_id else ''
    })



def crud_categorias(request):
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        if 'crear' in request.POST:
            nombre = request.POST.get('nombre')
            if nombre:
                Categoria.objects.create(nombre=nombre)
            return redirect('producto:crud_categorias')

        elif 'editar' in request.POST:
            cat_id = request.POST.get('cat_id')
            nueva = request.POST.get('nuevo_nombre')
            if cat_id and nueva:
                categoria = get_object_or_404(Categoria, id=cat_id)
                categoria.nombre = nueva
                categoria.save()
            return redirect('producto:crud_categorias')

        elif 'eliminar' in request.POST:
            cat_id = request.POST.get('cat_id')
            if cat_id:
                categoria = get_object_or_404(Categoria, id=cat_id)
                categoria.delete()
            return redirect('producto:crud_categorias')

    return render(request, 'crud_categorias.html', {'categorias': categorias})


def ranking_productos(request):
     productos = Producto.objects.order_by('-ranking') 
     return render(request, 'ranking.html', {'productos': productos})


def comparar_productos(request):
    productos = Producto.objects.annotate(
        calidad_precio=ExpressionWrapper(
            F('precio') / (F('ranking') + 0.1), 
            output_field=FloatField()
        )
    ).order_by('calidad_precio') 

    return render(request, 'comparar.html', {'productos': productos})

# --- NO CRUD perra ---
