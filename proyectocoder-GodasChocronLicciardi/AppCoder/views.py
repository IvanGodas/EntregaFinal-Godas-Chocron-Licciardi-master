
from django.shortcuts import render

from AppCoder.forms import CursoForm, MedioForm , DelanteroForm
from .models import *
from django.http import HttpResponse

# Create your views here.
"""  """

def arquero(request):
    return render(request, "Appcoder/arquero.html")
    

def inicio(request):
    return render (request, "Appcoder/inicio.html")



def mediocampista(request):
    return render(request, "Appcoder/mediocampista.html")

def delantero(request):
    return render(request, "Appcoder/delantero.html")




def arqueroFormulario(request):

    if (request.method=="POST"):
        form= CursoForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            apellido= info["apellido"]
            edad = info["edad"]
            arquero= Arquero(nombre=nombre, apellido=apellido, edad=edad)
            arquero.save()
            return render (request, "Appcoder/inicio.html")
    else:
        form= CursoForm()
    return render(request, "Appcoder/arqueroFormulario.html", {"formulario":form})

def medioFormulario(request):
    
    if (request.method=="POST"):
        form= MedioForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            apellido= info["apellido"]
            edad = info["edad"]
            mediocampista= Mediocampista(nombre=nombre, apellido=apellido, edad=edad)
            mediocampista.save()
            return render (request, "Appcoder/inicio.html")
    else:
        form= MedioForm()
    return render(request, "Appcoder/medioFormulario.html", {"formulario":form})

def delanteroFormulario(request):
    
    if (request.method=="POST"):
        form=  DelanteroForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            apellido= info["apellido"]
            edad = info["edad"]
            mediocampista= Delantero(nombre=nombre, apellido=apellido, edad=edad)
            mediocampista.save()
            return render (request, "Appcoder/inicio.html")
    else:
        form= DelanteroForm()
    return render(request, "Appcoder/delanteroFormulario.html", {"formulario":form})


def busquedaFutbolista(request):
    
    return render(request, "Appcoder/busquedaFutbolista.html")


def buscar(request):
    if request.GET["futbolista"]:
        jugador= request.GET["futbolista"]
        arqueros= Arquero.objects.filter(nombre__icontains=jugador)
        return render(request, "Appcoder/resultadosBusqueda.html", {"arqueros":arqueros})
    else:
        return render(request, "Appcoder/busquedaFutbolista.html", {"error":"No se ingreso ningun futbolista"})

