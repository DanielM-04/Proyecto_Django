from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporte
import datetime

def Saludar(request):
    return HttpResponse("Hol mundo")

def goIndex(request):
    dia_acutal = datetime.date.today().day
    mes_actual = datetime.date.today().month
    data = {
        'nombre':'Daniel',
        'apellido':'Melo',
        'ciudad':'Bogota',
        'dia':dia_acutal,
        'mes':mes_actual 
    }
    return render(request, 'index.html',data)

def traerReporte(request, id_reporte):
    reporte = Reporte.objects.get(id=id_reporte)
    return render(request,'reportes.html',{'reporte':reporte})