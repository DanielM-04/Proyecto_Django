from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.db import connection

def crear_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)  # No guardar aún
            usuario.set_password(formulario.cleaned_data['password'])  # Establecer la contraseña
            usuario.save()  # Guardar el usuario en la base de datos
            return redirect('listar_usuarios')  # Redirige a la lista de usuarios
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