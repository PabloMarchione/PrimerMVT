from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader


def elJom(request):
    template= loader.get_template("elJom.html")
    documento=template.render(template.__dict__)
    return HttpResponse(documento)

#pruebas
"""def jom(request):
    
    dision={"nombre":"pipo","apellido":"roke","edad":"25","listaN":[8,3,4]}
    
    template= loader.get_template("jom.html")
    documento=template.render(dision)
    return HttpResponse(documento)"""

"""
def padre(request):
    dicc={"nombre":"Silicato","apellido":"Volcanico","fecha_nacimiento":f"{datetime.datetime.date}","dni": "O4"}
    template= loader.get_template("padre.html")
    documento=template.render(dicc)
    return HttpResponse(documento)

def madre(request):
    dicc={"nombre":"Ossida","apellido":"Di silicatta","fecha_nacimiento":f"{datetime.datetime.date}","dni": "O2"}
    template= loader.get_template("madre.html")
    documento=template.render(dicc)
    return HttpResponse(documento)

def hijo(request):
    dicc={"nombre":"Vidrio","apellido":"Volcanico","fecha_nacimiento":f"{datetime.datetime.date}","dni":"0234"}
    template= loader.get_template("hijo.html")
    documento=template.render(dicc)
    return HttpResponse(documento)"""
    

