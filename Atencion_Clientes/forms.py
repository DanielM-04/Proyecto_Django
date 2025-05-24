from django import forms
from .models import TicketAtencion

class TicketAtencionForm(forms.ModelForm):
    class Meta:
        model = TicketAtencion
        fields = ['cliente_id', 'asunto', 'descripcion', 'metodo_contacto']
