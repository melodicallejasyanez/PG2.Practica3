from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from consultas.models import Diagnostico, Intervencion, Apoyo, Sintomas
from consultas.serializers import (
    consultasSerializer,
    IntervencionSerializer,
    ApoyoSerializer,
    SintomasSerializer,
)

class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = consultasSerializer

class IntervencionViewSet(viewsets.ModelViewSet):
    queryset = Intervencion.objects.all()
    serializer_class = IntervencionSerializer

class ApoyoViewSet(viewsets.ModelViewSet):
    queryset = Apoyo.objects.all()
    serializer_class = ApoyoSerializer

class SintomasViewSet(viewsets.ModelViewSet):
    queryset = Sintomas.objects.all()
    serializer_class = SintomasSerializer