from django.urls import path
from .views import Start

urlpatterns = [
    path('',Start, name="Start"),
]