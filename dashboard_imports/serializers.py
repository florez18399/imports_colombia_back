from rest_framework import serializers

from .models import ImportProcess, Country, Aduana


class AduanaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aduana
        fields = ('adua', 'name')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('cod', 'name')


class ImportProcessSerializer(serializers.HyperlinkedModelSerializer):
    paispro = CountrySerializer()
    adua = AduanaSerializer()

    class Meta:
        model = ImportProcess
        fields = ('id', 'fech', 'adua', 'paispro', 'paisgen', 'vafodo', 'flete', 'cuidaexp', 'luin', 'baseiva')


class ImportProcessByProCountrySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para consulta de cantidad de procesos de importación y suma de vafodo por país de origen
    """
    paispro = serializers.IntegerField()
    num_procesos = serializers.IntegerField()
    sum_vafodo = serializers.IntegerField()
    paispro__name = serializers.CharField()

    class Meta:
        model = ImportProcess
        fields = ('paispro', 'paispro__name', 'num_procesos', 'sum_vafodo')


class ImportProcessByProCitySerializer(serializers.HyperlinkedModelSerializer):
    cuidaexp = serializers.CharField()
    num_procesos = serializers.IntegerField()
    sum_vafodo = serializers.IntegerField()

    class Meta:
        model = ImportProcess
        fields = ('cuidaexp', 'num_procesos', 'sum_vafodo')

