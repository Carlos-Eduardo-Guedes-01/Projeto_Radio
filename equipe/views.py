from rest_framework import viewsets
from rest_framework.response import Response
from .models import Integrantes
from .serializers import EquipeSerializer

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Integrantes.objects.all()
    serializer_class = EquipeSerializer

    def create(self, request, *args, **kwargs):
        dados_formulario = request.data
        validador = Integrantes.objects.create(
            Nome_integrante = dados_formulario.get('Nome_integrante'),
            Telefone = dados_formulario.get('Telefone')
        )
        if(validador):
            return Response('Dados Cadastrados')
        return Response('Erro de Cadastro!')