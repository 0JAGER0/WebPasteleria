from django.urls import path
from .views import Start, nosotros , productos , contacto , registros , fomularioContac , operaBlanca , merengueframbuesa, login , hojaRasca ,HojaldreManjar , Cassatta , BiscochoFrambuesa

urlpatterns = [
    path('',Start, name="Start"),
    path('form-nosotros',nosotros,name="nosotros"),
    path('form-productos/<id>',productos,name="productos"),
    path('contacto/',contacto,name="contacto"),
    path('registros/',registros,name="registros"),
    path('formularioContac/',fomularioContac,name="formularioContac"),
    path('',operaBlanca,name="operaBlanca"),
    path('',merengueframbuesa,name="merengue-frambuesa"),
    path('',login,name="login"),
    path('',hojaRasca,name="hojaRasca"),
    path('',HojaldreManjar,name="Hojaldre-Manjar"),
    path('',Cassatta,name="Cassatta"),
    path('',BiscochoFrambuesa,name="Biscocho-Frambuesa"),
    

]