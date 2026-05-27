from django.urls import path
from .views import acerca

urlpatterns = [
    path("acerca/", acerca, name="acerca"),
]