from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

from votes.serializers import VoteSerializer
from votes.models import Vote, VOTE_CHOICES
from votes import vote
from core.services import get_ip_address


class VoteViewSet(viewsets.ViewSet):
    @staticmethod
    def get_object_votes(request, model, object_id):
        try:
            content_type = ContentType.objects.get(model=model)
            content_type.get_object_for_this_type(pk=object_id)
        except ObjectDoesNotExist:
            return Response({'error': 'OBJECT_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

        ip_address = get_ip_address(request)
        votes_cast = {'client_vote': None}
        filters = {
            'content_type': content_type,
            'object_id': object_id
        }

        for vote_value, choice in dict(VOTE_CHOICES).items():
            votes_cast[vote_value] = vote.get_object_vote_count(vote_value=vote_value, **filters)
        votes_cast['client_vote'] = vote.get_object_vote_value_for_ip_address(ip_address, **filters)

        serializer = VoteSerializer({'votes': votes_cast})
        return Response(serializer.data)

    @staticmethod
    def cast_object_vote(request, model, object_id, vote_value):
        try:
            content_type = ContentType.objects.get(model=model)
            content_type.get_object_for_this_type(pk=object_id)
        except ObjectDoesNotExist:
            return Response({'error': 'OBJECT_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

        ip_address = get_ip_address(request)
        vote_data = {
            'ip_address': ip_address,
            'content_type': content_type,
            'object_id': object_id,
        }
        object_vote_cast_by_ip_address = vote.get_object_vote_value_for_ip_address(**vote_data)
        if object_vote_cast_by_ip_address:
            return Response({'error': 'VOTE_ALREADY_CAST_BY_CLIENT'}, status=status.HTTP_200_OK)

        vote.cast_vote(vote_value, **vote_data)
        return Response({'success': 'VOTE_CAST'}, status=status.HTTP_200_OK)

