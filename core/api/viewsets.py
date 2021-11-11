from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao')
    # permission_classes = (IsAuthenticated,)  # user authentication for token, using IsAdminUser superuser permission
    # authentication_classes = (TokenAuthentication,)  # user authentication for token

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # Action GET
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    # Action POST
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # Action DELETE
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # Action GET for ID, example "...pontosturisticos/1"
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    # Action UPDATE (PUT)
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # Action PARCIAL UPDATE (PATCH)
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # Action personalizada para envio de denuncia de ponto turistico
    # @action(methods=['get', 'post'], detail=True)
    # def denunciar(self, request, pk=None):
    #    pass
