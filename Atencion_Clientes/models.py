from django.db import models

class TicketAtencion(models.Model):
    ESTADO_CHOICES = [
        ('Abierto', 'Abierto'),
        ('En Proceso', 'En Proceso'),
        ('Cerrado', 'Cerrado')
    ]
    cliente_id = models.IntegerField()
    asunto = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='Abierto')
    metodo_contacto = models.CharField(max_length=50, default='Formulario Web')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket #{self.id} - {self.asunto} ({self.estado})"


class HistorialInteraccion(models.Model):
    ticket = models.ForeignKey(TicketAtencion, on_delete=models.CASCADE, related_name='interacciones')
    mensaje = models.TextField()
    emisor = models.CharField(max_length=50, default='Cliente')  
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.emisor} en Ticket #{self.ticket.id}"


class ValoracionAtencion(models.Model):
    ticket = models.OneToOneField(TicketAtencion, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()  
    comentario = models.TextField(blank=True, null=True)
    fecha_valoracion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Valoración {self.puntuacion}/5 para Ticket #{self.ticket.id}"