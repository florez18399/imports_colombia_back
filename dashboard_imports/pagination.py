from rest_framework.pagination import PageNumberPagination


class ImportsProcessPagination(PageNumberPagination):
    ordering = 'adua'
    page_size = 50
    page_size_query_param = 'page_size'