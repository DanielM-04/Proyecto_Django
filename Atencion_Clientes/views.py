from django.shortcuts import render, redirect
from .models import TicketAtencion
from .forms import TicketAtencionForm



def traeTicket(request):
    tickets = TicketAtencion.objects.all()
    return render(request,'indexatencion.html', {'tickets':tickets} )


def crearTicket(request):
    form = TicketAtencionForm()
    if request.method == 'POST':
        form = TicketAtencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traer_tickets')
    return render(request, 'crear_ticket.html', {'form': form})


def eliminarTicket(request, ticket_id ):
    ticket = TicketAtencion.objects.get(id = ticket_id )
    if request.method == 'POST':
        ticket.delete()
        return redirect('traer_tickets')
    return render(request, 'confimar_eliminar.html', {'ticket':ticket})


def modificarEstado(request, id_ticket):
    ticket = TicketAtencion.objects.get(id=id_ticket) 

    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado:
            ticket.estado = nuevo_estado
            ticket.save()
            return redirect('traer_tickets')

    return render(request, 'actualizar_estado.html', {'ticket': ticket})

