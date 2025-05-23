from django.urls import path
from .views import  traeTicket, crearTicket,eliminarTicket, modificarEstado


urlpatterns = [
    path('', traeTicket, name="traer_tickets"),
    path('crear/', crearTicket, name="crear_ticket"),
    path('eliminar/<int:ticket_id>/', eliminarTicket, name="eliminar_ticket"),
    path('actualizar/<int:id_ticket>/', modificarEstado, name="actualizar_estado_ticket"),


    
]
