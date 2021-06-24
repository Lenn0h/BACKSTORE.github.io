from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

#Creacion de clases

class Empresa(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    empresa = models.ForeignKey(Empresa,on_delete=CASCADE) 

    def __str__(self):
        return self.nombre