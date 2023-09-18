from AppCoder.models import Generos

def generos_contexto(request):
    generos=Generos.objects.all()

    return {
        'generos':generos
    }