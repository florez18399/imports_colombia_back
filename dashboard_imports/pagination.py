from rest_framework.pagination import PageNumberPagination


class ImportsProcessPagination(PageNumberPagination):
    ordering = 'adua'
    page_size = 50
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        total_vafodo = sum([import_process.vafodo for import_process in self.page])
        response.data['total_vafodo'] = total_vafodo
        return response
