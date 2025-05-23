from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def saludar(request):
    return render(request, 'indexatencion.html', {"saludo": "Hola desde atencion"})
