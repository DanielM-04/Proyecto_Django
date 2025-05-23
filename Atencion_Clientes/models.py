from django.db import models
from Usuarios.models import Usuario

class Consulta(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas')
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    respondido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente.username} - {self.asunto}"
