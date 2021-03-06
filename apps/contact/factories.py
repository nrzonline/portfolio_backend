from django.utils.decorators import classonlymethod
import factory

from contact.models import ContactMessage


class ContactMessageFactory(factory.DjangoModelFactory):
    class Meta:
        model = ContactMessage

    name = "My name"
    organization = "Organization"
    email = "test@portfolio-test.com"
    phone_number = "06-12345678"
    subject = "Subject"
    message = "Message"
    ip_address = "192.168.0.0"

    @classonlymethod
    def as_form_data(cls, **kwargs):
        data = {
            'name': cls.name,
            'organization': cls.organization,
            'email': cls.email,
            'phone_number': cls.phone_number,
            'subject': cls.subject,
            'message': cls.message,
        }
        data.update(**kwargs)
        return data
