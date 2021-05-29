from django.urls import path
from .views import Start, nosotros

urlpatterns = [
    path('',Start, name="Start"),
    path('',nosotros,name="nosotros")
]