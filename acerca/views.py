from django.http import HttpResponse

def acerca(request):
    return HttpResponse("Acerca de Python - Django")