from django.urls import path
from .views import Start, nosotros , productos

urlpatterns = [
    path('',Start, name="Start"),
    path('',nosotros,name="nosotros"),
    path('',productos,name="productos")
]