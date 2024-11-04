from django.shortcuts import render
from .models import materia

# Create your views here.
def inicio_vista(request):
    materias=materia.objects.all
    return render(request,"gestionarmateria.html")