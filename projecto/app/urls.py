from django.urls import path
from . import views 

app_name = 'app'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('profesores/', views.profesores, name='profesores'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('entregables/', views.entregables, name='entregables'),
    path('padre/', views.padre, name='padre'),
    path('curso/', views.curso, name='curso'),
    path('profesor/', views.profesor, name='profesor'),
    path('estudiante/', views.estudiante, name='estudiante'),
    path('entregable/', views.entregable, name='entregable'),
]