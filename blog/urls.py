from django.urls import path
from .views import saludo, acerca

urlpatterns = [
    path("", saludo, name="saludo"),
    path("acerca/", acerca, name="acerca"),
]