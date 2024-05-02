from django.db import models

# Create your models here.

class User(models.Model):
    nombreApellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    telefono = models.CharField(max_length=25)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario
    
class Nota(models.Model):
    contenido = models.CharField(max_length=255)
    color =  models.CharField(max_length=15) #Ej: #FFAACC o #F0F8FF
    user = models.ForeignKey(User, on_delete=models.CASCADE)
