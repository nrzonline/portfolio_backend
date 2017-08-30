from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Sum

from statistics.requests_counter import RequestCount
from statistics.serializers import RequestCountSerializer


class RequestCountViewSet(viewsets.ViewSet):
    def get_request_count(self, request, path=None):
        path_filters = self.prepare_path_filters(path=path)

        request_count = RequestCount.objects.filter(**path_filters).aggregate(count=Sum('count'))
        if not request_count['count']:
            request_count['count'] = 0

        serializer = RequestCountSerializer(request_count)
        return Response(serializer.data)

    def get_unique_request_count(self, request, path=None):
        path_filters = self.prepare_path_filters(path)

        unique_requests = RequestCount.objects.filter(**path_filters).count()
        serializer = RequestCountSerializer({'count': unique_requests})
        return Response(serializer.data)

    @staticmethod
    def prepare_path_filters(path):
        if path:
            return {'path': path}
        return {}

