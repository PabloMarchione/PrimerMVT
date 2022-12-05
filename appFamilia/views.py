from django.shortcuts import render
import datetime
from .models import Familiar
from django.http import HttpResponse
from django.template import Template, Context, loader



def Padre(request):
    padre= Familiar(nombre="Silicato", apellido="Volcanico", fecha_nacimiento= "1000-11-30", dni= 321)
    padre.save()
    template= loader.get_template("padre.html")
    documento=template.render(padre.__dict__)
    return HttpResponse(documento)
    

def madre(request):
    madre= Familiar(nombre="Ossida", apellido="Di silicatta", fecha_nacimiento= "1201-01-15", dni= 831)
    madre.save()
    template= loader.get_template("madre.html")
    documento=template.render(madre.__dict__)
    return HttpResponse(documento)
    

def hijo(request):
    hijo= Familiar(nombre="Vidrio", apellido="Volcanico", fecha_nacimiento= "1500-08-05", dni= 1053)
    hijo.save()
    template= loader.get_template("hijo.html")
    documento=template.render(hijo.__dict__)
    return HttpResponse(documento)

#Prueba
#textoSave=f"Hola yo soy el Padre, me llamo {padre.nombre} {padre.apellido}, nací el {padre.fecha_nacimiento} y mi documento es {padre.dni}"
    #return HttpResponse (textoSave)
