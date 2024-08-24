from django.shortcuts import render, redirect
from .models import Propiedad
from django.shortcuts import render, get_object_or_404

def index(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'index.html', {'propiedades': propiedades})

def detalles(request, id):
    propiedad = get_object_or_404(Propiedad, id=id)  
    return render(request, 'detalles.html', {'propiedad': propiedad})

def propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'propiedades.html', {'propiedades': propiedades})