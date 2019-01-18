from django.shortcuts import render
from services.models import Meme
from services.serializers import MemeSerializer
from rest_framework import generics
# Create your views here.

class MemeListCreate(generics.ListCreateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
