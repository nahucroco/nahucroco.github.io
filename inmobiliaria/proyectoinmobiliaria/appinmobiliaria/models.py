from django.db import models

class Propiedad(models.Model):
    id = models.IntegerField(primary_key=True)
    ubicacion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')
    precio = models.CharField(max_length=100)
    tamanio = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.ubicacion