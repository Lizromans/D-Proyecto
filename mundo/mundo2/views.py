from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return HttpResponse("<h1>prueba de formulario</h1>")

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def bienvenido(request):
    return render(request,'paginas/bienvenido.html')