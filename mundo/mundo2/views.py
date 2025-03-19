from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def bienvenido(request):
    return render(request,'paginas/bienvenido.html')


def registro(request):
    return render(request, 'paginas/registro.html')