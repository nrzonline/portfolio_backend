from rest_framework import serializers


class RequestCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()

