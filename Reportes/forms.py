from django import forms
from .models import Reporte
import json # Necesario para validación personalizada si no se usa forms.JSONField o para lógica adicional

class ReporteForm(forms.Form):
    periodo = forms.ChoiceField(
        choices=Reporte.PERIODOS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    total_ventas = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 500000.00'
        }),
        label="Total de Ventas"
    )
    
    cantidad_transacciones = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 10'
        }),
        label="Cantidad de Transacciones"
    )

    # Opción 1: Usando forms.JSONField (Recomendado si Django >= 3.1)
    metodo_de_pago = forms.JSONField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3, # Ajustar según sea necesario
            'placeholder': 'Ingrese el método de pago en formato JSON.\nEjemplo: {"efectivo": 150000, "tarjeta": 350000}'
        }),
        label="Métodos de Pago (JSON)",
        help_text='Estructura JSON esperada: {"metodo1": valor1, "metodo2": valor2}'
    )

    productos_comprados = forms.JSONField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5, # Ajustar según sea necesario
            'placeholder': 'Ingrese los productos comprados en formato JSON.\nEjemplo: { "Producto A": 5, "Producto B": 2 }'
        }),
        label="Productos Comprados (JSON)",
        help_text='Estructura JSON esperada: {"nombre_producto1": cantidad1, "nombre_producto2": cantidad2}'
    )