from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views import generic


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

def usuario(request):
     return render(request,"AppCoder/usuario.html")