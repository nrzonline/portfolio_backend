from rest_framework import serializers

from statistics.models import RequestCount


class VoteSerializer(serializers.Serializer):
    votes = serializers.JSONField()
