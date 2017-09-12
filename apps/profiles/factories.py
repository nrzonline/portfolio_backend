from datetime import datetime
import factory

from profiles.models import Profile


class ProfileDetailFactory(factory.DjangoModelFactory):
    class Meta:
        model = Profile
        django_get_or_create = ('first_name', )

    about = "About me..."
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

