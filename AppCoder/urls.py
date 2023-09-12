from django.urls import path
from  AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('',views.inicio,name='inicio'),
    path('usuario/',views.usuario,name='usuario'),
    path('resultados/',views.resultados,name='resultados'),
    path('peliculas/', views.peliculas,name='peliculas'),
    path('series/', views.series,name='series'),
    path('directores/', views.directores,name='directores'),
    path('peliculas-detalle/<slug:slug>',views.ReseñaPeliculaDetalle.as_view(),name='peliculas_detalle'),
    path('series-detalle/<slug:slug>',views.ReseñaSeriesDetalle.as_view(),name='series_detalle'),
    path('directores-detalle/<slug:slug>',views.DirectoresDetalle.as_view(),name='directores_detalle'),
    path('peliculas-formulario/', views.peliculas_formulario,name='peliculasFormulario'),
    path('series-formulario/', views.series_formulario,name='seriesFormulario'),
    path('directores-formulario/', views.directores_formulario,name='directoresFormulario'),
    path('busqueda/', views.busqueda,name='busqueda'),
    path('generos-lista/<slug:slug>', views.GeneroListaVista.as_view(),name='generosLista'),
    path('login/', views.loginView,name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('registro/', views.registroUsuario,name='registro'),
    path('user-post-lista/', views.UserPostLista.as_view(),name='userPostLista'),
    

]