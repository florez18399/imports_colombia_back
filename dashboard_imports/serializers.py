from rest_framework import serializers

from .models import ImportProcess, Country


class ImportProcessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImportProcess
        fields = ('fech', 'adua', 'paisgen', 'paispro', 'vafodo')


class ImportProcessByProCountrySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para consulta de cantidad de procesos de importación y suma de vafodo por país de origen
    """
    num_procesos = serializers.IntegerField()
    sum_vafodo = serializers.IntegerField()

    class Meta:
        model = ImportProcess
        fields = ('paispro', 'num_procesos', 'sum_vafodo')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('cod', 'name')
