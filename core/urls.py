from django.urls import path
from .views import Start, nosotros , productos , contacto , registro

urlpatterns = [
    path('',Start, name="Start"),
    path('',nosotros,name="nosotros"),
    path('',productos,name="productos"),
    path('',contacto,name="contacto"),
    path('',registro,name="registro")
]