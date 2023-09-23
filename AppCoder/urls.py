from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [

    path('',inicio,name='inicio'),
    #Peliculas#
    path('peliculas/', PeliculasList.as_view(),name='peliculas'),
    path('peliculas-formulario/', CrearPelicula.as_view(),name='peliculasFormulario'),
    path('peliculas-detalle/<slug:slug>',ReseñaPeliculaDetalle.as_view(),name='peliculas_detalle'),
    path('peliculas-generos-lista/<slug:slug>', PeliculasGenerosLista.as_view(),name='PeliculasGenerosLista'),
    path('editar-peliculas/<pk>', EditarPeliculas.as_view(),name='EditarPeliculas'),
    path('eliminar-peliculas/<pk>', EliminarPeliculas.as_view(),name='EliminarPeliculas'),
    #Series#
    path('series/', SeriesList.as_view(),name='series'),
    path('series-formulario/',CrearSerie.as_view(),name='seriesFormulario'),
    path('series-detalle/<slug:slug>',ReseñaSeriesDetalle.as_view(),name='series_detalle'),
    path('series-generos-lista/<slug:slug>', SeriesGenerosLista.as_view(),name='SeriesGenerosLista'),   
    path('editar-series/<pk>', EditarSeries.as_view(),name='EditarSeries'),
    path('eliminar-series/<pk>', EliminarSeries.as_view(),name='EliminarSeries'),
    #Directores#
    path('directores/', directores,name='directores'),
    path('directores-formulario/',CrearDirectores.as_view(),name='directoresFormulario'), 
    path('directores-detalle/<slug:slug>',DirectoresDetalle.as_view(),name='directores_detalle'),
    #Busqedas#
    path('busqueda/', busqueda,name='busqueda'),
    path('resultados/',resultados,name='resultados'),
    #log/in/out/registro#
    path('login/', loginView,name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('registro/', registroUsuario,name='registro'),
    #Usuarios#
    path('usuario/',usuario,name='usuario'),
    path('usuario-perfil/',EditarPerfilUsuario.as_view(),name='usuario_perfil'),
    path('usuarios-detalle/<pk>',UsuariosDetalle.as_view(),name='usuarios_detalle'),
    path('usuario-lista-reseñas-series/<pk>',UserListaReseñasSeries.as_view(),name='usuario_lista_reseñas_series'),
    path('usuario-lista-reseñas-peliculas/<pk>',UserListaReseñasPeliculas.as_view(),name='usuario_lista_reseñas_peliculas'),
    path('user-post-lista/', UserPostLista.as_view(),name='userPostLista'),
    path('usuario-actualizar-pass/',usuario_actualizar_pass,name='usuario_actualizar_pass'),
    
   
    
    
    
   
    
   
    
    

]