from rest_framework import viewsets, mixins, permissions

from contact.serializers import ContactMessageSerializer
from utils.services import get_ip_address


class ContactMessageViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        ip_address = get_ip_address(self.request)
        serializer.save(ip_address=ip_address)
