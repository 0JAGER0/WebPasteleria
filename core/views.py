from core.forms import FormularioForm,RegistroForm, listadoTortasForm
from django.shortcuts import redirect, render
from .models import formulario, registro, listadoTortas
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UsernameField


# Create your views here.


def Start(request):

    return render(request,'core/Start.html')

def nosotros(request):

    return render(request,'core/nosotros.html')

def logout(request):

    return render(request,'core/logout.html')

def productos(request):

    return render(request,'core/productos.html')

def contacto(request):
    return render(request,'core/contacto.html')

def formularioContac(request):
    return render(request,'core/formularioContac.html')


def loginadmin(request):

    if request.method == 'POST':
        
        form = LoginView(request.POST) 
        if UsernameField == 'admin':

            return redirect('mantenedor')


    return render(request,'core/loginadmin.html')

def registros(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} a sido creado')
            return redirect('Start')
    else:
        form = UserRegisterForm()

    context = { 'form' : form }

    return render(request,'core/registros.html',context)

def operaBlanca(request):
    return render(request,'core/operaBlanca.html')

def merengueframbuesa(request):
    return render(request,'core/merengue-frambuesa.html')

def login(request):
    return render(request,'core/login.html')

def hojaRasca(request):
    return render(request,'core/hojaRasca.html')

def HojaldreManjar(request):
    return render(request,'core/Hojaldre_Manjar.html')

def Cassatta(request):
    return render(request,'core/Cassatta.html')


def mantenedor(request):
    tortas = listadoTortas.objects.all()

    datos = {
        'tortas':tortas
    }

    return render(request,'core/mantenedor.html',datos)

def mantenedormod(request,pk):

    torta = listadoTortas.objects.get(idtorta = pk)

    datos = {
        'form':listadoTortasForm(instance=torta)
    }

    if request.method == 'POST':

        formularioeditado = listadoTortasForm(request.POST,request.FILES,instance=torta)


        if formularioeditado.is_valid:
            formularioeditado.save()

            datos['mensaje']='Datos actualizados'
        else:
            datos['mensaje']='Hubo algun error intentelo de nuevo '

    return render(request,'core/mantenedormod.html',datos)

def BiscochoFrambuesa(request):
    return render(request,'core/Biscocho-Frambuesa.html')

def agregarTorta(request):

    datos = {
        'form':listadoTortasForm()
    }

    if request.method=='POST':
        formularioo = listadoTortasForm(request.POST,request.FILES)
        try:
            if formularioo.is_valid:
                formularioo.save()

                datos['mensaje'] ="guardados correctamente"

        except:
            datos['mensaje'] ="no se pudo guardar"
        

    return render(request,'core/agregartorta.html',datos)

def deletorta(request,pk):

    torta = listadoTortas.objects.get(idtorta = pk)

    torta.delete()

    return redirect(to='mantenedor')

def deletortaLista(request,pk):

    

    torta = listadoTortas.objects.get(idtorta = pk)
    
    torta.delete()

    return redirect(to='listadocompra')


def listadocompra(request):

    tortas = listadoTortas.objects.all()

    datos = {
        'tortas':tortas
    }

    return render(request,'core/listadocompra.html',datos)