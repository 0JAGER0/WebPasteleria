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