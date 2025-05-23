from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'stock', 'fecha_caducidad', 'ranking','imagen']

        widgets = {
            'fecha_caducidad': forms.DateInput(attrs={'type': 'date'}),
            'ranking': forms.NumberInput(attrs={'min': 0, 'max': 5, 'step': 0.1}),
        }

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        empty_label="Selecciona una categoría",
        required=False  
    )
