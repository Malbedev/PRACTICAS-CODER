from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views import generic
from .forms import PeliculasFormulario


def inicio(request):
    peliculas= Peliculas.objects.all()
    directores = Directores.objects.all()
    curadores= Curadores.objects.all()
    generos = Generos.objects.all()
    destacada= Peliculas.objects.filter(destacada=True)
    
    context= {
         'peliculas' : peliculas,
         'directores': directores,
         'curadores': curadores,
         'generos':generos,
         'destacada':destacada,
    }
    return render(request,"AppCoder/inicio.html",context=context)



def peliculas(request):
    peliculas= Peliculas.objects.all()
    directores = Directores.objects.all()
    curadores= Curadores.objects.all()
    generos = Generos.objects.all()
    destacada= Peliculas.objects.filter(destacada=True)
    
    context= {
         'peliculas' : peliculas,
         'directores': directores,
         'curadores': curadores,
         'generos':generos,
         'destacada':destacada,
    }
    return render(request,"AppCoder/peliculas.html",context=context)

class ReseñaPeliculaDetalle(generic.DetailView):
     model = Peliculas
     template_name= 'AppCoder/peliculas_detalle.html'



def series(request):
     
    series= Series.objects.all()
    directores = Directores.objects.all()
    curadores= Curadores.objects.all()
    generos = Generos.objects.all()
    destacada= Series.objects.filter(destacada=True)
     
    context= {
         'series' : series,
         'directores': directores,
         'curadores': curadores,
         'generos':generos,
         'destacada':destacada,
         }
    return render(request,"AppCoder/series.html",context=context)

class ReseñaSeriesDetalle(generic.DetailView):
     model = Series
     template_name= 'AppCoder/series_detalle.html'



def directores(request):
     directores = Directores.objects.all()
     series= Series.objects.all()
     peliculas= Peliculas.objects.all()

     context= {
         'series' : series,
         'directores': directores,
         'peliculas' : peliculas,
         }
    
     return render(request,"AppCoder/directores.html",context=context)

class DirectoresDetalle(generic.DetailView):
     model = Directores
     template_name= 'AppCoder/directores_detalle.html'


def peliculas_formulario(request):
    miFormulario = PeliculasFormulario(request.POST,request.FILES)
    if request.method == 'POST': 
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            pelicula =Peliculas(titulo=data['titulo'], slug=data['slug'], año=data['año'], director=data['director'], reseña=data['reseña'], autor_reseña=data['autor_reseña'], cover =data['cover'], imagen =data['imagen'])
            pelicula.save()
            pelicula.genero.set(data['genero']) 
            return render(request,'AppCoder/usuario.html',{"mensaje":'Pelicula cargada con exito'})
        else:
            return render(request,'AppCoder/usuario.html',{"mensaje":'Formulario Invalido'})
    else:
        miFormulario = PeliculasFormulario()
        return render(request,'AppCoder/peliculas_formulario.html',{ 'miFormulario': miFormulario })


def busqueda_peliculas(request):
    

    return render(request,'busqueda_peliculas.html')






def usuario(request):
     return render(request,"AppCoder/usuario.html")