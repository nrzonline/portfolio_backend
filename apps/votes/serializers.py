from rest_framework import serializers


class VoteSerializer(serializers.Serializer):
    votes = serializers.JSONField()
