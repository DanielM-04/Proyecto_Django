from django.db.models.functions import TruncDate
from django.db.models import Count
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.db import connection
from django.contrib.auth import authenticate, login

def crear_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)  
            usuario.set_password(formulario.cleaned_data['password'])  
            usuario.save()  
            return redirect('listar_usuarios')  
    else:
        formulario = UsuarioForm()
    return render(request, 'crear_usuario.html', {'formulario': UsuarioForm})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def ver_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'ver_usuario.html', {'usuario': usuario})

def editar_usuario(request, id):
    return render(request, 'editar_usuario.html', {'formulario': UsuarioForm})

def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})

def buscar_usuario(request):
    query = request.GET.get('q')
    usuarios = Usuario.objects.filter(username__icontains=query) if query else Usuario.objects.all()
    return render(request, 'buscar_usuario.html', {'usuarios': usuarios})

def estadisticas_usuarios(request):
    hoy = timezone.now().date()
    usuarios_por_dia = (
        Usuario.objects
        .annotate(dia=TruncDate('date_joined'))
        .values('dia')
        .annotate(cantidad=Count('id'))
    )
    return render(request, 'estadisticas.html', {'usuarios_por_dia': usuarios_por_dia})
def login_usuario(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario) 
            return redirect('estadisticas')  
        else:
            error = 'Usuario o contraseña incorrectos.'
    return render(request, 'login.html', {'error': error})