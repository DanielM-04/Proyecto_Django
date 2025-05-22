from django import forms
from .models import Reporte

class ReporteForm(forms.Form):
    periodo = forms.ChoiceField(choices=Reporte.Elegir_Periodo)
    total_ventas = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 500000.00'
        }))
    
    cantidad_transacciones = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 10'
        }))

   
    metodo_de_pago = forms.CharField(
                widget=forms.Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Ingrese el método de pago en formato JSON ejemplo:{"efectivo":valor,"tarjeta":valor}'
            }))

    productos_comprados = forms.CharField(
                widget=forms.Textarea(attrs={
                        'class': 'form-control',
                        'placeholder': 'Ingrese los productos comprados en formato JSON ejemplo:{ "nombre_medicamento":cantidad, "nombre_medicamento2":cantidad},....}'                     
                })
    )


