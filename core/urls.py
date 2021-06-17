from django.urls import path
from .views import Start, deletorta,agregarTorta, mantenedor, nosotros , productos , contacto , registros , formularioContac , operaBlanca , merengueframbuesa, login , hojaRasca ,HojaldreManjar , Cassatta , BiscochoFrambuesa,listadocompra,mantenedormod,deletortaLista,loginadmin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',Start, name="Start"),
    path('nosotros/',nosotros,name="nosotros"),
    path('productos/',productos,name="productos"),
    path('contacto/',contacto,name="contacto"),
    path('registros/',registros,name="registros"),
    path('login/',LoginView.as_view(template_name='core/login.html'),name="login"),
    path('logout/',LogoutView.as_view(template_name='core/logout.html'),name="logout"),
    path('formularioContac/',formularioContac,name="formularioContac"),
    path('operaBlanca/',operaBlanca,name="operaBlanca"),
    path('merengue-frambuesa/',merengueframbuesa,name="merengue-frambuesa"),
    path('hojaRasca/',hojaRasca,name="hojaRasca"),
    path('Hojaldre-Manjar/',HojaldreManjar,name="Hojaldre-Manjar"),
    path('Cassatta/',Cassatta,name="Cassatta"),
    path('Biscocho-Frambuesa/',BiscochoFrambuesa,name="Biscocho-Frambuesa"),
    path('listadocompra/',listadocompra,name="listadocompra"),
    path('mantenedor/',mantenedor,name="mantenedor"),
    path('mantenedormod/<pk>',mantenedormod,name="mantenedormod"),
    path('agregartorta/',agregarTorta,name="agregartorta"),
    path('deletorta/<pk>/',deletorta,name="deletorta"),
    path('deletortaLista/<pk>',deletortaLista,name="deletortaLista"),
    path('loginadmin/',LoginView.as_view(template_name='core/loginadmin.html'),name="loginadmin")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




