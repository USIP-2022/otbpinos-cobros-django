from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Propietario
from .serializers import PropietarioSerializer



def index(request):
    return HttpResponse("Hello! This is the polls APP index.")

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
class PropietarioCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

@api_view(["GET"])
def propietario_contador(request):
    """
    Cantidad de items en el modelo propietario
    """

    try:
        cantidad = Propietario.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

