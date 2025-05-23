from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Reporte
from .forms import ReporteForm

import json
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


def crearReporte(request):
    return render(request, 'crear_reporte.html', {'form': ReporteForm})

def guardarReporte(request):
    print("Entro aquiiii")
    if request.method == 'POST':
        try:
            reporte = Reporte(
                periodo = request.POST.get('periodo'),
                total_ventas = request.POST.get('total_ventas'),
                cantidad_transacciones = request.POST.get('cantidad_transacciones'),
                metodo_de_pago = json.loads(request.POST.get('metodo_de_pago')),
                productos_comprados = json.loads(request.POST.get('productos_comprados'))
            )
            
            try:
                reporte.save()
                print("Reporte guardado correctamente")
            except Exception as e:
                print(f"No se pudo guardar por {e}")

            return redirect('listar_reportes')
           
        except Exception as e:
            print(f"Error al guardar el reporte: {e}")
            return redirect('listar_reportes')

    else:
        print("No se guardo")
        return redirect('saludar')
    




def traerTodosReportes(request):
    lista_reportes = Reporte.objects.all()
    print("Total reportes:", Reporte.objects.count())
    return render(request,'listar_reportes.html',{'lista_reportes':lista_reportes})


def eliminarReporte(request):
    data = {
        'Saludar': 'Daniel',
    }
    return render(request,'eliminar_reporte.html',data)
    # reporte = Reporte.objects.get(id=id_reporte)
    # reporte.delete
            
def modificarReporte(request):
    return render(request,'modificar_reporte.html')
