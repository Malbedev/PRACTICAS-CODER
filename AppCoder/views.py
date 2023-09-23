
from django.views.generic import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .forms import *
from .models import *


def inicio(request):
    peliculas= Peliculas.objects.all()
    directores = Directores.objects.all()
    curadores= Curadores.objects.all()
    destacada= Peliculas.objects.filter(destacada=True)
    
    context= {
         'peliculas' : peliculas,
         'directores': directores,
         'curadores': curadores,
         'destacada':destacada,
    }
    return render(request,"AppCoder/inicio.html",context=context)

##Peliculas##

def peliculas(request):
    peliculas= Peliculas.objects.all()
    directores = Directores.objects.all()
    curadores= Curadores.objects.all()
    destacada= Peliculas.objects.filter(destacada=True)
    
    context= {
         'peliculas' : peliculas,
         'directores': directores,
         'curadores': curadores,
         'destacada':destacada,
    }
    return render(request,"AppCoder/peliculas.html",context=context)


class ReseñaPeliculaDetalle(LoginRequiredMixin,DetailView):
     model = Peliculas
     template_name= 'AppCoder/peliculas_detalle.html'
     
   
class PeliculasList(ListView):
    model = Peliculas
    template_name = 'AppCoder/peliculas.html'
    context_object_name ='peliculas'
    paginate_by = 2 


class CrearPelicula(LoginRequiredMixin,CreateView):
    model=Peliculas
    template_name='AppCoder/peliculas_formulario.html'
    fields=['titulo','genero','año','director','reseña','cover','imagen','video_link']
    success_url='/user-post-lista/'

    
    def form_valid(self, form):
        form.instance.autor_reseña = self.request.user
        return super().form_valid(form)


class EliminarPeliculas(DeleteView):
    model=Peliculas
    success_url='/user-post-lista/'

class EditarPeliculas(LoginRequiredMixin,UpdateView):
    model=Peliculas
    template_name='AppCoder/peliculas_actualizar.html'
    fields=['titulo','genero','año','director','reseña','cover','imagen','video_link']
    success_url='/user-post-lista/'

  
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


class SeriesList(ListView):
    model = Series
    template_name = 'AppCoder/series.html'
    context_object_name ='series'
    paginate_by = 4 


class CrearSerie(LoginRequiredMixin,CreateView):
    model=Series
    template_name='AppCoder/series_formulario.html'
    fields=['titulo','genero','año','temporadas','reseña','cover','imagen','video_link']
    success_url='/user-post-lista/'    


    def form_valid(self, form):
        form.instance.autor_reseña = self.request.user
        return super().form_valid(form)
    

class EliminarSeries(DeleteView):
    model=Series
    success_url='/user-post-lista/'

class EditarSeries(LoginRequiredMixin,UpdateView):
    model=Series
    template_name='AppCoder/series_actualizar.html'
    fields=['titulo','genero','año','temporadas','reseña','cover','imagen','video_link']
    success_url='/user-post-lista/'
     

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

     def get_context_data(self, **kwargs):
        query=self.request.path.replace('/directores-detalle/','')
        context = super().get_context_data(**kwargs)
        context['peliculas']=Peliculas.objects.filter(director__slug=query)
        return context
         
    
class CrearDirectores(LoginRequiredMixin,CreateView):
    model=Directores
    template_name='AppCoder/directores_formulario.html'
    fields=['nombre','apellido','biografia','citas','imagen']
    success_url='/user-post-lista/'   

  
##BUSQUEDA##
@login_required
def busqueda(request):
    generos = Generos.objects.all()
    if request.GET['titulo']:

        titulo = request.GET['titulo']
        pelicula=Peliculas.objects.filter(Q(titulo__icontains = titulo))
        serie=Series.objects.filter(Q(titulo__icontains = titulo))
        if pelicula:
            return render(request,'AppCoder/resultado_peliculas.html',{'pelicula':pelicula,'generos':generos})
        elif serie:
            return render(request,'AppCoder/resultado_series.html',{'serie':serie,'generos':generos})
        else: 
            return render(request,'AppCoder/resultados.html',{"mensaje":'Lo sentimos :( no hubo coincidencias!','generos':generos})
    else:
        return render(request,'AppCoder/resultados.html',{"mensaje":'Busqueda Invalida','generos':generos})

def resultados(request):
     return render(request,"AppCoder/resultado.html")

##Genero##

class SeriesGenerosLista(LoginRequiredMixin,ListView):
     model = Generos
     template_name= 'AppCoder/series_generos_lista.html'
     context_object_name='series'
     paginate_by=2
     
      
     def get_queryset(self):
       query=self.request.path.replace('/series-generos-lista/','')
       series_list = Series.objects.filter(genero__slug=query)
       return series_list
     
     def get_context_data(self, **kwargs):
        query=self.request.path.replace('/series-generos-lista/','')
        context = super().get_context_data(**kwargs)
        context['generos']=Generos.objects.filter(genero__icontains=query)
        return context
    
class PeliculasGenerosLista(LoginRequiredMixin,ListView):
     model =Peliculas
     template_name= 'AppCoder/peliculas_generos_lista.html'
     context_object_name='peliculas'
     paginate_by=2
     
      
     def get_queryset(self):
       query=self.request.path.replace('/peliculas-generos-lista/','')
       series_list = Peliculas.objects.filter(genero__slug=query)
       return series_list
     
     def get_context_data(self, **kwargs):
        query=self.request.path.replace('/peliculas-generos-lista/','')
        context = super().get_context_data(**kwargs)
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

def usuario_actualizar_pass(request):

    usuario=request.user

    miFormulario= ActualizarUserForm(request.POST, instance=request.user)

    if request.method =='POST':

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario.username=data['username']
            usuario.email=data['email']
            usuario.set_password(data['password1'])
            usuario.save()
            miFormulario= AuthenticationForm()
            return render(request,'AppCoder/login.html',{'miFormulario': miFormulario,"mensaje":f' Datos Actualizados correctamente!! Vuelva a logearse con su contraseña nueva.'})
            
        else:    
            return render(request,'AppCoder/usuario_actualizar_pass.html',{ 'miFormulario': miFormulario ,"mensaje":'Formulario Invalido'})   
    else:
        miFormulario= ActualizarUserForm(instance=request.user)
        return render(request,'AppCoder/usuario_actualizar_pass.html',{ 'miFormulario': miFormulario })

class UsuariosDetalle(LoginRequiredMixin,DetailView):
    model=User
    template_name= 'AppCoder/usuarios_detalle.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        query=self.request.path.replace('/usuarios-detalle/','')
        context = super().get_context_data(**kwargs)
        context['user']=User.objects.filter(id=query)
        return context
    
@login_required
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
     
class UserListaReseñasSeries(ListView):
    model= User
    template_name= 'AppCoder/usuario_lista_reseñas_series.html'
    context_object_name='series'
    paginate_by=2
   
    def get_queryset(self):
       query=self.request.path.replace('/usuario-lista-reseñas-series/','')
       series_list = Series.objects.filter(autor_reseña_id=query)
       return series_list
    
class UserListaReseñasPeliculas(ListView):
    model= User
    template_name= 'AppCoder/usuario_lista_reseñas_peliculas.html'
    context_object_name='peliculas'
    paginate_by=2
   
    def get_queryset(self):
       query=self.request.path.replace('/usuario-lista-reseñas-peliculas/','')
       series_list = Peliculas.objects.filter(autor_reseña_id=query)
       return series_list
    

class EditarPerfilUsuario(UpdateView):
    model:Perfil
    template_name='AppCoder/perfil_usuario_form.html'
    fields=['avatar','imagen','bio', 'fecha_nac','ciudad','pais','web','redes']
    success_url='/usuario/'

    def get_object(self):
        profile,created=Perfil.objects.get_or_create(user=self.request.user)
        return profile

