from django.db.models import Count, Sum, F
from rest_framework import viewsets

from .pagination import ImportsProcessPagination
from .serializers import ImportProcessSerializer, ImportProcessByProCountrySerializer, CountrySerializer, \
    AduanaSerializer, ImportProcessByProCitySerializer
from .models import ImportProcess, Country, Aduana


class ImportsProcessViewSet(viewsets.ModelViewSet):
    serializer_class = ImportProcessSerializer
    pagination_class = ImportsProcessPagination

    def get_queryset(self):
        queryset = ImportProcess.objects.order_by("adua", '-vafodo').exclude(paispro=None)

        adua = self.request.query_params.get('adua', None)

        if adua is not None:
            queryset = queryset.filter(adua=adua)

        paispro = self.request.query_params.get('paispro', None)
        if paispro is not None:
            queryset = queryset.filter(paispro=paispro)

        vafodo_min = self.request.query_params.get('vafodo_min', None)
        vafodo_max = self.request.query_params.get('vafodo_max', None)
        if vafodo_min is not None and vafodo_max is not None:
            queryset = queryset.filter(vafodo__gte=vafodo_min, vafodo__lte=vafodo_max)
        elif vafodo_min is not None:
            queryset = queryset.filter(vafodo__gte=vafodo_min)
        elif vafodo_max is not None:
            queryset = queryset.filter(vafodo__lte=vafodo_max)

        return queryset


class ImportsProcessByProCountryViewSet(viewsets.ModelViewSet):
    serializer_class = ImportProcessByProCountrySerializer
    queryset = ImportProcess.objects.values('paispro', 'paispro__name')\
        .annotate(num_procesos=Count('id'), sum_vafodo=Sum('vafodo')) \
        .order_by('-sum_vafodo')


class ImportsProcessByCityViewSet(viewsets.ModelViewSet):
    serializer_class = ImportProcessByProCitySerializer
    queryset = ImportProcess.objects.values('cuidaexp')\
        .annotate(num_procesos=Count('id'), sum_vafodo=Sum('vafodo')) \
        .order_by('-num_procesos')


class ContriesView(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class AduanasView(viewsets.ModelViewSet):
    serializer_class = AduanaSerializer
    queryset = Aduana.objects.all()

