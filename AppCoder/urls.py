from django.urls import path
from  AppCoder import views
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [

    path('',inicio,name='inicio'),
    path('usuario/',usuario,name='usuario'),
    path('resultados/',resultados,name='resultados'),
    path('peliculas/', peliculas,name='peliculas'),
    path('series/', series,name='series'),
    path('directores/', directores,name='directores'),
    path('peliculas-detalle/<slug:slug>',ReseñaPeliculaDetalle.as_view(),name='peliculas_detalle'),
    path('series-detalle/<slug:slug>',ReseñaSeriesDetalle.as_view(),name='series_detalle'),
    path('directores-detalle/<slug:slug>',DirectoresDetalle.as_view(),name='directores_detalle'),
    path('peliculas-formulario/', peliculas_formulario,name='peliculasFormulario'),
    path('series-formulario/',series_formulario,name='seriesFormulario'),
    path('directores-formulario/',directores_formulario,name='directoresFormulario'),
    path('busqueda/', busqueda,name='busqueda'),
    path('generos-lista/<slug:slug>', GeneroListaVista.as_view(),name='generosLista'),
    path('login/', loginView,name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('registro/', registroUsuario,name='registro'),
    path('user-post-lista/', UserPostLista.as_view(),name='userPostLista'),
    path('user-post-eliminar-peliculas/<pk>', UserPostEliminarPeliculas.as_view(),name='userPostEliminarPeliculas'),
     path('user-post-eliminar-series/<pk>', UserPostEliminarSeries.as_view(),name='userPostEliminarSeries'),
    

]