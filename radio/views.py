from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Radio
from .serializers import RadioSerializer
from PIL import Image

class RadioViewSet(viewsets.ModelViewSet):
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer

    def create(self, request, *args, **kwargs):
        dados_formulario = request.data
        validador = Validacao()
        resultado = validador.ValidaImagem(imagem=dados_formulario.get('Logo'))

        if not resultado['valido']:
            raise ValidationError(resultado['mensagem'])

        insercao = Radio.objects.create(
            Nome=dados_formulario['Nome'],
            Frequencia=dados_formulario['Frequencia'],
            Logo=dados_formulario['Logo'],
            Link=dados_formulario['Link']
        )

        if insercao:
            return Response('Dados Cadastrados!')
class Validacao:
    def ValidaImagem(self, imagem):
        if imagem is None:
            return {'valido': False, 'mensagem': 'A imagem é obrigatória.'}

        try:
            with Image.open(imagem) as img:
                if img.format != 'PNG':
                    return {'valido': False, 'mensagem': 'A imagem deve ser um arquivo PNG válido.'}
        except:
            return {'valido': False, 'mensagem': 'Ocorreu um erro ao abrir a imagem.'}

        return {'valido': True}
