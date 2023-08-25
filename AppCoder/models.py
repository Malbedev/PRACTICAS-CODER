from django.db import models



class Directores(models.Model):
    nombre =models.CharField(max_length=50)
    apeliido=models.CharField(max_length=50)
    filmografia=models.ManyToManyField('Peliculas',blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apeliido}'
    
class Curadores(models.Model):
    nombre =models.CharField(max_length=50)
    apeliido=models.CharField(max_length=50)
    reseñas=models.ManyToManyField('Peliculas',blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apeliido}'


class Peliculas(models.Model):

    titulo =models.CharField(max_length=50)
    slug = models.SlugField(unique=True,null=True)
    overview = models.TextField(null=True)
    genero= models.ManyToManyField('Generos')
    año=models.IntegerField()
    director = models.ForeignKey(Directores,on_delete=models.CASCADE,null=True)
    reseña = models.TextField(null=True)
    autor_reseña= models.ForeignKey(Curadores,on_delete=models.CASCADE,null=True)
    cover = models.ImageField(null=True)
    imagen = models.ImageField(null=True)

    def __str__(self):
        return self.titulo

class Series(models.Model):

    titulo =models.CharField(max_length=50)
    genero= models.CharField(max_length=50)
    temporadas= models.IntegerField()
    año=models.IntegerField()


    
class Generos(models.Model):
    genero=models.CharField(max_length=50)
    slug = models.SlugField(unique=False)

    def __str__(self):
        return self.genero


