from django.shortcuts import render,redirect
from .models import materia

# Create your views here.
def inicio_vista(request):
    materias=materia.objects.all
    return render(request,"gestionarmateria.html",{"mismaterias":materias})

def registrarmateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    guardarmateria=materia.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    # Guardame esta

    return redirect("/")

def seleccionarmateria(request,codigo):
    Materia=materia.objects.get(codigo=codigo)
    return render(request,"editarmateria.html",{"mismaterias":Materia})


def editarmateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]
    Materia=materia.objects.get(codigo=codigo)
    Materia.nombre=nombre
    Materia.creditos=creditos
    Materia.save()
    return redirect("/") #QUE ME LA GUARDES

def borrarmateria(request,codigo):
    Materia=materia.objects.get(codigo=codigo)
    Materia.delete() #Borrame esta
    return redirect("/")