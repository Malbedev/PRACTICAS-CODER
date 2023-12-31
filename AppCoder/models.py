from django.db import models
from django.template.defaultfilters import slugify
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from datetime import date


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
    
    def save(self, *args, **kwargs):
        self.slug = self.nombre.lower() + '-' + self.apellido.lower()
        super(Directores, self).save(*args, **kwargs)
    
    
class Generos(models.Model):
    genero=models.CharField(max_length=50)
    slug = models.SlugField(unique=True,null=True)

    def __str__(self):
        return self.genero
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.genero)
        super(Generos, self).save(*args, **kwargs)


class Peliculas(models.Model):

    titulo =models.CharField(max_length=50)
    slug = models.SlugField(unique=True,null=True)
    fecha_creacion=models.DateField(auto_now_add=True)
    genero= models.ManyToManyField(Generos)
    año=models.IntegerField(blank=True,null=True)
    director = models.ForeignKey(Directores,on_delete=models.CASCADE,null=True)
    reseña = models.TextField(null=True)
    autor_reseña= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    cover = models.ImageField(null=True)
    imagen = models.ImageField(null=True )
    video_link = EmbedVideoField(blank=True,null=True)
    destacada= models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo) +'-'+ str(self.autor_reseña)
        super(Peliculas, self).save(*args, **kwargs)
    

class Series(models.Model):

    titulo =models.CharField(max_length=50)
    slug = models.SlugField(unique=True,null=True)
    fecha_creacion=models.DateField(auto_now_add=True)
    genero= models.ManyToManyField(Generos)
    año=models.IntegerField(null=True)
    temporadas= models.IntegerField(null=True)
    reseña = models.TextField(null=True)
    autor_reseña= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    cover = models.ImageField(null=True)
    imagen = models.ImageField(null=True)
    video_link = EmbedVideoField(blank=True,null=True)
    destacada= models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)+'-'+ str(self.autor_reseña)
        super(Series, self).save(*args, **kwargs)
  

class Perfil(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.ImageField(null=True,blank=True)
    imagen=models.ImageField(null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    fecha_nac = models.DateField(null=True,blank=True,verbose_name='Fecha de nacimiento')
    ciudad=models.CharField(max_length=200,null=True,blank=True)
    pais=models.CharField(max_length=200,null=True,blank=True)
    web=models.URLField(max_length=200,null=True,blank=True)
    redes=models.URLField(max_length=200,null=True,blank=True)



    def calcular_años(self):
        edad=date.today().year - self.fecha_nac.year
        return edad
    

class Comentarios(models.Model):
    contenido= models.TextField(max_length=1000,help_text='Ingrese un comentario')
    autor= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fecha_comentario=models.DateTimeField(auto_now_add=True)
    peliculas=models.ForeignKey(Peliculas,on_delete=models.CASCADE,blank=True,null=True)
    series=models.ForeignKey(Series,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        ordering= ['-fecha_comentario']

