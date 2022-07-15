from django.db import models

# Create your models here.

class Arquero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()


    def __str__(self):
        return self.nombre+" "+self.apellido
 

class Mediocampista(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()

    def __str__(self):
        return self.nombre+" "+self.apellido

class Delantero(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()

    def __str__(self):
        return self.nombre+" "+self.apellido
