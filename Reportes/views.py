from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Reporte

from .forms import ReporteForm
from django.template.loader import render_to_string
from xhtml2pdf import pisa


import json
import datetime




def generar_pdf_unico(request, id_generar_reporte):
    reporte = Reporte.objects.get(id=id_generar_reporte)
    html_string = render_to_string('reporte_pdf.html',{'reporte': reporte})

    response_content = HttpResponse(content_type='application/pdf')
    response_content['Content-Disposition'] = f'attachment; filename = "reporte id{id_generar_reporte}.pdf" '

    pisa_html_to_pdf = pisa.CreatePDF(html_string, dest=response_content)

    if pisa_html_to_pdf.err:
        return HttpResponse(f"Error al generar el pdf ")
    
    return response_content


def generar_pdf(request):
    reporte_drogueria = Reporte.objects.all()
    html_reporte = render_to_string('drogueria_pdf.html', {'reportes':reporte_drogueria})

    response_content = HttpResponse(content_type='application/pdf')
    dia_acutal = datetime.date.today().day
    mes_actual = datetime.date.today().month
    response_content['Content-Disposition'] = f'attachment; filename = "reporteDrogueria_{dia_acutal}_x|{mes_actual}.pdf"'

    pisa_to_pdf = pisa.CreatePDF(html_reporte, dest=response_content)

    if pisa_to_pdf.err:
        print("Sucedio un error")
    
    return response_content


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
    return render(request,'reporte_individual.html',{'reporte':reporte})

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
    monto_minimo = request.GET.get('monto_minimo')
    monto_maximo = request.GET.get('monto_maximo')
    
    if monto_minimo:
        lista_reportes = lista_reportes.filter(total_ventas__gte=monto_minimo)
    if monto_maximo:
        lista_reportes = lista_reportes.filter(total_ventas__lte=monto_maximo)
    print("Total reportes:", Reporte.objects.count())
    return render(request,'listar_reportes.html',{'lista_reportes':lista_reportes})






def traerReporteIndividual(request, id_reporte):
    reporte = Reporte.objects.get(id=id_reporte)
    return reporte

def verEliminarReporte(request, id_eliminar):
    ver_reporte_eliminar = traerReporteIndividual(request, id_eliminar)
    return render(request,'eliminar_reporte.html', {"reporte":ver_reporte_eliminar})

def eliminarReporte(request, id_eliminar):
    try:
            
        reporte = Reporte.objects.get(id=id_eliminar)
        reporte.delete()
        print("Se elemino con exito el registro con el id",id_eliminar)
    except Exception as e:
        print("No  se pudo eliminar --> ",e)


    return redirect('listar_reportes')
            

def modificarReporte(request, id_modificar):

    reporte = traerReporteIndividual(request, id_modificar)
    data_reporte = {
        'periodo': reporte.periodo,
        'total_ventas':reporte.total_ventas,
        'cantidad_transacciones': reporte.cantidad_transacciones,
        'metodo_de_pago':reporte.metodo_de_pago,
        'productos_comprados': reporte.productos_comprados
    }

    form = ReporteForm(initial=data_reporte)
    data = {
        'form':form,
        'id':id_modificar
    }
    return render(request,'modificar_reporte.html', {'data':data})

def guardarCambios(request, id_modificar):
    print("Entro aquiiii")
    if request.method == 'POST':
        try:
            reporte = Reporte.objects.get(id= id_modificar)
            reporte.periodo = request.POST.get('periodo')
            reporte.total_ventas = request.POST.get('total_ventas')
            reporte.cantidad_transacciones = request.POST.get('cantidad_transacciones')
            reporte.metodo_de_pago = json.loads(request.POST.get('metodo_de_pago'))
            reporte.productos_comprados = json.loads(request.POST.get('productos_comprados'))
            
            
            try:
                reporte.save()
                print("Reporte actualizado correctamente")
            except Exception as e:
                print(f"No se pudo guardar por {e}")

            return redirect('listar_reportes')
           
        except Exception as e:
            print(f"Error al guardar el reporte: {e}")
            return redirect('listar_reportes')

    else:
        print("No se guardo")
        return redirect('saludar')
