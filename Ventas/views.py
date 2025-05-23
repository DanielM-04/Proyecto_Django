from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def saludar(request):
    return render(request, 'index_ventas.html', {"saludo":"hola desde la app de ventas"})