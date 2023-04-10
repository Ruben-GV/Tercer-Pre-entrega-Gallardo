from django.urls import path
from .views import *
from AppCoder import views


urlpatterns = [
    
    path("", inicioApp, name="inicioApp"),
    #path("crear_curso/", crear_curso),
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables"),
    #path('busquedaCurso', views.busquedaCurso, name="BusquedaCurso"),
    path('buscar/', views.buscar),
    
]