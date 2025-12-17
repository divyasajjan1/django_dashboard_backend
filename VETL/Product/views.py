from django.shortcuts import render
from .models import TeamDC, TeamMarvel
from .serializers import TeamDCSerializer, TeamMarvelSerializer
from rest_framework import viewsets

# Create your views here.
class TeamDCViewset(viewsets.ModelViewSet):
    queryset = TeamDC.objects.all()
    serializer_class = TeamDCSerializer

class TeamMarvelViewset(viewsets.ModelViewSet):
    queryset = TeamMarvel.objects.all()
    serializer_class = TeamMarvelSerializer