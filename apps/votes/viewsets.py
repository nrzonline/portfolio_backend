from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType

from votes.serializers import VoteSerializer
from votes.models import Vote, VOTE_CHOICES
from votes import services
from utils.services import get_ip_address


class VoteViewSet(viewsets.ViewSet):
    def get_object_votes(self, request, model, object_id):
        content_type = ContentType.objects.get(model=model)
        votes_cast = {
            'client_vote': None,
        }

        filters = {
            'content_type': content_type,
            'object_id': object_id
        }
        for vote_value, choice in dict(VOTE_CHOICES).items():
            votes_cast[vote_value] = Vote.objects.filter(vote=vote_value, **filters).count()

        ip_address = get_ip_address(request)
        client_vote_cast = services.get_object_vote_cast_by_ip_address(ip_address, **filters)
        if client_vote_cast:
            votes_cast['client_vote'] = client_vote_cast.vote

        serializer = VoteSerializer({'votes': votes_cast})
        return Response(serializer.data)

    def cast_object_vote(self, request, model, object_id, vote):
        content_type = ContentType.objects.get(model=model)
        ip_address = get_ip_address(request)

        vote_data = {
            'ip_address': ip_address,
            'content_type': content_type,
            'object_id': object_id,
        }
        object_vote_cast_by_ip_address = services.get_object_vote_cast_by_ip_address(**vote_data)

        if not object_vote_cast_by_ip_address:
            Vote.objects.create(vote=vote, **vote_data)
            return Response({'success': 'VOTE_CAST'}, status=status.HTTP_200_OK)
        return Response({'error': 'VOTE_ALREADY_CAST_BY_CLIENT'}, status=status.HTTP_200_OK)

