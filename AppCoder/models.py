from django.db import models


class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apeliido=models.CharField(max_length=50)
    email=models.EmailField()
    preferencias=models.CharField(max_length=50)

class Peliculas(models.Model):

    Titulo =models.CharField(max_length=50)
    Genero= models.CharField(max_length=50)
    año=models.IntegerField()
    duracion=models.CharField(max_length=10)

class Series(models.Model):

    Titulo =models.CharField(max_length=50)
    Genero= models.CharField(max_length=50)
    Temporadas= models.IntegerField()
    año=models.IntegerField()
    

class Directores(models.Model):
    nombre =models.CharField(max_length=50)
    apeliido=models.CharField(max_length=50)
    filmografia=models.CharField(max_length=50)
