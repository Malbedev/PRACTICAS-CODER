from django.urls import path
from  AppCoder import views

urlpatterns = [

    path('',views.inicio,name='inicio'),
    path('usuario/',views.usuario,name='usuario'),
    path('peliculas/', views.peliculas,name='peliculas'),
    path('series/', views.series,name='series'),
    path('directores/', views.directores,name='directores'),
    path('peliculas-detalle/<slug:slug>',views.ReseñaPeliculaDetalle.as_view(),name='peliculas_detalle'),
    path('series-detalle/<slug:slug>',views.ReseñaSeriesDetalle.as_view(),name='series_detalle'),
    path('directores-detalle/<slug:slug>',views.DirectoresDetalle.as_view(),name='directores_detalle'),
    path('peliculas-formulario/', views.peliculas_formulario,name='peliculasFormulario'),
    path('series-formulario/', views.series_formulario,name='seriesFormulario'),
    path('directores-formulario/', views.directores_formulario,name='directoresFormulario'),
    path('busqueda-peliculas/', views.busqueda_pelicula,name='busquedaPeliculas'),
    path('busqueda-series/', views.busqueda_serie,name='busquedaSeries'),

]