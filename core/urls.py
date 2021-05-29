from django.urls import path
from .views import Start, nosotros , productos , contacto , registro , fomularioContac , operaBlanca , merengueframbuesa, login , hojaRasca ,HojaldreManjar , Cassatta , BiscochoFrambuesa

urlpatterns = [
    path('',Start, name="Start"),
    path('',nosotros,name="nosotros"),
    path('',productos,name="productos"),
    path('',contacto,name="contacto"),
    path('',registro,name="registro"),
    path('',fomularioContac,name="formularioContac"),
    path('',operaBlanca,name="operaBlanca"),
    path('',merengueframbuesa,name="merengue-frambuesa"),
    path('',login,name="login"),
    path('',hojaRasca,name="hojaRasca"),
    path('',HojaldreManjar,name="Hojaldre-Manjar"),
    path('',Cassatta,name="Cassatta"),
    path('',BiscochoFrambuesa,name="Biscocho-Frambuesa")
]