from django import forms
from .models import Usuario

""" class UsuarioForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    telefono = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=100) """

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'telefono', 'direccion','es_cliente', 'es_admin']
        widgets = {
            'password': forms.PasswordInput(),
        }