


# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from bluehaven.models import Bluehaven
from .serializers import BluehavenSerailizer


class BluehavenViewSet(viewsets.ModelViewSet):
    queryset=Bluehaven.objects.all()
    serializer_class=BluehavenSerailizer