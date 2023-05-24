from django.shortcuts import render
from django.shortcuts import HttpResponse

def inicio(request):
    return HttpResponse("vista inicio")

def cursos(request):
    return HttpResponse("vista cursos")

def profesores(request):
    return HttpResponse("vista profesores")

def estudiantes(request):
    return HttpResponse("vista estudiantes")

def entregables(request):
    return HttpResponse("vista entregables")

def padre(request):
    return render(request, "app/padre.html")

def curso(request):
    return render(request, "app/curso.html")

def profesor(request):
    return render(request, "app/profesor.html")

def estudiante(request):
    return render(request, "app/estudiante.html")

def entregable(request):
    return render(request, "app/entregable.html")