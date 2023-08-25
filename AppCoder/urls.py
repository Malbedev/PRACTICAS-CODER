from django.urls import path
from  AppCoder import views

urlpatterns = [

    path('',views.inicio,name='inicio'),
    path('usuario/',views.usuario,name='usuario'),
    path('peliculas/', views.peliculas,name='peliculas'),
    path('series/', views.series,name='series'),
    path('directores/', views.directores,name='directores'),
    path('peliculas_detail/<int:pk>',views.ReseñaDetalle.as_view(),name='peliculas_detail'),
    
]
