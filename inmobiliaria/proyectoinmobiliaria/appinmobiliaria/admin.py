from django.contrib import admin
from .models import Propiedad

# Register your models here.
@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('id', 'ubicacion', 'imagen', 'precio', 'tamanio', 'descripcion') 
    search_fields = ('ubicacion',)      