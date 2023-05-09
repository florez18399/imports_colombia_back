from django.db.models import Sum
from rest_framework.pagination import PageNumberPagination


class ImportsProcessPagination(PageNumberPagination):
    ordering = 'adua'
    page_size = 50
    page_size_query_param = 'page_size'

    def paginate_queryset(self, queryset, request, view=None):
        self.total_vafodo = queryset.aggregate(total_vafodo=Sum('vafodo'))['total_vafodo']
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['total_vafodo'] = self.total_vafodo
        return response
