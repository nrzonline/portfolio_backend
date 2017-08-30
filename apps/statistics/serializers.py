from rest_framework import serializers

from statistics.models import RequestCount


class RequestCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()

