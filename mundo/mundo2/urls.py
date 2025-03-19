from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('bienvenido', views.bienvenido, name='bienvenido'),
    path('registro', views.registro, name='registro'),
]