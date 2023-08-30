from django import forms
from .models import *

class PeliculasFormulario(forms.Form):

    titulo =forms.CharField(max_length=50,required=True)
    slug = forms.SlugField(required=True)
    genero= forms.ModelMultipleChoiceField(queryset=Generos.objects.all(),required=True)
    año=forms.IntegerField(required=True)
    director =forms.ModelChoiceField(queryset=Directores.objects.all(),required=True)
    reseña = forms.CharField(widget=forms.Textarea)
    autor_reseña= forms.ModelChoiceField(queryset=Curadores.objects.all(),required=True)
    cover = forms.ImageField(required=True)
    imagen = forms.ImageField(required=True)
  
