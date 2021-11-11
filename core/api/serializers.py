from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)  # Incluindo mais uma busca no fields do ponto turistico
    enderecos = EnderecoSerializer()  # Incluindo mais uma busca no fields do ponto turistico
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios',
            'avaliacoes', 'enderecos', 'descricao_completa', 'descricao_completa2',
        )

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
