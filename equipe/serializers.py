from rest_framework import serializers
from .models import Integrantes

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrantes
        fields = ['Nome_integrante', 'Telefone']