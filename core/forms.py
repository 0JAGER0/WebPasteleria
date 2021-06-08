from django import forms
from django.forms import ModelForm
from .models import formulario, registro


class FormularioForm(ModelForm):

    class Meta:
        model = formulario
        fields = ['rut','nombreCompleto','correo_electronico','numero','mensaje']




class RegistroForm(ModelForm):

    class Meta:
        model = registro
        fields =['idRegistro','nombres','apellidos','usuario','correo','contraseña']





