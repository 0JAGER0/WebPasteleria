from django.shortcuts import render

# Create your views here.

def Start(request):
    return render(request,'core/Start.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def productos(request):
    return render(request,'core/productos.html')

def contacto(request):
    return render(request,'core/contacto.html')

def fomularioContac(request):
    return render(request,'core/fomularioContac.html')

def registro(request):
    return render(request,'core/REGISTRO.HTML')


def operaBlanca(request):
    return render(request,'core/operaBlanca.html')

def merengueframbuesa(request):
    return render(request,'core/merengue-frambuesa.html')

def login(request):
    return render(request,'core/LOGIN.HTML')

def hojaRasca(request):
    return render(request,'core/hojaRasca.html')

def HojaldreManjar(request):
    return render(request,'core/Hojaldre_Manjar.html')

def Cassatta(request):
    return render(request,'core/Cassatta.html')


def BiscochoFrambuesa(request):
    return render(request,'core/Biscocho-Frambuesa.html')