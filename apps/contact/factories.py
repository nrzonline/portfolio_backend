from django.utils.decorators import classonlymethod
import factory

from datetime import datetime
from contact.models import ContactDetail, ContactMessage


class ContactDetailFactory(factory.DjangoModelFactory):
    class Meta:
        model = ContactDetail
        django_get_or_create = ('first_name', )

    first_name = "First name"
    last_name = "Last name"
    date_of_birth = datetime.now()
    nationality = "Nationality"
    location = "Location"
    email = "test@portfolio-test.com"
    phone_number = "06-12345678"
    website_url = "http://portfolio-test.com"
    linkedin_url = "http://linkedin.com"
    facebook_url = "http://facebook.com"
    twitter_url = "http://twitter.com"


class ContactMessageFactory(factory.DjangoModelFactory):
    class Meta:
        model = ContactMessage

    first_name = "First name"
    last_name = "Last name"
    organisation = "Organization"
    email = "test@portfolio-test.com"
    phone_number = "06-12345678"
    subject = "Subject"
    message = "Message"
    ip_address = "192.168.0.0"

    @classonlymethod
    def as_form_data(cls, **kwargs):
        data = {
            'first_name': cls.first_name,
            'last_name': cls.last_name,
            'organisation': cls.organisation,
            'email': cls.email,
            'phone_number': cls.phone_number,
            'subject': cls.subject,
            'message': cls.message,
        }
        data.update(**kwargs)
        return data
