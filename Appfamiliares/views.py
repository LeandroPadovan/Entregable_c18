from django.shortcuts import render
from .models import familiar
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template
from django.template import loader
# Create your views here.

def familiares(request):
    
    fliar1= familiar(nombre="Leandro", apellido="Padovan", dni=36707307, nacimiento="08/07/1992")
    fliar2= familiar(nombre="Jose", apellido="Padovan", dni=14281080, nacimiento="14/02/1961")
    fliar3= familiar(nombre="Joaquin", apellido="Padovan", dni=34100487, nacimiento="25/02/1989")
    fliar1.save()
    fliar2.save()
    fliar3.save()

    txt1= f"{fliar1.nombre} {fliar1.apellido} con DNI: {fliar1.dni} nacido el {fliar1.nacimiento} es un integrante de la familia.<br> <br> ------------------------------------------------------------------------------------"
    txt2= f"<br> <br>{fliar2.nombre} {fliar2.apellido} con DNI: {fliar2.dni} nacido el {fliar2.nacimiento} es un integrante de la familia.<br> <br> ------------------------------------------------------------------------------------"
    txt3= f"<br> <br>{fliar3.nombre} {fliar3.apellido} con DNI: {fliar3.dni} nacido el {fliar3.nacimiento} es un integrante de la familia.<br> <br> ------------------------------------------------------------------------------------"


    
    return HttpResponse(txt1+txt2+txt3)

def template1(request):
   
    diccionario = {"name": ["Leandro", "Jose","Joaquin"] , "apellido":["Padovan","Padovan","Padovan"], "dni": [36707307,14281080,34100487] , "nacimiento": ["08/07/1992" , "14/02/1961" , "25/02/1989"]}
 
    template=loader.get_template("familia.html")

    documento = template.render(diccionario)
    return HttpResponse(documento)