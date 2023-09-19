from django.urls import path
from  AppCoder import views
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [

    path('',inicio,name='inicio'),
    path('usuario/',usuario,name='usuario'),
    path('resultados/',resultados,name='resultados'),
    path('peliculas/', PeliculasList.as_view(),name='peliculas'),
    path('series/', SeriesList.as_view(),name='series'),
    path('directores/', directores,name='directores'),
    path('peliculas-detalle/<slug:slug>',ReseñaPeliculaDetalle.as_view(),name='peliculas_detalle'),
    path('series-detalle/<slug:slug>',ReseñaSeriesDetalle.as_view(),name='series_detalle'),
    path('directores-detalle/<slug:slug>',DirectoresDetalle.as_view(),name='directores_detalle'),
    path('peliculas-formulario/', CrearPelicula.as_view(),name='peliculasFormulario'),
    path('series-formulario/',CrearSerie.as_view(),name='seriesFormulario'),
    path('directores-formulario/',CrearDirectores.as_view(),name='directoresFormulario'),
    path('busqueda/', busqueda,name='busqueda'),
    path('generos-lista/<slug:slug>', GeneroListaVista.as_view(),name='generosLista'),
    path('login/', loginView,name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('registro/', registroUsuario,name='registro'),
    path('user-post-lista/', UserPostLista.as_view(),name='userPostLista'),
    path('eliminar-peliculas/<pk>', EliminarPeliculas.as_view(),name='EliminarPeliculas'),
    path('eliminar-series/<pk>', EliminarSeries.as_view(),name='EliminarSeries'),
    path('editar-peliculas/<pk>', EditarPeliculas.as_view(),name='EditarPeliculas'),
    path('editar-series/<pk>', EditarSeries.as_view(),name='EditarSeries'),
    path('usuarios-detalle/<pk>',UsuariosDetalle.as_view(),name='usuarios_detalle'),
    path('usuario-lista-reseñas/<pk>',UserListaReseñas.as_view(),name='usuario_lista_reseñas'),
    
    

]