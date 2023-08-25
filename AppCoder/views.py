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

def usuario(request):
     return render(request,"AppCoder/usuario.html")

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

def series(request):
     return render(request,"AppCoder/series.html")

def directores(request):
     return render(request,"AppCoder/directores.html")



class ReseñaDetalle(generic.DetailView):
     model = Peliculas


