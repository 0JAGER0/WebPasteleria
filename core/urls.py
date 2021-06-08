from django.urls import path
from .views import Start, nosotros , productos , contacto , registros , formularioContac , operaBlanca , merengueframbuesa, login , hojaRasca ,HojaldreManjar , Cassatta , BiscochoFrambuesa

urlpatterns = [
    path('',Start, name="Start"),
    path('form-nosotros',nosotros,name="nosotros"),

    path('form-productos/<id>',productos,name="productos"),

    path('contacto/',contacto,name="contacto"),
    path('registros/',registros,name="registros"),
    path('formularioContac/',formularioContac,name="formularioContac"),
    path('operaBlanca/',operaBlanca,name="operaBlanca"),
    path('merengue-frambuesa/',merengueframbuesa,name="merengue-frambuesa"),
    path('login/',login,name="login"),
    path('hojaRasca/',hojaRasca,name="hojaRasca"),
    path('Hojaldre-Manjar/',HojaldreManjar,name="Hojaldre-Manjar"),
    path('Cassatta/',Cassatta,name="Cassatta"),
    path('Biscocho-Frambuesa/',BiscochoFrambuesa,name="Biscocho-Frambuesa"),
    

]