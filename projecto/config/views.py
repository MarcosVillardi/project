from django.http import HttpResponse
from django.template import Context,Template
from django.shortcuts import render
from datetime import datetime
def saludar (request):
    return HttpResponse("<h1>Hola Mundo<h1>")

def nombre(request, nombre: str, apellido: str):
    nombre = nombre. capitalize()
    apellido = apellido.upper()
    return HttpResponse(f"tu nombre completo es: {nombre},{apellido}")
def template_test(request):
    mi_html = open("./templates/template1.html", encoding="utf-8")
    mi_template = Template (mi_html.read())
    mi_html.close()
    nombre = "juan"
    apellido = "perez"
    datos = {"nombre": nombre.capitalize(), "apellido": apellido.capitalize()}
    mi_contexto = Context(datos)
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)

def template_test2(request):
    nombre = "luis"
    nombre = nombre.capitalize()
    apellido = "gonzales"
    apellido = apellido.capitalize()
    dt = datetime.now()
    hora = dt.strftime("%H:%M:%S")
    fecha = dt.strftime("%d/%m/%Y")
    datos = {"nombre": nombre, "apellido": apellido, "fecha": fecha, "hora": hora}
    return render(request, "template1.html", context = datos)

def template_test3(request):
    notas = [5,7,9,3,1,2,4,6,8]
    contexto = {"notas": notas}
    notas.sort(reverse=True)
    return render(request, "template2.html", contexto)
