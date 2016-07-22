from django.shortcuts import render
from gestion.models import alumno, materia
from rest_framework import viewsets
from .serializable import EstudianteSerializable, MateriaSerializable

class EstudiantesViewSet(viewsets.ModelViewSet):
	serializer_class = EstudianteSerializable
	queryset = alumno.objects.all()

class MateriaViewSet(viewsets.ModelViewSet):
	serializer_class = MateriaSerializable
	queryset = materia.objects.filter(cupo__gt=0,cupo__lte=30)
