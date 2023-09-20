from django import forms
from .models import *
from embed_video.fields import EmbedVideoFormField
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class PeliculasFormulario(forms.Form):

    titulo =forms.CharField(max_length=50,required=True)
    genero= forms.ModelMultipleChoiceField(queryset=Generos.objects.all(),required=True)
    año=forms.IntegerField(required=True)
    director =forms.ModelChoiceField(queryset=Directores.objects.all(),required=True)
    reseña = forms.CharField(widget=forms.Textarea)
    autor_reseña= forms.ModelChoiceField(queryset=User.objects.all(),required=True)
    cover = forms.ImageField(required=True)
    imagen = forms.ImageField(required=True)
    video_link =EmbedVideoFormField(required=False)
    
      
class SeriesFormulario(forms.Form):

    titulo =forms.CharField(max_length=50,required=True)
 
    genero= forms.ModelMultipleChoiceField(queryset=Generos.objects.all(),required=True)
    temporadas=forms.IntegerField(required=True)
    año=forms.IntegerField(required=True)
    reseña = forms.CharField(widget=forms.Textarea)
    autor_reseña= forms.ModelChoiceField(queryset=User.objects.all(),required=True)
    cover = forms.ImageField(required=True)
    imagen = forms.ImageField(required=True)
    video_link =EmbedVideoFormField(required=False)
    
 
class DirectoresFormulario(forms.Form):

    nombre =forms.CharField(max_length=50,required=True)
    apellido=forms.CharField(max_length=50,required=True)
    biografia= forms.CharField(widget=forms.Textarea) 
    citas=forms.CharField(max_length=300,required=True)
    imagen= forms.ImageField(required=True)


class RegistroUserForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)

    class meta:
        model=User 
        fields= ['username','password1','password2']
        help_texts= {k:"" for k in fields}