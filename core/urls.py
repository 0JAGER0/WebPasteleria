from django.urls import path
from .views import Start, fomularioContac, nosotros , productos , contacto

urlpatterns = [
    path('',Start, name="Start"),
    path('',nosotros,name="nosotros"),
    path('',productos,name="productos"),
    path('',contacto,name="contacto"),
    path('',fomularioContac, name="fomularioContac")
]