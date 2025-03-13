from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('bienvenido', views.bienvenido, name='bienvenido'),
]