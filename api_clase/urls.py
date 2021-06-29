from django.urls import path
from .views import apiTortas,torta
from .viewsLogin import login

urlpatterns = [
    path('tortas/',apiTortas, name="tortas"),
    path('torta/<pk>',torta, name="torta"),
    path('login/', login, name="login"),
]