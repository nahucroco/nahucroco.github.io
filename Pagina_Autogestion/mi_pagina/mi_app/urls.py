from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='perfil'),
    path('notas/', views.notas, name='notas'),
    path('cursos/', views.cursos, name='cursos'),
    path('contenido/', views.contenido, name='contenido'),
    path('noticias/', views.noticias, name='noticias'),
    path('procesar/', views.procesar_formulario, name='procesar_formulario'),
]