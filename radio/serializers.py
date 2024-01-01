from rest_framework import serializers
from .models import Radio

class RadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radio
        fields = ['Nome','Frequencia','Logo','Link', 'Whatsapp','Email']
