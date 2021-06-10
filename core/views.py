from core.forms import FormularioForm,RegistroForm, listadoTortasForm
from django.shortcuts import redirect, render
from .models import formulario, registro, listadoTortas


# Create your views here.


def Start(request):

    formularios = formulario.objects.all()

    datos= {
        'formularios':formularios
    }

    return render(request,'core/Start.html', datos)

def nosotros(request):

    datos = {
        'form':FormularioForm() 
    }

    if request.method=='POST':
        formularioo = FormularioForm(request.POST)
        if request.method == 'POST':
            try:
                if formularioo.is_valid:
                    formularioo.save()

                    datos['mensaje'] ="guardados correctamente"

            except:
                datos['mensaje'] ="no se pudo guardar"
    

    return render(request,'core/nosotros.html',datos)


def productos(request, id):

    formulariio = formulario.objects.get(rut=id)

    datoss = {
        'form': FormularioForm(instance=formulariio)
    }

    if request.method== 'POST':

        formulariio = FormularioForm(data=request.POST,instance=formulario)

        if formulariio.is_valid:
            formulariio.save()

            datoss['mensaje'] = "modificados correctamente"

    return render(request,'core/productos.html',datoss)

def contacto(request):
    return render(request,'core/contacto.html')

def formularioContac(request):
    return render(request,'core/formularioContac.html')

def registros(request):

    datos = {
        'form':RegistroForm() 
    }

    if request.method=='POST':
        formulariio = RegistroForm(request.POST)
        if request.method == 'POST':
            try:
                if formulariio.is_valid:
                    formulariio.save()

                    datos['mensaje'] ="GUARDADO"

            except:
                datos['mensaje'] ="NO GUARDADO"

    return render(request,'core/registros.html')


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
        formularioeditado = listadoTortasForm(data=request.POST,instance=torta)

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
        formularioo = listadoTortasForm(request.POST)
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


def listadocompra(request):

    tortas = listadoTortas.objects.all()

    datos = {
        'tortas':tortas
    }

    return render(request,'core/listadocompra.html',datos)