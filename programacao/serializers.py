from rest_framework import serializers
from .models import Programacao
class ProgramacaoSerializer(serializers.ModelSerializer):
    TURNO_CHOICES = (
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
    )
    turno = serializers.ChoiceField(choices=TURNO_CHOICES)
    class Meta:
        model = Programacao
        fields = ['nome_programacao', 'horario', 'loucutor', 'detalhes', 'turno']