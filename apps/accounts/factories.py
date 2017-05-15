from django.contrib.auth.models import User
import factory

from utils.services import random_string


class UserFactory(factory.DjangoModelFactory):
    class Meta:
	model = User
	django_get_or_create = ('username', )

    id = factory.Sequence(lambda n: n)
    username = "username"

