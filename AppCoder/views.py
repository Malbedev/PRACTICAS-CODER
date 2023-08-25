from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def inicio(request):
    return render(request,"AppCoder/inicio.html")

def usuario(request):
     return render(request,"AppCoder/usuario.html")

def peliculas(request):
    peliculas= Peliculas.objects.all()

    context= {
         'peliculas' : peliculas

    }
    return render(request,"AppCoder/peliculas.html",context=context)

def series(request):
     return render(request,"AppCoder/series.html")

def directores(request):
     return render(request,"AppCoder/directores.html")





