from typing import Any, Dict
from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
from django.views.generic import *
from django.db.models.query import QuerySet
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user

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

class ReseñaPeliculaDetalle(LoginRequiredMixin,DetailView):
     model = Peliculas
     template_name= 'AppCoder/peliculas_detalle.html'
     
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['generos']=Generos.objects.all()
         return context
     
@login_required  
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

class ReseñaSeriesDetalle(LoginRequiredMixin,DetailView):
     model = Series
     template_name= 'AppCoder/series_detalle.html'

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['generos']=Generos.objects.all()
         return context
      
@login_required
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

class DirectoresDetalle(LoginRequiredMixin,DetailView):
     model = Directores
     template_name= 'AppCoder/directores_detalle.html'

@login_required
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
@login_required
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

##Genero##

class GeneroListaVista(LoginRequiredMixin,ListView):
     model = Generos
     template_name= 'AppCoder/genero_lista.html'
     context_object_name = 'generos'
     
     def get_context_data(self, **kwargs):
        query=self.request.path.replace('/generos-lista/','')
        context = super().get_context_data(**kwargs)
        context['peliculas']=Peliculas.objects.filter(genero__slug=query)
        context['series']=Series.objects.filter(genero__slug=query)
        context['generos']=Generos.objects.filter(genero__icontains=query)
        return context
     
    

##USUARIOS##

def loginView(request):

    if request.method =='POST':
        miFormulario= AuthenticationForm(request, data=request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario=data['username']
            password=data['password']

            user=authenticate(username=usuario,password=password)

            if user:
              login(request,user)
              return render(request,'AppCoder/inicio.html',{"mensaje":f'{usuario.capitalize()}'})
            else:
               return render(request,'AppCoder/login.html',{'miFormulario': miFormulario ,"mensaje":f'Datos Incorrectos'})
        else:
           
            return render(request,'AppCoder/login.html',{ 'miFormulario': miFormulario , "mensaje":'Formulario Invalido'})   
    else:
        miFormulario= AuthenticationForm()
        return render(request,'AppCoder/login.html',{ 'miFormulario': miFormulario })
        
def registroUsuario(request):
    if request.method =='POST':
        miFormulario= RegistroUserForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario=data['username']
            miFormulario.save()
            miFormulario= AuthenticationForm()
            return render(request,'AppCoder/login.html',{ 'miFormulario': miFormulario ,"mensaje":f'Bienvenidx {usuario.capitalize()} !!'})
            
        else:    
            return render(request,'AppCoder/registro.html',{ 'miFormulario': miFormulario ,"mensaje":'Formulario Invalido'})   
    else:
        miFormulario= RegistroUserForm()
        return render(request,'AppCoder/registro.html',{ 'miFormulario': miFormulario })



def usuario(request):
     return render(request,"AppCoder/usuario.html")


class UserPostLista(ListView):
    model= User
    template_name= 'AppCoder/user_post_lista.html'
    context_object_name = 'peliculas'
    context_object_name = 'series'


    def get_context_data(self, **kwargs):
        query= self.request.user.id
        context = super().get_context_data(**kwargs)
        context['peliculas']=Peliculas.objects.filter(autor_reseña_id=query)
        context['series']=Series.objects.filter(autor_reseña_id=query)
        return context
     
class UserPostEliminarPeliculas(DeleteView):
    model=Peliculas
    template_name='AppCoder/confirmacion_eliminar.html'
    success_url='/user-post-lista/'

class UserPostEliminarSeries(DeleteView):
    model=Series
    template_name='AppCoder/confirmacion_eliminar.html'
    success_url='/user-post-lista/'






def resultados(request):
     return render(request,"AppCoder/resultado.html")