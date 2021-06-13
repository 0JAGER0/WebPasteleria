from django import forms
from django.forms import ModelForm
from .models import formulario, registro, listadoTortas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioForm(ModelForm):

    class Meta:
        model = formulario
        fields = ['rut','nombreCompleto','correo_electronico','numero','mensaje']


class RegistroForm(ModelForm):

    class Meta:
        model = registro
        fields =['idRegistro','nombres','apellidos','usuario','correo','contraseña']


class listadoTortasForm(ModelForm):
    class Meta:
        model = listadoTortas
        fields = ['idtorta','torta','tipotorta','tamaño','stock','foto']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email' ,'password1' ,'password2']
        help_texts = {k:"" for k in fields}
