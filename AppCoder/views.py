from typing import Any, Dict
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views import generic
from .forms import *
from django.db.models import Q


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

##Peliculas##

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
     
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['generos']=Generos.objects.all()
         return context
     
     
def peliculas_formulario(request):
    miFormulario = PeliculasFormulario(request.POST,request.FILES)
    if request.method == 'POST': 
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            pelicula =Peliculas(titulo=data['titulo'], año=data['año'], director=data['director'], reseña=data['reseña'], autor_reseña=data['autor_reseña'], cover =data['cover'], imagen =data['imagen'],video_link=data['video_link'])
            pelicula.save()
            pelicula.genero.set(data['genero']) 
            return render(request,'AppCoder/resultados.html',{"mensaje":'Pelicula cargada con exito'})
        else:
            return render(request,'AppCoder/resultados.html',{"mensaje":'Formulario Invalido'})
    else:
        miFormulario = PeliculasFormulario()
        return render(request,'AppCoder/peliculas_formulario.html',{ 'miFormulario': miFormulario })
    


      ##SERIES## 

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

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['generos']=Generos.objects.all()
         return context
      

def series_formulario(request):
    miFormulario = SeriesFormulario(request.POST,request.FILES)
    if request.method == 'POST': 
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            serie =Series(titulo=data['titulo'],año=data['año'],temporadas=data['temporadas'], reseña=data['reseña'], autor_reseña=data['autor_reseña'], cover =data['cover'], imagen =data['imagen'],video_link=data['video_link'])
            serie.save()
            serie.genero.set(data['genero']) 
            return render(request,'AppCoder/resultados.html',{"mensaje":'Serie cargada con exito'})
        else:
            return render(request,'AppCoder/resultados.html',{"mensaje":'Formulario Invalido'})
    else:
        miFormulario = SeriesFormulario()
        return render(request,'AppCoder/series_formulario.html',{ 'miFormulario': miFormulario })



##DIRECTORES##

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

def directores_formulario(request):
    miFormulario = DirectoresFormulario(request.POST,request.FILES)
    if request.method == 'POST': 
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            director =Directores(nombre=data['nombre'],apellido=data['apellido'],biografia=data['biografia'],citas=data['citas'],imagen =data['imagen'])
            director.save()
            return render(request,'AppCoder/resultados.html',{"mensaje":'Director cargado con exito'})
        else:
            return render(request,'AppCoder/resultados.html',{"mensaje":'Formulario Invalido'})
    else:
        miFormulario = DirectoresFormulario()
        return render(request,'AppCoder/directores_formulario.html',{ 'miFormulario': miFormulario })

##BUSQUEDA##

def busqueda(request):
    if request.GET['titulo']:

        titulo = request.GET['titulo']
        pelicula=Peliculas.objects.filter(Q(titulo__icontains = titulo))
        serie=Series.objects.filter(Q(titulo__icontains = titulo))
        if pelicula:
            return render(request,'AppCoder/resultado_peliculas.html',{'pelicula':pelicula})
        elif serie:
            return render(request,'AppCoder/resultado_series.html',{'serie':serie})
        else: 
            return render(request,'AppCoder/resultados.html',{"mensaje":'Lo sentimos :( no hubo coincidencias!'})
    else:
        return render(request,'AppCoder/resultados.html',{"mensaje":'Busqueda Invalida'})

##USUARIOS##

def usuario(request):
     return render(request,"AppCoder/usuario.html")

def resultados(request):
     return render(request,"AppCoder/resultado.html")