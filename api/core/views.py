from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArretSerializers
from .models import Arret
# Create your views here.

class ArretViewSet(viewsets.ModelViewSet):
    serializer_class = ArretSerializers
    queryset = Arret.objects.all()