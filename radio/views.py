from django.shortcuts import render
from .models import Radio
from rest_framework import viewsets
from .serializers import RadioSerializer
class RadioViewSet(viewsets.ModelViewSet):
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer
    #def create(self, request, *args, **kwargs):