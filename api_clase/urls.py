from django.urls import path
from .views import apiTortas,torta
from .viewsLogin import loginApi

urlpatterns = [
    path('tortas/',apiTortas, name="tortas"),
    path('torta/<pk>',torta, name="torta"),
    path('loginApi/', loginApi, name="loginApi"),
]