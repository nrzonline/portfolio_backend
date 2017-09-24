from rest_framework import serializers
from django.utils.translation import ugettext as _

from contact.models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        exclude = ('ip_address',)


class ContactMessageCustomErrorMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        exclude = ('ip_address',)
        extra_kwargs = {
            'name': {
                'error_messages': {
                    'required': _("I would like to know who you are"),
                }
            },
            'email': {
                'error_messages': {
                    'required': _("I would like an e-mail address to contact you"),
                    'invalid': _("The current e-mail address seems not to be valid"),
                }
            },
            'subject': {
                'error_messages': {
                    'required': _("Please give me a small heads-up projects the content"),
                }
            },
            'message': {
                'error_messages': {
                    'required': _("The content of of your message is missing")
                }
            }
        }

