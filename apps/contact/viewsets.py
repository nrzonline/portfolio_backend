from rest_framework import viewsets, mixins, permissions, generics

from contact.serializers import ContactDetailSerializer, \
    ContactMessageSerializer
from contact.models import ContactDetail, ContactMessage
from utils.services import get_ip_address


class ContactDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ContactDetailSerializer
    queryset = ContactDetail.objects.all()


class ContactMessageViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        ip_address = get_ip_address(self.request)
        serializer.save(ip_address=ip_address)
