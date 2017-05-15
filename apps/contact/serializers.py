from rest_framework import serializers

from contact.models import ContactDetail, ContactMessage


class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetail
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

    ip_address = serializers.IPAddressField(read_only=True)

