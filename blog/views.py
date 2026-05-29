from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    contexto = { 'nombre': 'Alex' }
    return render(request, 'blog/saludo.html', contexto)

def acerca(request):
    return render(request, 'blog/acerca.html')