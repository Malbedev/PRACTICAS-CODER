from django.db import models
from django.template.defaultfilters import slugify

class Generos(models.Model):
    genero=models.CharField(max_length=50)
    slug = models.SlugField(unique=False)

    def __str__(self):
        return self.genero

class Curadores(models.Model):
    nombre =models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    reseñas=models.ManyToManyField('Peliculas',blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Directores(models.Model):
    nombre =models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    slug = models.SlugField(unique=True,null=True)
    biografia= models.TextField(blank=True,null=True)
    imagen= models.ImageField(null=True)
    filmografia=models.ManyToManyField('Peliculas',blank=True)
    citas=models.CharField(max_length=300,null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    



class Peliculas(models.Model):

    titulo =models.CharField(max_length=50,null=True)
    slug = models.SlugField(null=True)
    overview = models.TextField(null=True)
    genero= models.ManyToManyField(Generos)
    año=models.IntegerField(blank=True,null=True)
    director = models.ForeignKey(Directores,on_delete=models.CASCADE,null=True)
    reseña = models.TextField(null=True)
    autor_reseña= models.ForeignKey(Curadores,on_delete=models.CASCADE,null=True)
    cover = models.ImageField(null=True)
    imagen = models.ImageField(null=True)
    destacada= models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
    

class Series(models.Model):

    titulo =models.CharField(max_length=50)
    slug = models.SlugField(unique=False,null=True)
    overview = models.TextField(null=True)
    genero= models.ManyToManyField(Generos)
    año=models.IntegerField()
    temporadas= models.IntegerField()
    reseña = models.TextField(null=True)
    autor_reseña= models.ForeignKey(Curadores,on_delete=models.CASCADE,null=True)
    cover = models.ImageField(null=True)
    imagen = models.ImageField(null=True)
    destacada= models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
    
    


