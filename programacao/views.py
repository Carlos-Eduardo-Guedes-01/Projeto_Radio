from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Programacao
from .serializers import ProgramacaoSerializer

class ProgramacaoViewSet(viewsets.ModelViewSet):
    queryset = Programacao.objects.all()
    serializer_class = ProgramacaoSerializer
    def create(self, request, *args, **kwargs):
        dados_formulario = request.data
        insercao = Programacao.objects.create(
            nome_programacao=dados_formulario['nome_programacao'],
            horario=dados_formulario['horario'],
            loucutor=dados_formulario['loucutor'],
            detalhes=dados_formulario['detalhes'],
            turno=dados_formulario['turno']
        )

        if insercao:
            return Response('Dados Cadastrados!')