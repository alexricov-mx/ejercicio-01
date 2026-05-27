from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mundo - Django")

def acerca(request):
    return HttpResponse("(BLOG) Acerca de - Django")