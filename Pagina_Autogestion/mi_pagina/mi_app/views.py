from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Nota, User


# Create your views here.
def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def cursos(request):
    # Lógica para determinar si mostrar la ventana modal
    mostrar_modal = True  # Aquí puedes cambiar la lógica según tus necesidades

    context = {
        'mostrar_modal': mostrar_modal
    }
    return render(request, 'cursos.html', context)

def contenido(request):
    return render(request, 'contenido.html')

def noticias(request):
    return render(request, 'noticias.html')

def notas(request):
    return render(request, 'notas.html')

def procesar_formulario(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        # Aquí puedes trabajar con el texto como lo necesites
        context = {
            'textoIngresado' : texto
        }
        Nota.objects.create(contenido=texto, color='#FFAACC', user_id='1')
        return render(request, 'notas.html', context)
    else:
        return HttpResponse('Error: método no permitido')