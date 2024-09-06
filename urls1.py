from django.urls import path
from . import views

urlpatterns = [
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('entradas/<int:autor_id>/', views.entradas_por_autor, name='entradas_por_autor'),
]