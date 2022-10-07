from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Propietario
from .serializers import PropietarioSerializer

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

def index(request):
    return HttpResponse("Hello! This is the polls APP index.")
